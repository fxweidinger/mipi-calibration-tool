#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import cv2
import numpy
import numpy as np
from typing import List


class Calibration:
    blob_detector: cv2.SimpleBlobDetector = None
    objp: np.ndarray = None
    object_points: List[np.ndarray] = []
    img_points: List[np.ndarray] = []
    symmetry: int = None

    def __init__(self, focal_length_x: float, focal_length_y: float,
                 optical_center_x: float, optical_center_y: float,
                 pattern_size: tuple[int, int],
                 termination_criteria: List[float] = None):

        # Intrinsic Parameters
        self.optical_centerX = optical_center_x
        self.focal_lengthY = focal_length_y
        self.focal_lengthX = focal_length_x
        self.optical_centerY = optical_center_y

        # Pattern Configuration
        self.pattern_size = pattern_size
        if pattern_size[0] == pattern_size[1]:
            self.symmetry = cv2.CALIB_CB_SYMMETRIC_GRID
        else:
            self.symmetry = cv2.CALIB_CB_ASYMMETRIC_GRID

        # Termination Criteria Defaults
        if termination_criteria is None:
            self.termination_criteria = (
                cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        else:
            self.termination_criteria = termination_criteria

        self.objp = np.zeros((self.pattern_size[0] * self.pattern_size[1], 3),
                             np.float32)
        self.objp[:, :2] = np.mgrid[0:self.pattern_size[0],
                           0:self.pattern_size[1]].T.reshape(-1, 2)

    def set_grid(self):
        self.objp = np.zeros((self.pattern_size[0] * self.pattern_size[1], 3),
                             np.float32)
        self.objp[:, :2] = np.mgrid[0:self.pattern_size[0],
                           0:self.pattern_size[1]].T.reshape(-1, 2)

    def init_params_circular_pattern(self, threshold: tuple[int, int],
                                     area: tuple[float, float] = None,
                                     min_circle: float = None,
                                     min_convex: float = None,
                                     min_inertia: float = None):
        print("--- Setting parameters for circle pattern calibration ---")
        blob_params = cv2.SimpleBlobDetector_Params()
        blob_params.minThreshold = threshold[0]
        blob_params.maxThreshold = threshold[1]

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

    def find_circles(self, frame: numpy.ndarray) -> tuple[bool, np.ndarray]:

        refined_frame: np.ndarray
        # blobs = self.blob_detector.detect(frame)

        # blobs_overlaid = cv2.drawKeypoints(frame, blobs, np.array([]),
        #                                   (0, 255, 0),
        #                                   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, circles = cv2.findCirclesGrid(frame, (
            self.pattern_size[0], self.pattern_size[1]),
                                           flags=self.symmetry,
                                           blobDetector=self.blob_detector,
                                           parameters=None)
        if ret:
            self.object_points.append(self.objp)
            circles2 = cv2.cornerSubPix(cvt, circles, (1, 1),
                                        (-1, -1), self.termination_criteria)
            self.img_points.append(circles2)
            refined_frame = cv2.drawChessboardCorners(frame, (
                self.pattern_size[0], self.pattern_size[1]), circles2,
                                                      ret)
            return True, refined_frame
        return False, None

    def init_params_checkerboard_pattern(self):
        # TODO
        print("--- Setting parameters for checkerboard calibration ---")

    def save_calibration_yaml(self):
        print("--- Saving calibration YAML file ---")
        # TODO
