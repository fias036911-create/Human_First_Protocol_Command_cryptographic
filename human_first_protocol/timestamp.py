"""Timestamping helpers using the OpenTimestamps client.

These functions wrap the `ots` CLI; a future version might call a library or
use a network API directly. They are deliberately simple so that newcomers can
understand and extend them.
"""

import shutil
import subprocess
from pathlib import Path


def _ensure_ots_installed():
    """Raise :class:`RuntimeError` if the ``ots`` command is not found."""
    if shutil.which("ots") is None:
        raise RuntimeError("OpenTimestamps client (`ots`) is not installed or not in PATH")


def timestamp_file(path: Path) -> Path:
    """Create an OpenTimestamps receipt for ``path``.

    :param path: path to the file to timestamp
    :returns: path to the generated receipt (``<file>.ots``)
    :raises RuntimeError: if the ``ots`` tool is missing or the command fails
    """
    _ensure_ots_installed()
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"{path} does not exist or is not a file")

    receipt = path.with_suffix(path.suffix + ".ots")
    # the CLI subcommand is called "stamp" in current ots versions
    result = subprocess.run(["ots", "stamp", str(path)], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"timestamping failed: {result.stderr.strip() or result.stdout.strip()}"
        )
    return receipt


def verify_receipt(receipt: Path) -> bool:
    """Verify an OpenTimestamps receipt.

    :param receipt: path to a ``.ots`` file
    :returns: ``True`` if verification succeeded, ``False`` otherwise
    :raises RuntimeError: if the ``ots`` tool is missing
    """
    _ensure_ots_installed()
    receipt = Path(receipt)
    if not receipt.is_file():
        raise FileNotFoundError(f"{receipt} does not exist or is not a file")

    result = subprocess.run(["ots", "verify", str(receipt)], capture_output=True, text=True)
    if result.returncode == 0:
        return True
    # try upgrading the receipt and verify again; some environments need this
    subprocess.run(["ots", "upgrade", str(receipt)], capture_output=True, text=True)
    result = subprocess.run(["ots", "verify", str(receipt)], capture_output=True, text=True)
    return result.returncode == 0
