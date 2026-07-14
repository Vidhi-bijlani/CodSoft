import cv2

cap = cv2.VideoCapture(0) # 0 = default webcam

if not cap.isOpened():
    print("Error: Webcam not found")
    exit()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret: break

    # Draw text
    cv2.putText(frame, "OpenCV 5.0.0 Working", (10,30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.imshow("Face Detection Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()