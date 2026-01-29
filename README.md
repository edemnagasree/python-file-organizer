# 🗂️ Python File Organizer

## 📌 Overview
This is a simple Python script that automatically organizes files in a folder into categories:
- **Images** → jpg, png, jpeg  
- **Documents** → pdf, docx, txt  
- **Videos** → mp4, mkv  
- **Others** → everything else  

It helps keep your folders clean by sorting files into subfolders.

---

## ⚙️ How It Works
1. The script scans the folder you specify.
2. It checks each file’s extension.
3. Based on the extension, it moves the file into a subfolder (`Images`, `Docs`, `Videos`, or `Others`).
4. If the subfolder doesn’t exist, it creates it automatically.

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/python-file-organizer.git
2. Navigate into the folder:
cd python-file-organizer
3. Run the script:
python file_organizer.py


4. By default, it organizes files in:
C:/Users/YourName/Downloads

5. 👉 You can change this path in the last line of the script.

📚 Tech Stack
- Python 3
- Built-in modules: os, shutil


