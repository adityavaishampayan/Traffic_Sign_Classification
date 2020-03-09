Traffic_Sign_Detection
1 Introduction In this project of Traﬃc Sign Recognition, the whole project can be divided into two phases. First phase involved the detection of the sign, (this phase does not focus on what the sign is). The next phase of Classiﬁcation involved determining the sign that was been detected. For the detection phase, we ﬁrst denoise the image, followed by contrast stretching and normalizing the intensity. After this we applied the MSER algorithm for feature detection. Once these features were identiﬁed, a bounding box is ﬁtted to the detected Region of Interest for the data preparation of the next phase of Classiﬁcation. In Classiﬁcation, ﬁrst the SVM(Support Vector Machine) classiﬁer is trained using HOG feature extraction on the training set. Then the corresponding detected areas of interest are classiﬁed using the trained SVM classiﬁer.

2 Detection Phase

The initial step involved denoising of the raw images. With this, averaging any nuances such as textures are removed for proper sign detection.
After this, we performed contrast stretching on each channel i.e. on B,G and R channel. In contrast stretching higher and lower values of the pixel intensities are distributed between 0 and 255. The formula below is used for contrast stretching, where a = 0, b = 255 and c and d are the minimum and maximum intensities in the frame.
Normalization of these intensities was our next step. The above two steps distribute the pixel intensities and normalize it for signiﬁcant improvement in easier detection of the blue and red color. For the Blue and red channel.
The next step involved the extraction of MSER features from the image. We constructed separate MSER functions for detecting the red and blue signs and their respective parameters were tuned accordingly.
The last step of detection phase was ﬁtting a bounding box to the MSER features that were detected. The bounding box was also ﬁne tuned as there were multiple boxes being formed.
The tuning was done by grouping diﬀerent contours by their centroids. The centroids near each other are grouped together, say lies in a circle of radius 100 are grouped together. Groups with less than 4 contours are ignored as they are not important.
After grouping, the bounding box with maximum area is taken from each group. At this point we further increased the size of the bounding box, so that the image which was cropped out for classiﬁcation gave us better results.
3 Classiﬁcation Phase

Classiﬁcation for blue and red coloured signals were done separately (just like the MSER features were applied and tuned individually due to their diﬀerent intensities), i.e., they were trained and tested separately so that there are no kind of false identiﬁcation because generally red coloured signs call for immediate action unlike the blue coloured ones.
Training folders are segregated based on the signs we need to perform the training. For training the SVM model for red coloured signals the training set was of 5 folders 1, 14, 17, 19 and 21.
Similarly, for the blue coloured signs 35, 38 and 45 were the folders. The training set consisted of the image and the corresponding label of the signal.
After this each image from each folders were resized to 16x16 and converted to grayscale and hog features were extracted.
After performing the training on the SVM model, for testing purpose the images from the test dataset were taken and checked using predict function.
After performing the evaluation over all the required test dataset we achieved an accuracy of 91.5%.
After this we need to apply the test part of the code to the main program where we give the detected sign as the test image and the predict function provides a label for each image and the corresponding sign is displayed beside the detected region.

# Traffic_Sign_Classification

https://drive.google.com/drive/folders/1-_XyClUV0M-7JpPbvQdg9uK8wjH2GXM4?usp=sharing
