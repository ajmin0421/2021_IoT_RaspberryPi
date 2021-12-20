import cv2

#xml 분류기 파일 로그
face_cascade = cv2.CascadeClassifier(
    './xml/face.xml')
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
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   #이미지에서 얼굴 검출
    faces = face_cascade.detectMultiScale(gray)

    #얼굴 위치에 대한 좌표 정보 가져오기
    for(x ,y ,w ,h) in faces:
        #원본 이미지에 얼굴 위치 표시
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0), 2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) ==13:
        break

cam.release()
cv2.destoryALLWindows()


