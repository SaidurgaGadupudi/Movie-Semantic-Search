# import the library
import os
import cv2
import matplotlib.pyplot as plt


# Movie source
source = r"C:\Users\91949\Downloads\The.Lake.House.2006.mp4"

# returns the videocapture object 
cap = cv2.VideoCapture(source)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

if (cap.isOpened()== False): 
    print("Error opening video stream or file")

# Frames directory
directory = r"C:\Users\91949\Desktop\frames"
os.chdir(directory)

frame_count=0



while cap.isOpened():
    # changing directory every time as it reads from source folder
    os.chdir(directory)
    # retrive frame 
    ret, frame = cap.read()
    if ret==False:
            break
    #writing to file
    cv2.imwrite('Frame'+str(frame_count)+'.png',frame)
            
    frame_count+=1
    
print("done")   
# once finished release object 
cap.release()
cv2.destroyAllWindows()