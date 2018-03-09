import select
import socket
import sys
import argparse
import Queue
from Crypto.Cipher import AES  
import base64
import cv2
import numpy as np
import speech_recognition as sr




keySizeInBits128 = 'diplwmatikh$%$!@' # Secret Passphrase  
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

def text(file):

#Function reading start.txt

	file = open('public_html/start.txt', 'r')
	file=file.read()
	return file

#===================================================================

def convert(image):

#Function saving string to image.jpg

    string=image
    t = open("example.jpg", "w+")
    t.write(string)
    t.close()

#===================================================================

def convert1(voice):

#Function saving string to image.jpg

    string=voice
    t = open("voice.wav", "w+")
    t.write(string)
    t.close()

#===================================================================












# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", 
        default="example.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
# Bind the socket to the port
server_address = ('83.212.106.184', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)
# Listen for incoming connections
server.listen(5)
# Sockets from which we expect to read
inputs = [ server ]
# Sockets to which we expect to write
outputs = [ ]
# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:

    # Wait for at least one of the sockets to be ready for processing
    #print >>sys.stderr, '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)


    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data

		# DECRYPT: AES 128 bit, CBC    
		obj2 = AES.new(keySizeInBits128, AES.MODE_CBC, 'This is an IV456')  
		data = obj2.decrypt(data)
		data = data.split('end')[0]  
		# DECRYPT done

#===================================================================				
		if data == 'Ready':
		    file=text(file)
		    while (file != '1'):
			file=text(file)	
	            s.send(encrypt("Begin"))
		if data != 'Ready':
			t = open("/home/user/public_html/person.txt", "w+")
    			t.write('0')
    			t.close()
			part1 = data.split('plus')[0]
#===================================================================				
			if (part1=='object_f'):
				Left = data.split('plus')[1]
				Right = data.split('plus')[2]
				Left=float(Left)
				Right=float(Right)
   				if ((Left) > 0.4) and (( Right) > 0.4):
					print("Going Forward")
					s.send(encrypt("Forward"))
				else:
					print("Use Camera")
					s.send(encrypt("Camera"))
#===================================================================	
			if (part1=='camera'):
				file = open('public_html/image_upload/uploads/image.txt', 'r')
				data=file.read()

				# DECRYPT: AES 128 bit, CBC    
				obj2 = AES.new(keySizeInBits128, AES.MODE_CBC, 'This is an IV456')  
				data = obj2.decrypt(data)
				data = data.split('end')[0]  
				# DECRYPT done
				img=data
				convert(img)
				print("Processing Image")
				face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
				eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')				
				# load the input image and convert it to grayscale
				image = cv2.imread(args["image"])
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)				
				# load the  Haar cascade, then detect faces
				# in the input image
				faces = face_cascade.detectMultiScale(gray, 1.3, 5)
				cat_detected = False
				for (i,(x,y,w,h)) in enumerate(faces):
				    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
				    roi_gray = gray[y:y+h, x:x+w]
				    roi_color = image[y:y+h, x:x+w]
				    eyes = eye_cascade.detectMultiScale(roi_gray)
				    for (ex,ey,ew,eh) in eyes:
				        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
				        cv2.putText(image, "Person #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
					cat_detected = True
				print  'Face',cat_detected
				if cat_detected == False:
				        detector = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
				        rects = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))
				        person_detected = False
				        # loop over the cat faces and draw a rectangle surrounding each
				        for (i, (x, y, w, h)) in enumerate(rects):
				                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
				                cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
				                person_detected = True
				        # show the detected cat faces
				        print 'Cat',person_detected 
				if (cat_detected == True) or (person_detected == True):
					s.send(encrypt("Voice"))
				if (cat_detected != True) and  (person_detected != True):
					s.send(encrypt("NoFace"))
#===================================================================				
			if (part1=='object_hand'):
				ar = data.split('plus')[1]
				de = data.split('plus')[2]
				ar=float(ar)
				de=float(de)
				if ar > 1.18 and de < -1.18:
				   	if (Left - Right) > 0.2:
				        	# PAEI ARISTERA BRHKE EMPODIO MPROSTA DEKSIA
						s.send(encrypt("forward_left"))
					elif (Left - Right) < -0.2:
				    		# PAEI ARISTERA BRHKE EMPODIO MPROSTA DEKSIA
						s.send(encrypt("forward_right"))
					else:
						s.send(encrypt("right"))
    				elif ar > 1.18 and de > -1.18:
					s.send(encrypt("left"))
    				elif ar < 1.18 and de < -1.18:
					s.send(encrypt("right"))
    				else:
					s.send(encrypt("back"))
#===================================================================				
			if (part1=='voice'):
				file = open('public_html/image_upload/uploads/voice.txt', 'r')
				data=file.read()
				# DECRYPT: AES 128 bit, CBC    
				obj2 = AES.new(keySizeInBits128, AES.MODE_CBC, 'This is an IV456')  
				data = obj2.decrypt(data)
				data = data.split('end')[0]  
				# DECRYPT done
				voice=data
				convert1(voice)

				r = sr.Recognizer()
				with sr.WavFile("voice.wav") as source:              # use "test.wav" as the audio source
    					audio = r.record(source)                     # extract audio data from the file
				try:
    					print( r.recognize_google(audio))   # recognize speech using Google Speech Recognition
					if "yes" in  r.recognize_google(audio):
						t = open("/home/user/public_html/person.txt", "w+")
    						t.write('1')
    						t.close()
					else:
						t = open("/home/user/public_html/person.txt", "w+")
    						t.write('2')
    						t.close()
						 
				except LookupError:                                 # speech is unintelligible
   					print("Could not understand audio")
				break
#===================================================================	
                        file=text(file)
			if file == '0':
	            	    s.send(encrypt("Stop"))
			if data == '1.Done':
	            	    s.send(encrypt("goto2"))
#===================================================================				





                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queues[s]



