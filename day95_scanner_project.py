import cv2
import numpy as np

def order_points(pts):
    pts = pts.reshape(4,2)
    rect = np.zeros((4,2), dtype="float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff) ]
    rect[3] = pts[np.argmax(diff)]


    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)

    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)

    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxHeight = max(int(heightA), int(heightB))

    destination = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
        ], dtype = 'float32')
    
    matrix = cv2.getPerspectiveTransform(rect, destination)

    warped = cv2.warpPerspective(
        image,
        matrix,
        (maxWidth, maxHeight)
    )

    return warped

image_path = "document1.png"
image = cv2.imread(image_path)

if image is None:
    print(f"Image not found: {image_path}")
    exit()

image = cv2.resize(image, (800, 600))

original = image.copy()

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

blur = cv2.GaussianBlur(
    gray,
    (5,5),
    0
)

edges = cv2.Canny(
    blur,
    30,
    150
)

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

document = None
for contour in contours:

    area = cv2.contourArea(contour)

    if area < 10000:
        continue

    perimeter = cv2.arcLength(
        contour,
        True
    )

    approx = cv2.approxPolyDP(
        contour,
        0.02 * perimeter,
        True
    )

    if len(approx) == 4:
        document = approx
        break

if document is None:
    print("No document detected!")

    cv2.imshow("Original", original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()

contour_image = original.copy()

cv2.drawContours(
    contour_image,
    [document],
    -1,
    (0, 255, 0),
    3
)

warped = four_point_transform(
    original,
    document
)

warped_gray = cv2.cvtColor(
    warped,
    cv2.COLOR_BGR2GRAY
)

scanned = cv2.adaptiveThreshold(
    warped_gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)


cv2.imshow("Original", original)
cv2.imshow("Edges", edges)
cv2.imshow("Detected Document", contour_image)
cv2.imshow("Warped", warped)
cv2.imshow("Scanned Document", scanned)

cv2.waitKey(0)
cv2.destroyAllWindows()