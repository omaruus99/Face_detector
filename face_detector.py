import cv2
 
face_cascade = cv2.CascadeClassifier('face_detector.xml')
img = cv2.imread('imaage.jpg') #img input
 
faces = face_cascade.detectMultiScale(img, 1.1, 4)
 
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("facedetector.png", img) #img output
 
print('Successfully saved')
