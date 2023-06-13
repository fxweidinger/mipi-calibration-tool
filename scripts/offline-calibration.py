#  Copyright (c) Felix Weidinger (fxweidinger) 2023
import glob

import cv2

from calibration import Calibration

glob_img = glob.glob(
    '../art-image-data/asymmetric-circles-opencv-testdata/acircles8.png')
calib = Calibration(1, 1, 1, 1, (3, 9), None)
print(calib.symmetry)
calib.init_params_circular_pattern((8, 255), (50.0, 30000.0), 0.1, 0.87, 0.01)

for frame in glob_img:
    mat = cv2.imread(frame)
    ret, img = calib.find_circles(mat)
    print(ret)
    cv2.imshow("img", img)  # display
    key = cv2.waitKey(0)
cv2.destroyAllWindows()
exit(0)
