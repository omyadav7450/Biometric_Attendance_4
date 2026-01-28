import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STUDENTS_DIR = os.path.join(DATA_DIR, "students")
FACES_DIR = os.path.join(DATA_DIR, "faces")

FACULTIES = ["Science", "Management"]
CLASSES = ["11", "12"]
SECTIONS = ["A", "B", "C"]

# ---------- CREATE BASE FOLDER STRUCTURE ----------
for faculty in FACULTIES:
    for cls in CLASSES:
        for section in SECTIONS:
            stu_path = os.path.join(STUDENTS_DIR, faculty, cls, section)
            face_path = os.path.join(FACES_DIR, faculty, cls, section)
            os.makedirs(stu_path, exist_ok=True)
            os.makedirs(face_path, exist_ok=True)

            csv_file = os.path.join(stu_path, "students.csv")
            if not os.path.exists(csv_file):
                df = pd.DataFrame(columns=["ID", "Name", "Class", "Faculty", "Section", "Contact", "Email"])
                df.to_csv(csv_file, index=False)

print("🎉 All folders are ready!")

# ---------- INTERACTIVE ADD STUDENTS ----------
def add_student():
    print("\nSelect Faculty:")
    for i, f in enumerate(FACULTIES, 1):
        print(f"{i}. {f}")
    fac_choice = int(input("Enter number: ")) - 1
    faculty = FACULTIES[fac_choice]

    print("\nSelect Class:")
    for i, c in enumerate(CLASSES, 1):
        print(f"{i}. {c}")
    cls_choice = int(input("Enter number: ")) - 1
    cls = CLASSES[cls_choice]

    print("\nSelect Section:")
    for i, s in enumerate(SECTIONS, 1):
        print(f"{i}. {s}")
    sec_choice = int(input("Enter number: ")) - 1
    section = SECTIONS[sec_choice]

    sid = input("\nEnter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    contact = input("Enter Contact (optional): ").strip()
    email = input("Enter Email (optional): ").strip()

    # Save to CSV
    csv_file = os.path.join(STUDENTS_DIR, faculty, cls, section, "students.csv")
    df = pd.read_csv(csv_file)
    if sid in df["ID"].astype(str).values:
        print(f"⚠ Student ID {sid} already exists! Skipping.")
        return
    df.loc[len(df)] = [sid, name, cls, faculty, section, contact, email]
    df.to_csv(csv_file, index=False)

    # Create face folder
    face_path = os.path.join(FACES_DIR, faculty, cls, section, str(sid))
    os.makedirs(face_path, exist_ok=True)

    print(f"✅ Added Student: {sid} - {name}\nFace folder created at {face_path}")

# ---------- RUN ADDITION LOOP ----------
while True:
    add_student()
    again = input("\nAdd another student? (y/n): ").lower()
    if again != 'y':
        break

print("\n🎉 Student data entry complete!")
