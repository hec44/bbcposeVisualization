'''
testing joints in bbcpose dataset with opencv

by: hec44

'''

import cv2
import csv
import os
import numpy as np

def test_csv(csvFile):

    with open(csvFile, 'rb') as csvfile:#load images joints and id from csv
        raw = csv.reader(csvfile)
        imagesIdAndJoints = np.squeeze(np.array([row for row in raw]))

    for j in range(0,800):#print joints in 800 images
        #first element is image id, so we load it
        print csvFile.split('.')[0]+"/"+imagesIdAndJoints[j][0]+".jpg"
        test_img=cv2.imread(csvFile.split('.')[0]+"/"+imagesIdAndJoints[j][0]+".jpg")
        try:
            for i in range(1,10):
                cv2.circle(test_img,(int(imagesIdAndJoints[j][i]),\
                int(imagesIdAndJoints[j][i+9])), 3, (0,0,255), -1)
            cv2.imshow("image",test_img)
            cv2.waitKey(0)
        except:#some times the image is not in the dataset
            print ("ERROR LOADING: ",csvFile.split('.')[0]+"/"+imagesIdAndJoints[j][0]+".jpg")


if __name__ == '__main__':
    test_csv('1.csv')
