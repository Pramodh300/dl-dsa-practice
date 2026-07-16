import cv2
import time
model = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt",
    "res10_300x300_ssd_iter_140000_fp16.caffemodel"
)

cap = cv2.VideoCapture(0)

previous_time = time.time()

CONFIDENCE_THRESHOLD = 0.6

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        image = frame,
        scalefactor = 1.0,
        size = (300, 300),
        mean = (104.0, 177.0, 123.0),
        swapRB = False,
        crop = False
    )
    model.setInput(blob)

    detections = model.forward()

    face_detected = False
    face_count = 0

    for i in range(detections.shape[2]):
        confidence = float(detections[0, 0, i, 2])

        if confidence >= CONFIDENCE_THRESHOLD:

            face_detected = True
            face_count += 1

            box = detections[0, 0, i, 3:7] *  \
                [w, h, w, h]
            x1, y1, x2, y2 = box.astype("int")

            cv2.rectangle(
                frame, 
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            text = f"{confidence*100:.1f}"
            
            cv2.putText(
                frame,
                "Face",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    if face_detected:
        cv2.putText(
            frame,
            "Face Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:
        cv2.putText(
            frame,
            "Face Not Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )


    cv2.putText(
        frame,
        f"Faces: {face_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (350, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Face Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()