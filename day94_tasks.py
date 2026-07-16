import cv2
import time

cap = cv2.VideoCapture(0)

ret, previous_frame = cap.read()

previous_gray = cv2.cvtColor(
    previous_frame,
    cv2.COLOR_BGR2GRAY
)

previous_gray = cv2.GaussianBlur(
    previous_gray,
    (21, 21),
    0
)

previous_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (21, 21),
        0
    )

    difference = cv2.absdiff(
        previous_gray,
        gray
    )

    _, threshold = cv2.threshold(
        difference,
        25,
        255,
        cv2.THRESH_BINARY
    )

    threshold = cv2.dilate(
        threshold,
        None,
        iterations = 2
    )

    contours, _ = cv2.findContours(
        threshold,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    

    motion = False
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        motion = True

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        status = "Motion Detected" if motion else "No Motion"

        cv2.putText(
            frame,
            status,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
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


        cv2.imshow("Motion Detector", frame)
        cv2.imshow("Threshold", threshold)
        cv2.imshow("Difference", difference)

        previous_gray = gray.copy()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()