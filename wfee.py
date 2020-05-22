import cv2 as cv
import imutils
from imutils.video import VideoStream
print(cv.__file__)
face_cascade = cv.CascadeClassifier('C:\\Users\\riyas\\PycharmProjects\\smile\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\\Users\\riyas\\PycharmProjects\\smile\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('C:\\Users\\riyas\\PycharmProjects\\smile\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_smile.xml')
#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))

cap1 = 0
while 1:
 # reads frames from a camera
 ret, img = cap.read()

 if ret:
  # if video is still left continue creating images

  # convert to gray scale of each frames
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  # Detects faces of different sizes in the input image
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x, y, w, h) in faces:
   # To draw a rectangle in a face
   cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
   roi_gray = gray[y:y + h, x:x + w]
   roi_color = img[y:y + h, x:x + w]
   # Detects eyes of different sizes in the input image
   eyes = eye_cascade.detectMultiScale(roi_gray)
   # To draw a rectangle in eyes
   for (ex, ey, ew, eh) in eyes:
    cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
   # to detect smile
   smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
   for (sx, sy, sw, sh) in smiles:
    cap1 = cv.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

   # if video is still left continue creating images
    for cap1 in range(1,5):
     name = 'C:\\Users\\riyas\\Desktop' + str(cap1) + '.jpg'

   # writing the extracted images
     cv.imwrite(name, img)
     print('Creating...' + name)

   # increasing counter so that it will
   # show how many frames are created
     #cap1 += 1
    if not condition(item):
     cap1 = 0
     break

 else:
  break

   # Display an image in a window
 cv.imshow('video', img)


 # Wait for Esc key to stop
 if cv.waitKey(30) & 0xff == ord('a'):
  break


# Close the window
cap.release()

# De-allocate any associated memory usage
cv.destroyAllWindows()
