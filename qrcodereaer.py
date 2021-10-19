import cv2
img=cv2.imread("3.png")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)