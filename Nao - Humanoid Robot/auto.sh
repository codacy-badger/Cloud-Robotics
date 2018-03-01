
#!/bin/sh





auto=0
valid=1
while [ 1 -eq 1 ]
do
action=$(< value.txt)


if [ ! -z "$action" ] ; then

case $action in
	0)
		sleep 1

	;;
	1)
		curl -X POST -F "uploaded_file=@image.txt" -F "submit=1" http://83.212.106.184//image_upload/upload.php

		#reset status
		python reset.py
	;;
	2)
		curl -X POST -F "uploaded_file=@voice.txt" -F "submit=1" http://83.212.106.184//image_upload/upload.php

		#reset status
		python reset.py
	;;






esac
fi

done
