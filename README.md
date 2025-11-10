# 🧮 IP Subnet Calculator (Class C)

A simple Python script to calculate **Network ID**, **Broadcast Address**, and **Subnet Mask** for **Class C IP addresses**.  
This script is designed for students learning subnetting or anyone who wants a quick command-line subnet calculator.

---

## 🚀 Features

- Supports **Class C** IPv4 addresses (e.g., `192.180.35.220/27`)
- Automatically calculates:
  - Network ID
  - Broadcast Address
  - Subnet Mask
  - Number of Hosts per Subnet
- Clear and step-by-step explanation of the calculation
- Works on **Windows**, **Linux**, and **macOS**

---

## 🧰 Requirements

- Python 3.x
- Works on any terminal that supports Python

---

## ⚙️ How to Use

1. Clone or download this repository  
   ```bash
   git clone https://github.com/hanlyz/ip-subnet-calculator.git
   cd ip-subnet-calculator
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Enter your IP address and subnet prefix when prompted:
   ```
   Enter Class C IP (example: 192.180.35.220/27):
   ```

4. The program will show the results:
   ```
   ==============================
   Question: 192.180.35.220/27

     Octet 4     220
   ----------- = ----- = 6.875
   Total hosts   32
   ==============================

   ==== ( Calculate NET ID )
   Net ID = Quotient x Total Hosts
          = 6 x 32
          = 192
   Net ID = 192.180.35.192 <---

   ==== ( Calculate Broadcast )
   Broadcast  = Starting IP + Total Hosts - 1
              = 192 + 32 - 1
              = 223
   Broadcast = 192.180.35.223 <---

   ==== ( Calculate Subnetmask )
   Subnetmask  = IP Total - Total Hosts
               = 256 - 32
               = 224
   Subnetmask = 255.255.255.224 <---
   ```

5. Press **Enter** to return or exit.

---

## 🧩 Example Input / Output

| Input IP | Prefix | Network ID | Broadcast | Subnet Mask | Hosts |
|-----------|---------|-------------|------------|--------------|--------|
| 192.180.35.220 | /27 | 192.180.35.192 | 192.180.35.223 | 255.255.255.224 | 32 |
| 192.168.1.10 | /29 | 192.168.1.8 | 192.168.1.15 | 255.255.255.248 | 8 |

---

## 🧠 Notes

- The script focuses on **Class C IP calculations** (first octet 192–223).
- It’s made for **learning and demonstration** purposes — not for production networking tools.
- Output is designed to be **educational**, showing each calculation step.

---

## 👨‍💻 Author

- **Created by:** Farhan
- **GitHub:** hanlyz

---
