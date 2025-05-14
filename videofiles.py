import cv2

cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('webcam_output.mp4', cv2.VideoWriter_fourcc(*'mp4v'),
                      20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret: break
    out.write(frame)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
out.release()
cv2.destroyAllWindows()
