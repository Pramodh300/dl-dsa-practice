import cv2
import numpy as np

img = cv2.imread("marker.jpg")

hsv = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2HSV
)

lower_blue = np.array(
    [100, 100, 100]
)

upper_blue = np.array(
    [140,255,255]
)

mask = cv2.inRange(
    hsv,
    lower_blue,
    upper_blue
)

cv2.imshow(
    "Mask",
    mask
)

cv2.waitKey(0)
cv2.destroyAllWindows()


#For video
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if success == False:
        break

    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )

    lower_blue = np.array(
        [100,100,100]
    )

    upper_blue = np.array(
        [140, 255, 255]
    )

    mask = cv2.inRange(
        hsv,
        lower_blue,
        upper_blue
    )

    result = cv2.bitwise_and(
        frame,
        frame,
        mask = mask
    )

    cv2.imshow(
        "Original Camera",
        frame
    )

    cv2.imshow(
        "Mask",
        mask
    )

    cv2.imshow(
        "Detected Color",
        result
    )

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()