# Wi-Fi Scanner & Password Tester

A Python-based **GUI tool** built with Tkinter that scans nearby Wi-Fi networks, allows you to select one, and tests passwords from a provided list to find the correct one. If a matching password is found, the program generates a **QR code** for easy sharing.

> ⚠ **Disclaimer:** This tool is for educational and authorized testing purposes only. Using it on networks without permission is illegal.

---

## 🚀 Features

- **Scan Available Networks**
  - Uses `nmcli` to detect nearby Wi-Fi SSIDs.
  - Displays results in a table view.

- **Select a Target Network**
  - Click to choose an SSID from the scanned list.

- **Load Password List**
  - Import a `.txt` file containing possible passwords.

- **Automated Password Testing**
  - Attempts to connect using each password.
  - Stops once the correct password is found.

- **QR Code Generation**
  - Creates a scannable QR code for the discovered network.
  - Displays it in a new Tkinter window.

- **User-Friendly Interface**
  - Built with Tkinter and ttk for a responsive GUI.
  - Interactive message boxes for guidance and results.

---

## 🛠 Requirements

- Python 3.12
- System tool: `nmcli` (Linux only, with NetworkManager installed)
- Sudo privileges for connecting to networks.

**Python libraries:**
- tkinter (standard python library)
- subprocess (standard python library)
- time (standard python library)
- qrcode
- Pillow

**Steps for Library Installation:**
```bash
pip install qrcode Pillow
```
(Tkinter is included with most Python installations. On Linux, you may need to install it with:)
```
sudo apt install python3-tk
```

## 📂 Project Structure

```
WiFi--Scanner-Password-Tester/
│
├── main.py                # Main application file
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── passwords.txt          # Example password list (optional)
```

## 📦 Installation Steps

**1️⃣ Clone the repository**
```
git clone https://github.com/VARDAAN17/WiFi--Scanner-Password-Tester
cd WiFi--Scanner-Password-Tester
```

**2️⃣ Create and activate a virtual environment**
```
python3 -m venv venv
source venv/bin/activate
```
**3️⃣ Install dependencies from 'requirements.txt'**
```
pip install -r requirements.txt
```

**4️⃣ Install system dependencies**
```
sudo apt install python3-tk network-manager
```

**5️⃣ Run the program**
```
python main.py
```

## ▶ Usage

**1️⃣ Run the script:**
```
python3 main.py
```

**2️⃣ Scan Networks:**

- Click "Scan Wi-Fi Networks" to detect nearby SSIDs.

**3️⃣ Select Network:**

- Highlight a network in the table and click "Select Network".

**4️⃣ Load Password File:**

- Choose a .txt file with one password per line.

**5️⃣ Run Password Scan:**

- Click "Run Password Scan" to start testing passwords.

**6️⃣ QR Code:**

- If a correct password is found, a QR code will be displayed in a new window.



## ⚠ Disclaimer

This tool is strictly for educational purposes or for testing networks you own or have explicit permission to test. Unauthorized use is illegal and punishable under law. The author is not responsible for misuse of this tool.
