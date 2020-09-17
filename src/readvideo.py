import cv2

capture = cv2.VideoCapture("videos/run.mp4")

while cv2.waitKey(1) < 0:
    hasframe, frame = capture.read()
    if not hasframe:
        break
    cv2.imshow("run", frame)

cv2.destroyAllWindows()
