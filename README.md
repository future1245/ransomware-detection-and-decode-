# ransomware-detection-and-decode-
A beginner-friendly Python project that simulates ransomware encryption and real-time decryption monitoring in a safe, offline environment. Built using watchdog for file system monitoring and cryptography (Fernet) for encryption/decryption. For educational purposes only.

# 🛡️ Ransomware Defense Simulator

A beginner-friendly Python project that **simulates a ransomware attack and demonstrates real-time decryption** in a safe, offline environment.  
Built using [`watchdog`](https://pypi.org/project/watchdog/) for file monitoring and [`cryptography`](https://pypi.org/project/cryptography/) (Fernet) for encryption/decryption.

⚠ **Educational Purposes Only** – This project is designed to help beginners learn about ransomware behavior and defensive scripting in a controlled environment.  
Do **NOT** use any part of this code for malicious purposes.

---

## 📌 Features
- **Directory monitoring** – Watches for newly created or modified files
- **Key detection** – Identifies potential decryption keys in real time
- **Automatic decryption** – Attempts to decrypt modified files using discovered keys
- **Safe simulation** – Works entirely on dummy files in an offline test folder

---

## 🗂 Project Structure
Ransomware-Defense-Simulator/
│
├── decrypter.py # Script that monitors and decrypts files
├── ransomware_sim.py # Simulation script that encrypts files
├── test_files/ # Dummy files for safe testing
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Ransomware-Defense-Simulator.git
cd Ransomware-Defense-Simulator

```
2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Start the decrypter
```bash
python3 ranprev.py
```
4️⃣ Run the ransomware simulation (in another terminal)
```bash
python3 ransomware.py
```
⚠ Disclaimer
This project is for educational purposes only.
Do not deploy, run, or adapt this code for malicious purposes. The author is not responsible for any misuse.


---

