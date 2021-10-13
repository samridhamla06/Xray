# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:33:29 2021

@author: samridhamla
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:01:23 2021

@author: samridhamla
"""
from imageai.Detection import VideoObjectDetection
import os
import pafy
import cv2

global_dict = {}

def getFPS(camera):
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
        # With webcam get(CV_CAP_PROP_FPS) does not work.
        # Let's see for ourselves.
    
    if int(major_ver)  < 3 :
        fps = camera.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using camera.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = camera.get(cv2.CAP_PROP_FPS)
        print("Frames per second using camera.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
        
def forSecond(second_number, output_arrays, count_arrays, average_output_count):
    print("Second : ", second_number)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    print("------------END OF A SECOND --------------")
    
    if len(average_output_count) > 0 :        
        global_dict[second_number] = list(average_output_count.keys())
    
def processVideo(url):
    global global_dict 
    global_dict = {}
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    current_directory = os.getcwd()
    
    print(current_directory)
    detector = VideoObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    fileName = "LiveTraffic"
    input_path = os.path.join(current_directory, fileName + ".mp4")
    output_path = os.path.join(current_directory , fileName + "_output12.mp4")
    
    
    detector.setModelPath(os.path.join(current_directory , "yolo-tiny.h5"))
    detector.loadModel()
    
    
    #url = "https://www.youtube.com/watch?v=vDHtypVwbHQ"
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    
    print(best.url)
    
    camera = cv2.VideoCapture(best.url)
    fps = getFPS(camera)
    
    video_path = detector.detectObjectsFromVideo(camera_input=camera,
        output_file_path=output_path
        , frames_per_second=30, log_progress=True, minimum_percentage_probability=30, frame_detection_interval = 300
        , per_second_function=forSecond)
    
    return global_dict
    
    # =============================================================================
    # detections = detector.detectObjectsFromImage(
    # input_image = input_path, 
    # output_image_path = output_path
    # )
    # 
    # 
    # for eachObject in detections:
    #     print(
    #          eachObject["name"] , " : ",
    #          eachObject["percentage_probability"], " : ",
    #          eachObject["box_points"] )
    #     print("--------------------------------")
    # =============================================================================
    
    # =============================================================================
    # custom = detector.CustomObjects(person = True)
    # 
    # detections = detector.detectCustomObjectsFromVideo(
    #       custom_objects = custom, 
    #       input_file_path=input_path,
    #       output_file_path=output_path,
    #       frames_per_second=20, log_progress=True,frame_detection_interval = 50,
    #       minimum_percentage_probability = 50)
    # =============================================================================
    
#dict = processVideo("https://www.youtube.com/watch?v=vDHtypVwbHQ")
#print(str(dict))