import cv2, os, numpy as np, pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACES_DIR = os.path.join(BASE_DIR, "data", "faces")
MODEL_DIR = os.path.join(BASE_DIR, "model")
os.makedirs(MODEL_DIR, exist_ok=True)

recognizer = cv2.face.LBPHFaceRecognizer_create()
faces = []
labels = []
label_ids = {}
current_id = 0

for faculty in os.listdir(FACES_DIR):
    faculty_path = os.path.join(FACES_DIR, faculty)
    for cls in os.listdir(faculty_path):
        cls_path = os.path.join(faculty_path, cls)
        for section in os.listdir(cls_path):
            section_path = os.path.join(cls_path, section)
            for student_id in os.listdir(section_path):
                student_path = os.path.join(section_path, student_id)
                for img_name in os.listdir(student_path):
                    img_path = os.path.join(student_path, img_name)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is None:
                        continue
                    faces.append(img)
                    label_text = os.path.join(faculty, cls, section, student_id)
                    if label_text not in label_ids:
                        label_ids[label_text] = current_id
                        current_id += 1
                    labels.append(label_ids[label_text])

labels = np.array(labels)
recognizer.train(faces, labels)
recognizer.save(os.path.join(MODEL_DIR, "trainer.yml"))

with open(os.path.join(MODEL_DIR, "labels.pkl"), "wb") as f:
    pickle.dump(label_ids, f)

print("🎉 Model trained successfully!")
