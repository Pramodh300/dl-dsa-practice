import cv2
'''cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    cv2.imshow("Original: ", frame)
    cv2.imshow("Gray: ",gray)
    cv2.imshow("Binary: ",binary)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    threshold, otsu = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imshow("Original: ", frame)
    cv2.imshow("Gray: ",gray)
    cv2.imshow("Otsu: ",otsu)
    cv2.imshow("Threshold: ", threshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()