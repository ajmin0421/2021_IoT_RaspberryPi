import picamera
import time

path = '/home/pi/src3/06_multimedia'
now_str = time.strftime("%Y%m%d_%H%M%S")
camera = picamera.PiCamera()
while(True):
    cmd = input("photo : 1,video : 2,exit:9 > ")
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    if cmd == '1':
        now_str = time.strftime("%Y%m%d_%H%M%S")
        camera.capture('%s/%s.jpg' % (path,now_str))
        print('사진 촬영')
    elif cmd == '2':    
        print('동영상 촬영')
        now_str = time.strftime("%Y%m%d_%H%M%S")
        camera.start_recording('%s/%s.h264' % (path,now_str))
        input('press enter to start to stop recording')
        camera.stop_recording()
    elif cmd == '9':
        camera.stop_preview()
        break
