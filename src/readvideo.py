import cv2
print(cv2.getBuildInformation())
capture = cv2.VideoCapture("videos/run.mp4")

while cv2.waitKey(1) < 0:

    #load classifier
    face_classifier = cv2.CascadeClassifier("haarcascadefiles/haarcascade_frontalface_alt.xml")
    eyes_classifier = cv2.CascadeClassifier("haarcascadefiles/haarcascade_eye.xml")

    hasframe, frame = capture.read()
    faces = face_classifier.detectMultiScale(frame)

    if not hasframe:
        break

    #draw rectangles around faces
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))

        #search eyes in detected faces
        eyes = eyes_classifier.detectMultiScale(frame)

        for eyes_x, eyes_y, eyes_w, eyes_h in eyes:
            if eyes_x > x and eyes_x < x + w and eyes_y + eyes_h < y + h and eyes_y < h  + y:
                cv2.rectangle(frame, (eyes_x, eyes_y),
                    (eyes_x + eyes_w, eyes_y + eyes_h), (0, 255, 0))
    cv2.imshow("run", frame)

cv2.destroyAllWindows()
