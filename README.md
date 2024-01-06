# Camera_calibration
Camera Calibration using OpenCV
This repository contains Python code for camera calibration using OpenCV. Camera calibration is a crucial step in computer vision applications, allowing you to correct distortions caused by the camera lens.

### Instructions
Follow the steps below to use the camera calibration code:

### Clone the Repository:
git clone https://github.com/Skanda-sap/Camera_calibration.git

### Set Up Calibration Target:
Feel free to use the Checkerboard target from the calibration_target folder provided in the repository.
Place your calibration target images in a separate folder.

### Update Code:
Open the calibration.py file.
Update the CheckerBoard dimensions and square_size according to your calibration target.
Modify the images variable to point to the folder containing your calibration target images.

### Run the Code:
Execute the code using the following command:
python3 calibration.py

Follow on-screen instructions to refine the calibration.

### Review Results:
After the calibration process, the camera matrix, distortion coefficients, and other calibration parameters will be displayed.
The mean reprojection error will be calculated and printed.

### Note:
Ensure that the checkerboard target images used for calibration are high-quality and cover different orientations to obtain accurate calibration results.
