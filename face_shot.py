import cv2
import os
import setting_up

name = setting_up.create_directory()

cam = cv2.VideoCapture(0)

cv2.namedWindow("Press Space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press Space to take a photo", 500, 300)

img_counter = 1

while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break
		cv2.imshow("Press Space to take a photo", frame)
		
		wait_key = cv2.waitKey(1)
		if wait_key%256 == 27:
			# ESC is pressed
			print("Escape hit, closing...")
			break
		elif wait_key%256 == 32:
			# Space is pressed
			img_name = "dataset/" + name +"/image_{}.jpg".format(img_counter)
			cv2.imwrite(img_name, frame)
			print("{} written!".format(img_name))
			img_counter += 1
			
cam.release()

cv2.destroyAllWindows()
