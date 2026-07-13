import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blur, 100, 200)

    contours, hierachy = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    #Draw Every Contour
    for contour in contours:
        area = cv2.contourArea(contour)

        if area < 500:
            continue

        cv2.drawContours(frame, [contour], -1, (0,255,0), 2)

        perimeter = cv2.arcLength(contour, True)

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x,y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Area: {int(area)}",
            (x,y - 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Perimeter: {int(perimeter)}",
            (x,y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        cv2.imshow("Original", frame)
        cv2.imshow("Gray", gray)
        cv2.imshow("Blur", blur)
        cv2.imshow("Edges", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()