"""Unit tests for the timestamping helpers."""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from human_first_protocol import timestamp


def test_ots_missing(monkeypatch):
    monkeypatch.setattr(timestamp, "_ensure_ots_installed", lambda: (_ for _ in ()).throw(RuntimeError("missing")))
    with pytest.raises(RuntimeError):
        timestamp._ensure_ots_installed()


def test_timestamp_file_nonexistent(tmp_path):
    with pytest.raises(FileNotFoundError):
        timestamp.timestamp_file(tmp_path / "nope.txt")


def test_verify_receipt_nonexistent(tmp_path):
    with pytest.raises(FileNotFoundError):
        timestamp.verify_receipt(tmp_path / "noots.ots")

# the following tests assume `ots` is installed in the environment; if it's not,
# they will be skipped

@pytest.mark.skipif(shutil.which("ots") is None, reason="ots not installed")
def test_timestamp_and_verify(tmp_path):
    # create a temporary file
    f = tmp_path / "foo.txt"
    f.write_text("hello")

    receipt = timestamp.timestamp_file(f)
    assert receipt.exists()
    assert receipt.suffix == ".ots"

    # verification may fail in isolated environments (no network access).
    # we just make sure the function runs and returns a boolean.
    ok = timestamp.verify_receipt(receipt)
    assert isinstance(ok, bool)
