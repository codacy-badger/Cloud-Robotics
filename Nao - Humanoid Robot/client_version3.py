import socket
import sys
import os
from naoqi import ALProxy
import time
import almath
import math
import argparse
import base64
import cv2
import cv
from Crypto.Cipher import AES  
import numpy

robotIp = "127.0.0.1"
serverIp = "83.212.106.184"

global motion
keySizeInBits128 = 'diplwmatikh$%$!@' # Secret Passphrase  
motion = None
HAS_PYLAB = True
tts = audio = record = aup = None 


#===================================================================

def encrypt(message):

#Function encrypting messages

	# ENCRYPT: AES 128 bit, CBC 
	message = message +'end'  
	while (len(message) % 16 != 0):
		message = message +'w'  
        obj = AES.new(keySizeInBits128, AES.MODE_CBC, 'This is an IV456')  
	message = obj.encrypt(message)  
	# ENCRYPT done
	return message

#===================================================================

def audio():

#Function for audio player and for recording
	tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
	audio = ALProxy("ALAudioDevice", "127.0.0.1", 9559)
	record = ALProxy("ALAudioRecorder", "127.0.0.1", 9559)
	aup = ALProxy("ALAudioPlayer", "127.0.0.1", 9559)


	tts.setParameter("doubleVoice", 1)
	tts.setParameter("doubleVoiceLevel", 0)
	tts.setParameter("doubleVoiceTimeShift", 0.1)
	tts.setParameter("pitchShift", 1.1)
	tts.say("Do you need Help?")
	record.startMicrophonesRecording("/var/volatile/test.wav", 'wav', 16000, (0,0,1,0))
	time.sleep(3)
	record.stopMicrophonesRecording()
	tts.say("Recording is. over.")
	time.sleep(1)

#===================================================================

def camera():

#Function for capturing a photo

	# Create a proxy to ALPhotoCapture
	try:
	  photoCaptureProxy = ALProxy("ALPhotoCapture", "127.0.0.1", 9559)
	except Exception, e:
	  print "Error when creating ALPhotoCapture proxy:"
	  print str(e)
	  exit(1)	
	photoCaptureProxy.setResolution(2)
	photoCaptureProxy.setPictureFormat("jpg")
	photoCaptureProxy.takePictures(1, "/var/volatile/", "image")

#===================================================================

def object_front(robotIp):

#Function for checking objects in front

    # Subscribe to sonars, this will launch sonars (at hardware level) and start data acquisition.
    sonarProxy.subscribe("myApplication")
    # Get sonar left first echo (distance in meters to the first obstacle).
    Left = memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")
    # Same thing for right.
    Right = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
    #print Sonar Left and Right
    print( "Left : %.2f" %  (Left) )
    print( "Right : %.2f" %  (Right) )
    return Left, Right
#===================================================================
	
def object_hand():

#Function for checking objects left and right using hands

    motion.setStiffnesses("RArm", 1.0)
    motion.setStiffnesses("LArm", 1.0)
    # Example showing a single target angle for one joint
    # Interpolate the head yaw to 1.0 radian in 1.0 second
    names      = ["LShoulderRoll","RShoulderRoll"]
    angleLists = [76.0*almath.TO_RAD, -76.0*almath.TO_RAD]
    timeLists  = 1.0
    isAbsolute = True
    motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(0.5)
    useSensors  = True
    sensorAngles = motion.getAngles(names, useSensors)
    ar=float(str(sensorAngles[0]))
    de=float(str(sensorAngles[1]))
    print( "Left_Hand : %.2f" %  (ar) )
    print( "Right_Hand : %.2f" %  (de) )
    return ar, de


#===================================================================

def move_forward(robotIp):

#Function for moving forward

        # A small step forwards and anti-clockwise with the left foot
        legName  = ["LLeg"]
        X        = 0.5
        Y        = 0.0
        Theta    = 0.0
        footSteps = [[X, Y, Theta]]
        timeList = [0.3]
        clearExisting = False
        motion.setFootSteps(legName, footSteps, timeList, clearExisting)
        time.sleep(1.0)
        # A small step forwards and anti-clockwise with the left foot
        legName  = ["RLeg"]
        X        = 0.5
        Y        = 0.0
        Theta    = 0.0
        footSteps = [[X, Y, Theta]]
        timeList = [0.3]
        clearExisting = False
        motion.setFootSteps(legName, footSteps, timeList, clearExisting)
        time.sleep(2.0)
        Left = memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")
    	Right = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")

#===================================================================

def for_left():

#Function for moving left

        	legName  = ["LLeg"]
		X        = 0.0
		Y        = 0.5
		Theta    = 0.0
		footSteps = [[X, Y, Theta]]
		timeList = [0.6]
		clearExisting = False
		motion.setFootSteps(legName, footSteps, timeList, clearExisting)
		time.sleep(1.0)
		# DEKSI PODI TWRA
		legName  = ["RLeg"]
		X        = 0.0
		Y        = 0.5
		Theta    = 0.0
		footSteps = [[X, Y, Theta]]
		timeList = [0.6]
		clearExisting = False
		motion.setFootSteps(legName, footSteps, timeList, clearExisting)
#===================================================================

def for_right():

#Function for moving right

    		# PAEI ARISTERA BRHKE EMPODIO MPROSTA DEKSIA
		#ARISTERO PODI PRWTA
	    	legName  = ["RLeg"]
		X        = 0.0
		Y        = -0.5
		Theta    = 0.0
		footSteps = [[X, Y, Theta]]
		timeList = [0.6]
		clearExisting = False
		motion.setFootSteps(legName, footSteps, timeList, clearExisting)
		time.sleep(1.0)
		# DEKSI PODI TWRA
		legName  = ["LLeg"]
		X        = 0.0
		Y        = -0.5
		Theta    = 0.0
		footSteps = [[X, Y, Theta]]
		timeList = [0.6]
		clearExisting = False
		motion.setFootSteps(legName, footSteps, timeList, clearExisting)

#===================================================================

def left():

#Function turning left

	X = 0
	Y = 0
	Theta = math.pi/2.0                 #math.pi/2.0 90 #math.pi/3 60 #math.pi/4 45
	Frequency=0
	motion.post.moveTo(X, Y, Theta)
	# wait that the move process start running
	time.sleep(0.1)
	footSteps1 = motion.getFootSteps()
	# Second call of move API
	motion.post.moveTo(X, Y, Theta)
	# get the second foot steps vector
	footSteps2 = motion.getFootSteps()
	# here we wait until the move process is over
	motion.waitUntilMoveIsFinished()
	# then we get the final robot position

#===================================================================

def right():


#Function turning right

	X = 0
	Y = 0
	Theta = -math.pi/2.0                 #math.pi/2.0 90 #math.pi/3 60 #math.pi/4 45
	Frequency=0
	motion.post.moveTo(X, Y, Theta)
	# wait that the move process start running
	time.sleep(0.1)
	footSteps1 = motion.getFootSteps()
	# Second call of move API
	motion.post.moveTo(X, Y, Theta)
	# get the second foot steps vector
	footSteps2 = motion.getFootSteps()
	# here we wait until the move process is over
	motion.waitUntilMoveIsFinished()
	# then we get the final robot position

#===================================================================

def back():

#Function moving 180 degrees

	X = 0
	Y = 0
	Theta = -math.pi                #math.pi/2.0 90 #math.pi/3 60 #math.pi/4 45
	Frequency=0
	motion.post.moveTo(X, Y, Theta)
	# wait that the move process start running
	time.sleep(0.1)
	footSteps1 = motion.getFootSteps()
	# Second call of move API
	motion.post.moveTo(X, Y, Theta)
	# get the second foot steps vector
	footSteps2 = motion.getFootSteps()
	# here we wait until the move process is over
	motion.waitUntilMoveIsFinished()
	# then we get the final robot position

#===================================================================









#===================================================================
try:
        motion = ALProxy("ALMotion", "127.0.0.1", 9559)
except Exception, a:
        print "Could not create proxy to ALMotion"
        print "Error was: ", a
#===================================================================
try:
        postureProxy = ALProxy("ALRobotPosture", "127.0.0.1", 9559)
except Exception, b:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", b
#===================================================================
try:
        sonarProxy = ALProxy("ALSonar", "127.0.0.1", 9559)
except Exception, c:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", c
#===================================================================
try:
        memoryProxy = ALProxy("ALMemory", "127.0.0.1", 9559)
except Exception, d:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", d
#===================================================================




if len(sys.argv) <= 1:
	print "Usage python alrobotposture.py robotIP"
else:
	robotIp = sys.argv[1]

messages = [ '']
server_address = (serverIp, 10000)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM)]










# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
for s in socks:
    s.connect((serverIp, 10000))
    print("----------------------------")


for message in messages:

    # Send messages on both sockets
    for s in socks:
	s.send(encrypt("Ready"))


    prohgoumeno=0
    # Read responses on both sockets
    for s in socks:
	while True:
        	data = s.recv(1024)
		if(data!=prohgoumeno):

			# DECRYPT: AES 128 bit, CBC    
			obj2 = AES.new(keySizeInBits128, AES.MODE_CBC, 'This is an IV456')  
			data = obj2.decrypt(data) 
			data = data.split('end')[0]  
			# DECRYPT done    
	


		        if(data == 'Begin'):
				Left, Right = object_front(robotIp)
				Left=str(Left)
				Right=str(Right)
				message = 'object_f'+'plus'+Left+'plus'+Right
	            	        s.send(encrypt(message))

		        if(data == 'Forward'):
				move_forward(robotIp)
				time.sleep(0.2)
 				postureProxy.goToPosture("Stand", 1.0)
				Left, Right = object_front(robotIp)
				Left=str(Left)
				Right=str(Right)
				message = 'object_f'+'plus'+Left+'plus'+Right
	            	        s.send(encrypt(message))
				
			if(data == 'Camera'):	
				camera()
	            	        s.send(encrypt("camera"))
				image = "/var/volatile/image.jpg"
				bytes = open(image).read()
				time.sleep(1)
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect(('83.212.106.184', 10001))
				client.send((encrypt(bytes)))				
				client.close()

			if(data == 'Voice'):				
				audio()
	            	        s.send(encrypt("voice"))
				voice = '/var/volatile/test.wav'
				time.sleep(1)
				bytes = open(voice).read()
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect(('83.212.106.184', 10001))
				client.send((encrypt(bytes)))				
				client.close()
				break

			if(data == 'NoFace'):	
				ar, de = object_hand()
				ar=str(ar)
				de=str(de)
				message = 'object_hand'+'plus'+ar+'plus'+de
	            	        s.send(encrypt(message))

			if(data == 'forward_left'):
				for_left()
				s.send(encrypt("Ready"))


			if(data == 'forward_right'):
				for_right()
				s.send(encrypt("Ready"))

			if(data == 'left'):
				left()
				s.send(encrypt("Ready"))

			if(data == 'right'):
				right()
				s.send(encrypt("Ready"))

			if(data == 'back'):
				back()
				s.send(encrypt("Ready"))

			if(data == 'Stop'):	
				break

			data = prohgoumeno
	print >>sys.stderr, 'closing socket', s.getsockname()
	s.close()
	print("----------------------------")









