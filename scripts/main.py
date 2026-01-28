import cv2, os, pickle, pandas as pd
from datetime import datetime, time as dtime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")
ATT_DIR = os.path.join(BASE_DIR, "attendance")
STUDENT_DIR = os.path.join(BASE_DIR, "data", "students")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(os.path.join(MODEL_DIR, "trainer.yml"))

with open(os.path.join(MODEL_DIR, "labels.pkl"), "rb") as f:
    labels = pickle.load(f)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

P_END = dtime(6,25)
L_END = dtime(18,0)

marked = set()
cap = cv2.VideoCapture(0)
#ip_cam_url = "http://10.116.64.158:8080/video"  # replace with your IP
#cap = cv2.VideoCapture(ip_cam_url)


print("Attendance system running (Press Q to quit)")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_detected = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces_detected:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200,200))

        label, conf = recognizer.predict(face)

        if conf < 65:
            try:
                info = [k for k,v in labels.items() if v==label][0]
                faculty, cls, section, sid = info.split(os.sep)
            except:
                continue

            now = datetime.now().time()
            if now <= P_END:
                status = "P"
            elif now <= L_END:
                status = "L"
            else:
                status = "A"

            path = os.path.join(ATT_DIR, faculty, cls, section)
            os.makedirs(path, exist_ok=True)
            day_file = os.path.join(path, datetime.now().strftime("%Y-%m-%d")+".xlsx")

            stu_csv = os.path.join(STUDENT_DIR, faculty, cls, section, "students.csv")
            if not os.path.exists(stu_csv):
                continue
            stu_df = pd.read_csv(stu_csv)

            if os.path.exists(day_file):
                df = pd.read_excel(day_file)
            else:
                df = stu_df[["ID","Name"]].copy()
                df["Status"] = ""

            if sid not in marked:
                marked.add(sid)
                df.loc[df["ID"].astype(str)==sid,"Status"] = status
                df.to_excel(day_file, index=False)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,f"ID:{sid} {status} ({int(conf)})",(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
        else:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,"Unknown",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

    cv2.imshow("Biometric Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Attendance system closed")
