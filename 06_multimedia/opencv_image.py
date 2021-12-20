import cv2

#image 파일 읽기
img = cv2.imread('BTS.jpg')
img2 = cv2.resize(img,(1980, 840))


#Edge선 추출하기
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('BTS', img)
cv2.imshow('1', edge1)
cv2.imshow('2', edge2)
cv2.imshow('3', edge3)

#키보드 입력을 기다림 *ms"
#기본값 0, 0인 경우 키보드 입력이 있을 떄까지 계속 기다림
cv2.waitKey(0)

#열려있는 모든 창 닫기
cv2.destroyAllWindows()