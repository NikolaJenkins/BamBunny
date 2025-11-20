import cv2
import numpy as np
import apriltag
import argparse
from pupil_apriltags import Detector

def apriltag_init():
    image_path = 'test.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    options = apriltag.DetectorOptions(families = '36h11')
    # detector = apriltag.Detector(options)
    detector = Detector(
        families = "36h11",
        nthreads=1,
        quad_decimate=1.0,
        quad_sigma=0.0,
        refine_edges=1,
        decode_sharpening=0.25,
        debug=0
    )

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
	help="path to input image containing AprilTag")
    args = vars(ap.parse_args())

def apriltag_periodic():

    # load the input image and convert it to grayscale
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    results = detector.detect(
        img = gray, 
        estimate_tag_pose = True, 
        camera_params = (269.72, 269.04, 175.09, 110.03),
        tag_size = 0.1651 # meters
        )

    if results:
        for r in results:
            (ptA, ptB, ptC, ptD) = r.corners
            ptA = (int(ptA[0]), int(ptA[1]))
            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            
            # draw the bounding box of the AprilTag detection
            cv2.line(image, ptA, ptB, (0, 255, 0), 2)
            cv2.line(image, ptB, ptC, (0, 255, 0), 2)
            cv2.line(image, ptC, ptD, (0, 255, 0), 2)
            cv2.line(image, ptD, ptA, (0, 255, 0), 2)
a
            center_x = r.center[0]
            tx = results.camera_params[2] - center_x
    
    # show the output image after AprilTag detection
    cv2.imshow("Image", image)
    cv2.waitKey(0)