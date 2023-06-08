#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import cv2, socket, numpy, pickle
import receiver

receiver = receiver.ImageReceiver(ip="localhost", port=9999)

while True:

    data = receiver.rec_disp_image()
    height = data.shape[0]
    width = data.shape[1]
    roi_width = 100
    roi_height = 100
    roi_top_end = int(height / 2 + roi_height / 2)
    roi_bottom_end = int(height / 2 - roi_height / 2)
    roi_right_end = int(width / 2 + roi_width / 2)
    roi_left_end = int(width / 2 - roi_width / 2)
    print("height: " + str(height) + " width: " + str(width))

    # Crosshair
    cv2.line(data, (718, 540), (722, 540), (0, 0, 255), 1)
    cv2.line(data, (720, 538), (720, 542), (0, 0, 255), 1)

    # Rectangular Region of Interest (ROI)
    cv2.line(data, (roi_left_end, roi_top_end), (roi_right_end, roi_top_end), (0, 0, 255), 1)
    cv2.line(data, (roi_left_end, roi_bottom_end), (roi_right_end, roi_bottom_end), (0, 0, 255), 1)
    cv2.line(data, (roi_left_end, roi_top_end), (roi_left_end, roi_bottom_end), (0, 0, 255), 1)
    cv2.line(data, (roi_right_end, roi_top_end), (roi_right_end, roi_bottom_end), (0, 0, 255), 1)
    cv2.imshow('server', data)  # to open image
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
