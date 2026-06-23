#!/usr/bin/env python3
"""
Verify the PGP signature for the FIASANOVA Quantum Seal.
"""

import subprocess
import sys
import os

def verify_signature():
    sig_path = "../signatures/fiasanova_pgp_signature.asc"
    file_path = "../proofs/fiasanova_quantum_seal.pdf"
    
    if not os.path.exists(sig_path) or not os.path.exists(file_path):
        print("❌ Signature or file not found.")
        return False
    
    try:
        result = subprocess.run(
            ["gpg", "--verify", sig_path, file_path],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if "Good signature" in result.stdout:
            print("✅ Signature verified successfully.")
            return True
        else:
            print("❌ Verification failed.")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if verify_signature() else 1)
