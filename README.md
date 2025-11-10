# 🧮 IP Subnet Calculator 

A simple Python script to calculate **Network ID**, **Broadcast Address**, and **Subnet Mask** for **Class B and Class C** IP addresses.  
This project is designed for networking students learning **subnetting** or anyone who needs a simple command-line subnet calculator.

---

## 🚀 Features

- Supports **Class B** and **Class C** IPv4 addresses  
- Automatically calculates:
  - Network ID  
  - Broadcast Address  
  - Subnet Mask  
  - Number of Hosts per Subnet  
- Provides **step-by-step explanations** of all calculations  
- Works on **Windows**, **Linux**, and **macOS**

---

## 🧰 Requirements

- Python 3.x  
- Any terminal that supports Python

---

## ⚙️ How to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/hanlyz/ip-subnet-calculator.git
   cd ip-subnet-calculator
   ```

2. Run the program:
   ```bash
   python main.py
   ```

3. Choose one of the available options:
   ```
   1. Calculate IP Class B
   2. Calculate IP Class C
   3. Exit
   ```

4. Enter the IP address and prefix when prompted:
   ```
   Enter Class B IP (example: 172.80.50.150/18)
   ```
   or
   ```
   Enter Class C IP (example: 192.180.35.220/27)
   ```

5. The program will display detailed results:
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

6. Press **Enter** to return to the menu or **Exit** the program.

---

## 🧩 Example Comparison

| Input IP | Class | Prefix | Network ID | Broadcast | Subnet Mask | Hosts |
|-----------|--------|---------|-------------|------------|--------------|--------|
| 172.80.50.150 | B | /18 | 172.80.0.0 | 172.80.63.255 | 255.255.192.0 | 16 |
| 192.180.35.220 | C | /27 | 192.180.35.192 | 192.180.35.223 | 255.255.255.224 | 32 |

---

## 🧠 Notes

- **Class B:** First octet 128–191  
- **Class C:** First octet 192–223  
- This tool is for **educational purposes** and demonstrations — not for production networking tools.  
- The output is designed to be **easy to understand** and **educational**.

---

## 👨‍💻 Author

- **Created by:** Farhan  
- **GitHub:** [hanlyz](https://github.com/hanlyz)
