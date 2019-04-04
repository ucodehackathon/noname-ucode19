import cv2
import time
import os

video = cv2.VideoCapture(0)

nframes = 0

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

while True:
    nframes += 1
    check, frame = video.read()
    print(check)
    print(frame)
    cv2.imshow("Capturing",frame)
    name = './data/input' + str(nframes) + '.jpg'
    cv2.imwrite(name, frame)
    time.sleep(0.20)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(nframes)
video.release()
cv2.destroyallwindows