from cv2 import *
import os
import face_recognition
import sys

def get_cam(imagePath):
    # initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        #namedWindow("cam-test", WINDOW_AUTOSIZE)
        #imshow("cam-test", img)
        # waitKey(1000)
        # destroyWindow("cam-test")
        imwrite("My_image.jpg", img)

def myFace(imagefile):
    picture_of_me = face_recognition.load_image_file(imagefile)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    return(my_face_encoding)

def badPeople(myFace, path=os.getcwd()):
    # files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if 'bad.jpg' in file:

                # get face encodings for each face in the image:
                unknown_picture = face_recognition.load_image_file(file)
                unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

                results = face_recognition.compare_faces([myFace], unknown_face_encoding)

                if results[0] == True:
                    print(file)
    
                else:
                    print("It's not a picture of me!")


                
                # files.append(os.path.join(r, file))
    # return files



###############################################################################################################
#           TESTING GROUND
#
###############################################################################################################


def main():
    imagePath = sys.argv[0]
    get_cam(imagePath)
    micara = myFace("My_image.jpg")
    badPeople(micara)
    # compareFaces(myFace,allImages)




if __name__ == "__main__":
    main()