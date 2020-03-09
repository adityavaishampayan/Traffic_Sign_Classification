![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Traffic-sign-recognition

## Table of contents
* [Overview](#Overview)
* [Dataset](#Dataset)
* [Output Video](#Output Video)
* [Libraries used](#Libraries used)


## Overview

Traffic Sign Recognition can be staged into two sections: Traffic Sign Detection and Traffic Sign Classification. In the Detection stage we aim to extract possible candidates (or regions) which contain a traffic sign (in this part, we do not care what the sign might be). In the Classification stage, we go over each Region of Interest (RoI) extracted previously and try to identify a traffic sign (which might not be in that RoI at all). The dataset.

The repository contains following files and folders:

- traffic_sign_recognition.pdf - Project report with detials.
- Final_TSR_detect.py - python code for running the traffic sign recognition algorithm
- dataset.pkl - pickle file containing the trained model using SVM
- templates - consists of different signs as templates, to be used for classification.

## Dataset
For the dataset, images from a driving car, training and testing images for a set of signs can be found [here](https://drive.google.com/drive/u/0/folders/0B8DbLKogb5ktTW5UeWd1ZUxibDA).


## Output Video

The google drive link for sample output video is provided here:

[Video](https://drive.google.com/open?id=1EfDC4rpTF3HhwQKok_FVIE2kgiWOaShD)

## Dependencies used
Project is created with:
* OpenCV - (OpenCV uses a BSD license and hence can be used for production with modification to the code.)
* Numpy
* Scikit Learn
* Pickle
* Skimage


# Algorithm Process and Output Results

Introduction In this project of Traﬃc Sign Recognition, the whole project can be divided into two phases. First phase involved the detection of the sign, (this phase does not focus on what the sign is). The next phase of Classiﬁcation involved determining the sign that was been detected. For the detection phase, we ﬁrst denoise the image, followed by contrast stretching and normalizing the intensity. After this we applied the MSER algorithm for feature detection. Once these features were identiﬁed, a bounding box is ﬁtted to the detected Region of Interest for the data preparation of the next phase of Classiﬁcation. In Classiﬁcation, ﬁrst the SVM(Support Vector Machine) classiﬁer is trained using HOG feature extraction on the training set. Then the corresponding detected areas of interest are classiﬁed using the trained SVM classiﬁer.

## Detection Phase

1. The initial step involved denoising of the raw images. With this, averaging any nuances such as textures are removed for proper sign detection.
2. After this, we performed contrast stretching on each channel i.e. on B,G and R channel. In contrast stretching higher and lower values of the pixel intensities are distributed between 0 and 255. The formula below is used for contrast stretching, where a = 0, b = 255 and c and d are the minimum and maximum intensities in the frame.
3. Normalization of these intensities was our next step. The above two steps distribute the pixel intensities and normalize it for signiﬁcant improvement in easier detection of the blue and red color. For the Blue and red channel.
4. The next step involved the extraction of MSER features from the image. We constructed separate MSER functions for detecting the red and blue signs and their respective parameters were tuned accordingly.
5. The last step of detection phase was ﬁtting a bounding box to the MSER features that were detected. The bounding box was also ﬁne tuned as there were multiple boxes being formed.
6. The tuning was done by grouping diﬀerent contours by their centroids. The centroids near each other are grouped together, say lies in a circle of radius 100 are grouped together. Groups with less than 4 contours are ignored as they are not important.
7. After grouping, the bounding box with maximum area is taken from each group. At this point we further increased the size of the bounding box, so that the image which was cropped out for classiﬁcation gave us better results.

## Classification

1. Classiﬁcation for blue and red coloured signals were done separately (just like the MSER features were applied and tuned individually due to their diﬀerent intensities), i.e., they were trained and tested separately so that there are no kind of false identiﬁcation because generally red coloured signs call for immediate action unlike the blue coloured ones.
2. Training folders are segregated based on the signs we need to perform the training. For training the SVM model for red coloured signals the training set was of 5 folders 1, 14, 17, 19 and 21.
3. Similarly, for the blue coloured signs 35, 38 and 45 were the folders. The training set consisted of the image and the corresponding label of the signal.
4. After this each image from each folders were resized to 16x16 and converted to grayscale and hog features were extracted.
5. After performing the training on the SVM model, for testing purpose the images from the test dataset were taken and checked using predict function.
6. After performing the evaluation over all the required test dataset we achieved an accuracy of 91.5%.
7. After this we need to apply the test part of the code to the main program where we give the detected sign as the test image and the predict function provides a label for each image and the corresponding sign is displayed beside the detected region.


## Output Results

|![](images/traffic_signs.png)|
|:--:|
| *Traffic signs to detect* |

|![](images/bicycle.png)|
|:--:|
| *Bicycle* |

|![](images/bump_ahead_1.png)|
|:--:|
| *Bump sign* |

|![](images/bump_and_bicycle.png)|
|:--:|
| *Bump and Bicycle* |

|![](images/keep_right_1.png)|
|:--:|
| *Keep Right* |

|![](images/narrow_road.png)|
|:--:|
| *Narrow Road* |

|![](images/parking_sign_2.png)|
|:--:|
| *Parking Sign* |

|![](images/road_on_right.png)|
|:--:|
| *Road on right* |

|![](images/yield_1.png)|
|:--:|
| *Yield sign* |

|![](images/X_road_1.png)|
|:--:|
| *Cross road* |

## License
```
MIT License

Copyright (c) 2018 Aditya Vaishampayan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Virtual Environment

### Installing a Virtual Environment
The virtualenv package is required to create virtual environments. You can install it with pip:
```
pip install virtualenv
```

### Create the virtual environment
To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following:
```
virtualenv mypython
```

### Activate the virtual environment
You can activate the python environment by running the following command:

Mac OS / Linux
```
source mypython/bin/activate
```

You should see the name of your virtual environment in brackets on your terminal line e.g. (mypython).

Any python commands you use will now work with your virtual environment

### Deactivate the virtual environment
To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’.
```
deactivate
```

## OpenCV installation
Update packages
```
sudo apt-get update
sudo apt-get upgrade
```
We will install required dependencies
```
sudo apt-get install build-essential checkinstall cmake pkg-config yasm
sudo apt-get install git gfortran
sudo apt-get install libjpeg8-dev libjasper-dev libpng12-dev
 ```
If you are using Ubuntu 14.04
```
sudo apt-get install libtiff4-dev
```
If you are using Ubuntu 16.04
```
sudo apt-get install libtiff5-dev
```

```
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo apt-get install libxine2-dev libv4l-dev
sudo apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install qt5-default libgtk2.0-dev libtbb-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev
sudo apt-get install libvorbis-dev libxvidcore-dev
sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install x264 v4l-utils
 ```
Optional dependencies
```
sudo apt-get install libprotobuf-dev protobuf-compiler
sudo apt-get install libgoogle-glog-dev libgflags-dev
sudo apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen
```
Clone OpenCV and OpenCV_contrib
```
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout 3.3.1
cd ..

git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout 3.3.1
cd ..
```
Make build directory
```
cd opencv
mkdir build
cd build
```
Run Cmake
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D WITH_TBB=ON \
      -D WITH_V4L=ON \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..
```
Find out number of CPU cores in your machine
```
nproc

# substitute 4 by output of nproc
make -j4
sudo make install
sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```
For installation related issues.

A complete OpenCV installation guide in Ubuntu can be found [here](http://www.codebind.com/cpp-tutorial/install-opencv-ubuntu-cpp/).
