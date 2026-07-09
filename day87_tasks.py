#image crop + Resize Pipeline
import cv2
img = cv2.imread(
    "Person.jpg"
)

print(
    "Original: ",
    img.shape
)

roi = img[
    100:400,
    200:500
]

resized = cv2.resize(
    roi,
    (224,224)
)

print("Final: ",resized.shape)

cv2.imshow(
    "ROI",
    resized
)

cv2.waitKey(0)
cv2.destroyAllWindows()