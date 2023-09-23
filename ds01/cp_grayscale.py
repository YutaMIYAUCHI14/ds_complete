import time
import numpy as np
import cv2

jellyfish = "jellyfish_-_110877 (540p).mp4"

cap = cv2.VideoCapture(jellyfish)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fmt = cv2.VideoWriter_fourcc("m","p","4","v")
writer = cv2.VideoWriter("jellyfish_gray.mp4", fmt, fps, (width, height), 0)

print("We Are Calculating ..........")
start = time.time()
while True:
    ret, frame = cap.read()

    if ret == False:
        break

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("Please Wait ... ")


    cv2.imshow("Bird Relaxing Gray Scale", frameGray)
    writer.write(frameGray)

process_time = time.time() - start
print("Finished !!!")
print("Process Time : " + str(process_time))

cap.release()
writer.release()
cv2.destroyAllWindows()