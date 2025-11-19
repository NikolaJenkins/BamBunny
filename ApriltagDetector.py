import cv2
import numpy as np
import apriltag
import argparse

camera_params = (320, 240, 160, 120) # fx, fy, cx, cy
tag_size = 0.1 # meters

def apriltag_init():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
	help="path to input image containing AprilTag")
    args = vars(ap.parse_args())

    # load the input image and convert it to grayscale
    print("[INFO] loading image...")
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # define the AprilTags detector options and then detect the AprilTags
    # in the input image
    print("[INFO] detecting AprilTags...")
    options = apriltag.DetectorOptions(families="tag36h11")
    detector = apriltag.Detector(options)
    results = detector.detect(gray)
    print("[INFO] {} total AprilTags detected".format(len(results)))

def apriltag_periodic():
    for r in results:
        # extract the bounding box (x, y)-coordinates for the AprilTag
        # and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = r.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))
        # draw the bounding box of the AprilTag detection
        cv2.line(image, ptA, ptB, (0, 255, 0), 2)
        cv2.line(image, ptB, ptC, (0, 255, 0), 2)
        cv2.line(image, ptC, ptD, (0, 255, 0), 2)
        cv2.line(image, ptD, ptA, (0, 255, 0), 2)

        # estimate pose of apriltag
        pose, euler, center = detector.detect_tags_and_return_pose(
            image,
            camera_params,
            tag_size
        )
        pitch_angle = euler[1]


# show the output image after AprilTag detection
cv2.imshow("Image", image)
cv2.waitKey(0)

image_path = 'test.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
options = apriltag.DetectorOptions(families = '36h11')
detector = apriltag.Detector(options)
results = detector.detect(gray)


detections = detector.detect(image)