import numpy as np
import cv2
import os
from skimage import io

def splite_video():
    cap = cv2.VideoCapture('Uploads from Nike/2011 Doernbecher Design - Dacia Kasenga.mp4')

    counter = 10000
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        path = ''.join(["splited_videos/", str(counter), ".jpg"])
        cv2.imwrite(path, frame)

        counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

def generate_video(dirname):
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    new_w, new_h = 1280, 720
    out = cv2.VideoWriter('playing-soccer.mp4', fourcc, 15.0, (new_w, new_h))

    path, dirs, files = os.walk(dirname).next()

    frame = cv2.imread(''.join([path, "/", files[1]]), 0)
    # print(img)
    # frame = (img * 255.0).astype
    # io.imshow(frame)
    # io.show()
    # cv2.imshow('frame', frame)
    for i in range(100):
        frame = cv2.resize(frame, (new_w, new_h))
        out.write(frame)
        print(frame.shape)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()

    #out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))

if __name__ == '__main__':
    generate_video("splited_videos/1")
    #splite_video()