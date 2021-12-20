

import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('Camera open failed')
    exit()

#fourcc
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))
#fps(초당 프레임수)


#동영상 촬영하기
while True:
    ret,frame = cam.read()
    if not ret:
        break
    
    cv2.imshow('frame',frame)
    out.write(frame)

    if cv2.waitKey(10) ==27:
        break


cam.release()
out.release()
cv2.destoryALLWindows()