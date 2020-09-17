import cv2

capture = cv2.VideoCapture("videos/run.mp4")

while cv2.waitKey(1) < 0:

    classifier = cv2.CascadeClassifier("haarcascadefiles/haarcascade_frontalface_alt.xml")
    hasframe, frame = capture.read()
    faces = classifier.detectMultiScale(frame)

    if not hasframe:
        break

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))
    cv2.imshow("run", frame)

cv2.destroyAllWindows()
