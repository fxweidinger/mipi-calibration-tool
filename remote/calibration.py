#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import cv2
import numpy


class Calibration:
    object_points = []
    img_points = []

    def __init__(self, focal_length_x, focal_length_y, optical_center_x, optical_center_y, pattern_size, criteria):
        self.pattern_size = pattern_size
        self.optical_centerX = optical_center_x
        self.focal_lengthY = focal_length_y
        self.focal_lengthX = focal_length_x
        self.optical_centerY = optical_center_y
        self.criteria = criteria
        self.objworldp = numpy.zeros((1, self.pattern_size[0] * self.pattern_size[1], 3), numpy.float32)
        self.objworldp[0, :, :2] = numpy.mgrid[0:self.pattern_size[0], 0:self.pattern_size[1]].T.reshape(-1, 2)

        print("--- Calibration init ---")

    def find_circles(self, frame: cv2.Mat):
        object_points_temp = []cd
        img_points_temp = []
        ret, centers = cv2.findCirclesGrid(frame, self.pattern_size, cv2.CALIB_CB_SYMMETRIC_GRID, None, None)
        if ret:
            object_points_temp.append(self.objworldp)
            centers2 =


    def save_calibration_xml(self):
        print("TODO")
