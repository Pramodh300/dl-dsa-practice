import cv2
import numpy as np

image = cv2.imread("car.jpg")

blur = cv2.GaussianBlur(image, (5,5), 0)

gray = cv2.cvtColor(
    blur,
    cv2.COLOR_BGR2GRAY
)

kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharp = cv2.filter2D(
    gray,
    -1,
    kernal
)

cv2.imshow("Original:", image)
cv2.imshow("Blur:", blur)
cv2.imshow("Gray:", gray)
cv2.imshow("Sharp:", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()


#For Video
video = cv2.VideoCapture(0)

kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

while True :
    success, frame = video.read()

    if not success :
        break

    mean_blur = cv2.blur(frame, (7,7))

    gaussian_blur = cv2.GaussianBlur(frame, (7,7), 0)

    median_blur = cv2.medianBlur(frame, 7)

    bilateral = cv2.bilateralFilter(frame, 9, 75, 75)

    sharpen = cv2.filter2D(frame, -1, kernal)
    
    cv2.imshow("Original:", frame)
    cv2.imshow("Mean Blur:", mean_blur)
    cv2.imshow("Gaussian Blur:", gaussian_blur)
    cv2.imshow("Median Blur:", median_blur)
    cv2.imshow("Bilateral Filter:", bilateral)
    cv2.imshow("Sharpen:", sharpen)

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()