#  Copyright (c) Felix Weidinger (fxweidinger) 2023
import glob

import cv2

from calibration import Calibration

glob_img = glob.glob(
    '../art-image-data/symmetric-circles-opencv-testdata/*.png')
calib = Calibration(1, 1, 1, 1, [7, 7], None)
calib.init_params_circular_pattern([8, 255], [50.0, 2500.0], 0.1, 0.87,
                                   0.01)


for frame in glob_img:
    mat = cv2.imread(frame)
    ret, img = calib.find_circles(mat)
    print(ret)
    cv2.imshow("img", img)  # display
    key = cv2.waitKey(0)
cv2.destroyAllWindows()
exit(0)

