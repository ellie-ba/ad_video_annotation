import cv2
import numpy as np
from skimage import util

in_video = '/home/elaheh/projects/ad_video_annotation/Uploads from Nike/1.19.12.mp4'
in_cap = cv2.VideoCapture(in_video)

rf = 1

w = in_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = in_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(int(w * rf), int(h * rf))
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('playing-soccer.mp4', fourcc, 15.0, (int(h), int(w)))


iii = 0
while in_cap.isOpened():
    iii += 1
    ret, frame = in_cap.read()

    if ret is None or frame is None:
        break

    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

in_cap.release()
out.release()
cv2.destroyAllWindows()
