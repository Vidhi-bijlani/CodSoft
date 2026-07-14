import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame = cap.read()
if ret:
    cv2.imshow("Camera Test", frame)
    print("Camera working. Press ESC to close")
    cv2.waitKey(0)
else:
    print("Camera FAILED to open")
cap.release()
cv2.destroyAllWindows()