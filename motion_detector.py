import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(0)

backSub = cv2.createBackgroundSubtractorMOG2(
    history = 500,
    varThreshold=16,
    detectShadows=True
)

kernal = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (5,5)
)

previous_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    mask = backSub.apply(frame)

    _,mask = cv2.threshold(
        mask,
        200,
        255,
        cv2.THRESH_BINARY
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernal
    )

    mask = cv2.dilate(
        mask,
        kernal,
        iterations = 2
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    

    motion_detected = False
    object_count = 0

    for contour in contours:
        if cv2.contourArea(contour) < 1500:
            continue

        motion_detected = True
        object_count += 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        status = "Motion Detected" if motion_detected else "No Motion"

        cv2.putText(
            frame,
            status,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0) if motion_detected else (0, 0, 255),
            2
        )

        cv2.putText(
            frame,
            f"Objects : {object_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
        )

        current_time = time.time()

        fps = 1/(current_time - previous_time)

        previous_time = current_time

        cv2.putText(
            frame,
            f"FPS : {int(fps)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )


        current_clock = datetime.now().strftime("%H:%M:%S")

        cv2.putText(
            frame,
            current_clock,
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )


        cv2.imshow("Motion Detector", frame)
        cv2.imshow("Foreground Mask",mask)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()