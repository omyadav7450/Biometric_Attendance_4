import cv2, os, pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STUDENTS_DIR = os.path.join(DATA_DIR, "students")
FACES_DIR = os.path.join(DATA_DIR, "faces")

FACULTIES = ["Science", "Management"]
CLASSES = ["11", "12"]
SECTIONS = ["A", "B", "C"]

def capture_faces():
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
    csv_file = os.path.join(STUDENTS_DIR, faculty, cls, section, "students.csv")
    df = pd.read_csv(csv_file)
    if sid not in df["ID"].astype(str).values:
        print("❌ Student ID not found. Enter data in data_entry.py first!")
        return
    name = df.loc[df["ID"].astype(str) == sid, "Name"].values[0]

    # Create face folder
    save_path = os.path.join(FACES_DIR, faculty, cls, section, str(sid))
    os.makedirs(save_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    count = 0
    num_images = 100
    print(f"📸 Capturing {num_images} faces for {name} ({sid})... Press Q to stop early.")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))
            count += 1
            cv2.imwrite(os.path.join(save_path, f"{count}.jpg"), face)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"{name} {count}/{num_images}", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        cv2.imshow("Capture Faces", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or count >= num_images:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"✅ Captured {count} images for {name}")

# Run capture
capture_faces()
