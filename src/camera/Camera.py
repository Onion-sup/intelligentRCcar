import cv2

import base_camera as base
import objectDetect
detection = False

class Camera(base.BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
		# read current frame
		_, img = camera.read()
		#############	 object detection	#############
		if (detection):
			img = objectDetect.object_detection(img)
		# encode as a jpeg image and return it
		yield cv2.imencode('.jpg', img)[1].tostring()

