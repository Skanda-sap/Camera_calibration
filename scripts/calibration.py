import cv2
import numpy as np
import os
import glob

# Defining the dimensions of the checkerboard
CheckerBoard = (7, 9)
# Size of each square in millimeters
square_size = 20.0

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Creating vector to store vectors of 3D points for each checkerboard image
objpoints = []
# Creating vector to store vectors of 2D points for each checkerboard image
imgpoints = []

# Defining the world coordinates for 3D points
objp = np.zeros((1, CheckerBoard[0] * CheckerBoard[1], 3), np.float32)
objp[0, :, :2] = square_size * np.mgrid[0:CheckerBoard[0], 0:CheckerBoard[1]].T.reshape(-1, 2)

prev_img_shape = None

# Initialize h and w
h, w = 0, 0

# Extracting path of individual image stored in a given directory
images = glob.glob('/home/images/*.jpg')

# Print the list of images for verification
print("List of images:")
print(images)

# Create a resizable window
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

# Loop through each image in the directory
for fname in images:
    # Read the image
    img = cv2.imread(fname)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find the checkerboard corners
    # If desired number of corners are found in the image, ret = true
    ret, corners = cv2.findChessboardCorners(gray, CheckerBoard, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    
    """
    If desired number of corners are detected, 
    refine the pixel coordinates and display them 
    on the images of the checkerboard
    """
    if ret == True:
        objpoints.append(objp)
        # Refining pixel coordinates for given 2D points
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CheckerBoard, corners2, ret)

    cv2.imshow('img', img)
    cv2.resizeWindow('img', 800, 600)  # Adjust window size as needed
    cv2.waitKey(0)
    h, w = img.shape[:2]

cv2.destroyAllWindows()

# Print the number of images used for calibration
print("Number of images used for calibration:", len(objpoints))

# Performing camera calibration
if len(objpoints) > 0:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (w, h), None, None)

    print("Camera matrix : \n")
    print(mtx)
    print("dist : \n")
    print(dist)
    print("rvecs : \n")
    print(rvecs)
    print("tvecs : \n")
    print(tvecs)
else:
    print("No images were successfully used for calibration.")

# Calculate reprojection error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error

print("Reprojection Error(mm): {}".format(mean_error / len(objpoints)))
