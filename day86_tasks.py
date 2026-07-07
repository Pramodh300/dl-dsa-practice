import cv2
camera = cv2.VideoCapture(0)

while True:
    status,frame = camera.read()

    if status == False:
        break

    cv2.putText(
        frame,
        "AI Camera",
        (50,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    cv2.imshow(
        "Output",
        frame
    )

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()