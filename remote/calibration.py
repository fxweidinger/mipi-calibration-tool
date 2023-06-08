#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import cv2
import numpy as np


class Calibration:
    blob_detector = None
    objp = None
    object_points = []
    img_points = []
    termination_criteria_circle = None
    termination_criteria_checkerboard = None
    circle_distance = None

    def __init__(self, focal_length_x, focal_length_y, optical_center_x, optical_center_y, pattern_size):
        self.pattern_size = pattern_size
        self.optical_centerX = optical_center_x
        self.focal_lengthY = focal_length_y
        self.focal_lengthX = focal_length_x
        self.optical_centerY = optical_center_y

    def set_grid(self):
        self.objp = np.zeros((self.pattern_size[0] * self.pattern_size[1], 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:self.pattern_size[0], 0:self.pattern_size[1]].T.reshape(-1, 2)

    def init_calib_circular_pattern(self, circle_distance, termination_criteria, threshold, area=None, min_circle=None,
                                    min_convex=None, min_inertia=None):
        print("--- Circle Pattern Calibration ---")
        self.termination_criteria_circle = termination_criteria
        self.circle_distance = circle_distance
        blob_params = cv2.SimpleBlobDetector_Params()
        blob_params.minThreshold(threshold[0])
        blob_params.maxThreshold(threshold[1])

        if area:
            blob_params.filterByArea = True
            blob_params.minArea = area[0]
            blob_params.maxArea = area[1]

        if min_circle:
            blob_params.filterByCircularity = True
            blob_params.minCircularity = min_circle

        if min_convex:
            blob_params.filterByConvexity = True
            blob_params.minConvexity = min_convex

        if min_inertia:
            blob_params.filterByInertia = True
            blob_params.minInertiaRatio = min_inertia

        self.blob_detector = cv2.SimpleBlobDetector_create(blob_params)

    def calib_checkerboard_pattern(self):
        print("-- Checkerboard Pattern Calibration ---")

    def save_calibration_xml(self):
        print("TODO")
