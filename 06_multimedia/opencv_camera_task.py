import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('Camera open failed')
    exit()


#사진찍기
#ret, frame = cam.read()
#cv2.imshow('frame',frame)
#cv2.imwrite('output.jpg',frame)




#동영상 촬영하기
while True:
    ret,frame = cam.read()
    edge1 = cv2.Canny(frame, 100, 150)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    cv2.imshow('edge1',edge1)
    cv2.imshow('gray',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) ==13:
        break


cam.release()
cv2.destoryALLWindows()