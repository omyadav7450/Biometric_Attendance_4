# Biometric_Attendance_4
Face recognition based attendance system using Python &amp; OpenCV

📸 Biometric Attendance System (Face Recognition)

A face recognition–based attendance system built using Python and OpenCV.
The system captures student faces, trains a recognition model, and automatically marks attendance using a live camera feed.

⚠️ Privacy-first design: Personal images, names, attendance files, and trained models are ignored from GitHub using .gitignore.


🚀 Features

📷 Face capture with interactive data entry

🤖 Face recognition using OpenCV (LBPH)

🧠 Automatic model training

📝 Attendance stored section-wise

🔒 Privacy-safe GitHub sharing

💻 Works on laptop webcam or IP Webcam (mobile)


🛠️ Tech Stack

Python 3.10 / 3.11

OpenCV

NumPy

CSV (attendance storage)

Git & GitHub


📁 Project Structure

Biometric_Attendance_4/
│
├── scripts/
│   ├── main.py                # Run   attendance system
│   ├── data_entry.py          # Student data entry
│   ├── capture_faces.py       # Capture face images
│   ├── train_model.py         # Train face recognizer
│
├── data/
│   ├── faces/                 # (ignored) captured face images
│   ├── students/              # (ignored) student info
│
├── attendance/                # (ignored) attendance records
│
├── model/
│   └── trainer.yml            # (ignored) trained model
│
├── .gitignore
├── README.md
└── requirements.txt

🔒 Privacy & GitHub Safety

The following are NOT uploaded to GitHub:

Student images

Student names & IDs

Attendance records

Trained face model

This ensures:
✅ Your personal data is safe
✅ Others must train their own data

⚙️ Installation
1️⃣ Clone the repository
bash- git clone https://github.com/YOUR_USERNAME/Biometric_Attendance_4.git
cd Biometric_Attendance_4

2️⃣ Create virtual environment
bash-python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
bash-pip install -r requirements.txt


▶️ How to Run (Step-by-Step)
Step 1: Student Data Entry
bash-python scripts/data_entry.py

-Interactive input (ID, name, section)
-Minimal typing, no confusion

Step 2: Capture Faces
bash-python scripts/capture_faces.py

-Uses webcam or IP Webcam
-Captures multiple samples per student

Step 3: Train Model
bash-python scripts/train_model.py

-Generates face recognition model

Step 4: Run Attendance System
bash-python scripts/main.py

-Live face detection
-Auto attendance marking
-Press Q to quit


📱 Using Mobile Camera (IP Webcam)
1. Install IP Webcam app on Android
2. Start server in app
3. Copy the camera URL (example):

http://192.168.1.5:8080/video

4. Paste URL inside the script where camera source is defined

🧠 Common Issues & Solutions
❌ Face not recognized properly
✔ Improve lighting
✔ Capture more face samples
✔ Use mobile IP Webcam (better quality)
✔ Avoid blur & side angles

❌ Camera opens & closes immediately
✔ Run using:

bash-python scripts/main.py
✔ Do NOT double-click .py files

📌 Future Improvements
-Web Version Development
-GUI (Tkinter / PyQt)
-Database (MySQL / SQLite)
-Mask detection
-Multi-camera support
-Cloud sync
-Twins detection error solution

👨‍💻 Author
Om Yadav
Student | Python Developer | AI Enthusiast |Web Developer(Frontend)

⭐ Support
If you like this project:

⭐ Star the repo

🍴 Fork it

🧠 Improve it

