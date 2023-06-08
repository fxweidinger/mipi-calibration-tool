#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import cv2
from pynput import keyboard
import event_handler
import transmitter

cap = cv2.VideoCapture(cv2.CAP_V4L2)
transmitter = transmitter.ImageTransmitter("localhost", 9999)
image_cnt = 0
trigger = False


def on_press(key):
    global image_cnt
    global trigger
    if key == keyboard.KeyCode.from_char("c"):
        print(' --- CAPTURE --- ')
        """
        1. Take image, find circles and display found circles overlaid on image
        2. Wait for keypress: okay or discard
        3. if circles are found correctly increase counter 
        """
        trigger = True
    if key == keyboard.KeyCode.from_char("x"):
        print("--- ABORT ---")
        cap.release()


event_handler = event_handler.EventHandler(listener=keyboard.Listener(on_press=on_press))

print(
    "\nAdjust the camera so calibration pattern is in focus. After taking an image of the calibration pattern,"
    "move the pattern. \n\n" +
    "Press C to trigger a calibration image acquisition\n" +
    "Press X to terminate. \n"
)
'''
Main Loop:
Waits for keypress to take a frame and perform calibration.
The calibration requires 10 images cx
'''

while True:
    ret, frame = cap.read()
    if image_cnt == 10:
        break
    if not ret:
        print("--- Error: Can't grab frames or aborted---")
        break
    while trigger:
        transmitter.send_image(frame, 60)
        image_cnt += 1
        trigger = False
    cv2.waitKey()
    transmitter.send_image(frame, 60)

event_handler.stop()
transmitter.close()
if image_cnt == 10:
    print("--- SUCCESSFULLY PERFORMED IMAGE ACQUISITION FOR CALIBRATION ---")
    cap.release()
else:
    print("--- CALIBRATION FAILED: NOT ENOUGH IMAGE DATA ---")
    exit(1)
