import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "/Users/meetjethwa21/PycharmProjects/Meet-FaceRecognizer/dataset/"
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesWithID(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #create empth face list
    faces=[]
    #create empty ID list
    IDs=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:


            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(faceNp)
            print(ID)
            IDs.append(ID)
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)

    return IDs, faces


Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.write('recognizer/trainningData.yml')
cv2.destroyAllWindows()
