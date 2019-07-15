import cv2
import numpy as np
 
video = cv2.VideoCapture(0)
 
while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break
 
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hls = cv2.cvtColor(blur, cv2.COLOR_BGR2HLS)
 
    lower = [14, 114, 220]
    upper = [18, 137, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hls, lower, upper)
    
    output = cv2.bitwise_and(frame, hls, mask=mask)
    no_red = cv2.countNonZero(mask)
    cv2.imshow("output", output)
    if int(no_red) > 20:
        print ('Fire detected')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cv2.destroyAllWindows()
video.release()
