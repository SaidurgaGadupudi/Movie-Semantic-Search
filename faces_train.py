#pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

people = ['amitabh', 'Nani', 'NTR']
#  in another way
# p=[]
# for i in os.listdir(r'C:\Users\91949\Desktop\opencv\faces')
# p.append()
DIR = r'C:\Users\91949\Desktop\opencv\faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:      #loop over every folder in base folder
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):       #loop over every img in a particular folder
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)  #face detection using haar cascade

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]  #region of interest(cropping out the face)
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()   #instantiating the face recognizer

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)