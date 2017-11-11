import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter()
succes = out.open('output.avi',fourcc, 15.0, (1280,720),True)
ii = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ii >100:
        break
    if ret==True:
        frame = cv2.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    ii += 1

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()