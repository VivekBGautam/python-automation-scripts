# 💻 Scripts on Command Line

## 📌 Aim
To execute and manage Python scripts directly from the command line using user-provided inputs and arguments.

---

## 📖 Description
Scripts on Command Line is a Python-based project that allows users to run scripts using command-line arguments. It helps in creating flexible and dynamic programs where inputs can be passed at runtime without modifying the code.

---

## ⚙️ Features
- Execute scripts via command line
- Accept user inputs using arguments
- Easy automation and flexibility
- Supports multiple commands
- Lightweight and fast execution

---

## 🛠️ Technologies Used
- Python 3.x
- sys module
- argparse module

---

## 📁 File Structure
scripts-on-command-line/
│── main.py
│── commands/
│   ├── command1.py
│   ├── command2.py
│── README.md

---

## 🚀 Installation

1. Clone the repository:
git clone https://github.com/vivekbgautam/scripts-on-command-line.git

2. Navigate to the project folder:
cd scripts-on-command-line

---

## ▶️ Usage

Run the script with arguments:
python main.py --name Vivek

Example:
python main.py --task greet --name Vivek

---

## 🧾 Example Code

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", type=str, help="Enter your name")
args = parser.parse_args()

if args.name:
    print(f"Hello, {args.name}!")

---

## 📌 Use Cases
- CLI tools and utilities
- Automation scripts
- Data processing tasks
- Quick command-based programs

---

## 🔮 Future Enhancements
- Add more command options
- Integrate with external APIs
- Build advanced CLI tools
- Add help and documentation commands

---

## 👨‍💻 Author
Vivek Gautam  
Email: vivekbgautam@gmail.com  
GitHub: https://github.com/vivekbgautam  
LinkedIn: https://www.linkedin.com/in/vivek-b-gautam/
