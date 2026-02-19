# Human_First_Protocol_Command_cryptographic
Irreversible_ENCODED

## 🔐 Cryptographic Proof of Existence
The FIASANOVA QUANTUM SIGNATURE was cryptographically timestamped on the Bitcoin blockchain on **February 19, 2026**.

**File:** FIASANOVA_QUANTUM_SIGNATURE - PNG ENCODED.pdf  
**SHA256:** `fd128112b0e06c6857f0f1cc4515936ba58fbded5dc17232bc4d97d36adeda62`  
**Proof:** [OpenTimestamps Receipt](proofs/FIASANOVA_QUANTUM_SIGNATURE_PNG_ENCODED.pdf.ots)

Verify: `ots verify proofs/FIASANOVA_QUANTUM_SIGNATURE_PNG_ENCODED.pdf.ots`

### 🧾 How to verify the timestamp

1. **Install the OpenTimestamps client** (if you haven’t already):
   ```bash
   pip install opentimestamps-client
   ```
2. **Download** or place both the original PDF and the `.ots` receipt in the same folder.
3. **Run the verify command** from the repository root:
   ```bash
   ots verify proofs/FIASANOVA_QUANTUM_SIGNATURE_PNG_ENCODED.pdf.ots
   ```
   You should see output confirming the receipt is anchored in the Bitcoin blockchain.

4. The command works offline once the calendar file has been fetched; you can repeat verification anytime.

---

## 🛠️ Reference Implementation Framework

This repository now includes a minimal Python-based framework that demonstrates
how the **Human First Protocol** might manage cryptographic timestamping and
proof verification. It is intended as a starting point for community
contributions and further experimentation.

### 📁 Project Layout

```
/ (root)
├── cli.py                 # simple command‑line interface
├── human_first_protocol/  # Python package
│   ├── __init__.py
│   └── timestamp.py       # timestamping helpers
├── proofs/                # OpenTimestamps receipts
├── tests/                 # unit tests
├── README.md
├── requirements.txt
└── pyproject.toml         # build metadata
```

### 🚀 Getting started

1. **Install dependencies** (inside a virtualenv):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Install the OpenTimestamps CLI** (required by the helpers):
   ```bash
   pip install opentimestamps-client
   ```
3. **(optional)** make the package importable for development:
   ```bash
   pip install -e .
   ```

### 🔧 Usage examples

Create a timestamp for a file:

```bash
python cli.py timestamp some-document.pdf
```

Verify a receipt:

```bash
python cli.py verify proofs/some-document.pdf.ots
```

You can also import the helpers directly from Python:

```python
from human_first_protocol import timestamp

receipt = timestamp.timestamp_file("foo.txt")
assert timestamp.verify_receipt(receipt)
```

### ✅ Running tests

```bash
pip install pytest
pytest
```

The repository contains a basic suite that verifies error conditions and,
if ``ots`` is installed on your system, performs an end-to-end timestamp/verify
cycle.

### 📈 Next steps

- Expand the cryptographic primitives (e.g. add signing, hashing, etc.)
- Build a web service or CLI to batch-process proofs
- Add documentation on the Human First Protocol itself

---

