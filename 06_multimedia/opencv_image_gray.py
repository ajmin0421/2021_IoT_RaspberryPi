import cv2

#image 파일 읽기
img = cv2.imread('BTS.jpg')


#색상 변환하기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#이미지 파일 읽기
cv2.imshow('BTS', img)
cv2.imshow('BTS_GRAY', gray)

#키보드 입력을 기다림 *ms"
#기본값 0, 0인 경우 키보드 입력이 있을 떄까지 계속 기다림
while True:
    if cv2.waitKey() == 13:
        break

#파일로 저장하기
cv2.imwrite('BTS_GRAY.jpg',gray)

#열려있는 모든 창 닫기
cv2.destroyAllWindows()