#!/usr/bin/env python3
"""
Verify the OpenTimestamps receipt for the FIASANOVA Quantum Seal.
"""

import subprocess
import sys
import os

def verify_timestamp():
    receipt_path = "../proofs/fiasanova_quantum_seal.pdf.ots"
    if not os.path.exists(receipt_path):
        print("❌ Receipt file not found.")
        return False
    
    try:
        result = subprocess.run(
            ["ots", "verify", receipt_path],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if "Success" in result.stdout or "anchored" in result.stdout.lower():
            print("✅ Timestamp verified successfully.")
            return True
        else:
            print("❌ Verification failed.")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if verify_timestamp() else 1)
