#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import pickle
import socket
import cv2

'''
Allows sending images over the network. Currently is hardcoded to UDP.
'''
class ImageTransmitter:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send_image(self, image, quality):
        ret, buffer = cv2.imencode(".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        d_bytes = pickle.dumps(buffer)
        self.sock.sendto(d_bytes, (self.ip, self.port))

    def close(self):
        self.sock.close()

