"""Human First Protocol cryptographic utilities.

This package provides basic functionality to support timestamping files and
verifying proofs using OpenTimestamps, along with bare-bones stubs for the
Human First Protocol itself.  It is intended as a starting point for an
open-source reference implementation of the concept.

The module exports both the new ``HumanFirstProtocol`` class and a couple of
legacy convenience functions for backwards compatibility.
"""

__version__ = "0.1.0"

from .protocol import HumanFirstProtocol

# legacy helpers (re-exported for scripts that imported them directly)
from . import protocol as _protocol_module

check_human_sovereignty = _protocol_module.HumanFirstProtocol().check_human_sovereignty
log_transparency = _protocol_module.HumanFirstProtocol().log_transparency
requires_consent = _protocol_module.HumanFirstProtocol().requires_consent
