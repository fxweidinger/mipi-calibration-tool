#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import pickle
import socket
import cv2
import numpy as np


class ImageReceiver:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock.bind((self.ip, self.port))

    def rec_disp_image(self) -> np.ndarray:
        x = self.sock.recvfrom(1000000)
        client_ip = x[1][0]
        image_data = x[0]
        image_data = pickle.loads(image_data)
        image_data = cv2.imdecode(image_data, cv2.IMREAD_GRAYSCALE)
        return image_data
