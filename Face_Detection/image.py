import cv2 
#Trained Dataset
train_dataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read a Image
#img=cv2.imread('img1.png')
img=cv2.imread('mul.jpg')
scaled_image = cv2.resize(img, None, fx=0.5, fy=0.5)
#convert in to grayscale
gray=cv2.cvtColor(scaled_image,cv2.COLOR_BGR2GRAY)
faces=train_dataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(scaled_image,(x,y),(x+w,y+h),(255,0,0),2)
    #cv2.rectangle(img,(x-axis,y-axis),(for create box),(255,0,0 for give color for box),2 for thickness)
cv2.imshow('COLOR',scaled_image)
cv2.imshow('GRAY',gray)

cv2.waitKey()
