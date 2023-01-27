import cv2

image = cv2.imread(filename="C:\\Users\\sk939\\Downloads\\e-mp3.jpg", flags=1)
cv2.imshow("python3.11.1",image)
cv2.waitKey(0)
cv2.destroyAllWindows()