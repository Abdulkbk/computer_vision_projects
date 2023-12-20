#!/usr/bin/env python3

import os
import cv2
import numpy as np
import argparse
from datetime import datetime

# Default input image and output path
in_path = "resources/blue.jpg"
output_path = "resources/output"

parser = argparse.ArgumentParser(description="Color Tracking Script")
parser.add_argument(
    "-i",
    "--img",
    dest="in_path",
    type=str,
    default=in_path,
    help="Path to the input image (default: resources/blue.jpg)",
)
parser.add_argument(
    "-o",
    "--out",
    dest="output_path",
    type=str,
    default=output_path,
    help="Path to the output folder to save image (default: resources/output/)",
)
args = parser.parse_args()

in_path = args.in_path
output_path = args.output_path

""" Validate cutom input image and output folder"""
if not os.path.exists(in_path):
    in_path = "resources/blue.jpg"

if not os.path.isdir(output_path):
    output_path = "resources/output"


def updater(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", "TrackBars", 0, 179, updater)
cv2.createTrackbar("Hue max", "TrackBars", 179, 179, updater)
cv2.createTrackbar("Sat min", "TrackBars", 0, 255, updater)
cv2.createTrackbar("Sat max", "TrackBars", 255, 255, updater)
cv2.createTrackbar("Value min", "TrackBars", 0, 255, updater)
cv2.createTrackbar("Value max", "TrackBars", 255, 255, updater)

while True:
    img = cv2.imread(in_path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHSV, lower, upper)

    img_result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Image", img_result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        cv2.imwrite(f"{output_path}/{datetime.now()}.jpg", img_result)
        print("Image saved!")

    if key == ord("q"):
        break
cv2.destroyAllWindows()
