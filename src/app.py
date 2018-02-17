import time

time.sleep(10)
from flask import Flask, render_template, Response, request
from camera import Camera
import carControl



app = Flask(__name__)


@app.route('/')
def mainPage():
	return render_template('index.html')

def gen(camera):
#"""Video streaming generator function."""
	while True:
        	frame = camera.get_frame()
       		yield (b'--frame\r\n'
               	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_freed')
def video_freed():
    	return Response(gen(Camera.Camera()),
            	        mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control_car', methods=['POST'])
def control_car_ajax():
    	direction = request.form['direction']
	position = request.form['position']
	if direction == 'fwd':
		if position == 'down':
			carControl.motor(1)
		if position == 'up':
			carControl.motor(0)
	elif direction == 'bwd':
		if position == 'down':
			carControl.motor(-1)
		if position == 'up':
			carControl.motor(0)
	elif direction == 'right':
		if position == 'down':
			carControl.steering(1)
		if position == 'up':
			carControl.steering(0)
	elif direction == 'left':
		if position == 'down':
			carControl.steering(-1)
		if position == 'up':
			carControl.steering(0)

	return 'ok'

@app.route('/lights', methods=['POST'])
def lights_ajax():
	carControl.lights(request.form['lights'])
	return 'ok'


if __name__ == '__main__':
    	app.run(debug=True, host='0.0.0.0', threaded=True)
