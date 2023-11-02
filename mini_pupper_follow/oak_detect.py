#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from vision_msgs.msg import Detection2DArray
import math

class OakDetect(Node):

    def __init__(self):
        super().__init__('oak_detect')

        self.height = 300
        self.width = 300
        self.roll=0
        self.pitch=0
        self.yaw=0
        self.yaw_increment=0
        self.pitch_increment=0
        self.pose = Pose()

        self.publisher_ = self.create_publisher(Pose, '/body_pose', 10)
        
        self.subscription = self.create_subscription(Detection2DArray, '/color/mobilenet_detections', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning 未使用変数の警告を防ぐ

        #mobilenet object list
        #0: background
        #1: aeroplane
        #2: bicycle
        #3: bird
        #4: boat
        #5: bottle
        #6: bus
        #7: car
        #8: cat
        #9: chair
        #10: cow
        #11: diningtable
        #12: dog
        #13: horse
        #14: motorbike
        #15: person
        #16: pottedplant
        #17: sheep
        #18: sofa
        #19: train
        #20: tvmonitor

    def toward_obj(self, obj_class, obj_list):
        self.yaw_increment = 0
        self.pitch_increment = 0
        
        for i in obj_list:
            bb = i.bbox         # BoundingBoxes2D
            #si = i.source_img  # SourceImage
            r = i.results       # Results
            #rr = r[0] #RealResults
            #print(rr.class_id)
            #print(i.id)
            if(i.id == obj_class):
                print(11111)
                self.yaw_increment = (self.width/2 - bb.center.position.x)*0.0002
                self.pitch_increment = -(self.height/2 - bb.center.position.y)*0.0002
            
            #else:
                #yaw_increment=0
        
        self.yaw = self.yaw + self.yaw_increment
        #print(self.yaw_increment)
        self.pitch = self.pitch + self.pitch_increment
        cy=math.cos(self.yaw*0.5)
        sy=math.sin(self.yaw*0.5)
        cp=math.cos(self.pitch*0.5)
        sp=math.sin(self.pitch*0.5)
        cr=math.cos(self.roll*0.5)
        sr=math.sin(self.roll*0.5)

        self.pose.orientation.w = cy * cp * cr + sy * sp * sr
        self.pose.orientation.x = cy * cp * sr - sy * sp * cr
        self.pose.orientation.y = sy * cp * sr + cy * sp * cr
        self.pose.orientation.z = sy * cp * cr - cy * sp * sr

        self.publisher_.publish(self.pose)
        
    def listener_callback(self, data):
        bounding_boxes = data                   # Detection2DArray
        detections = bounding_boxes.detections  # Detection2D[]
        self.toward_obj('5', detections)        # #5: bottle
        #toward_obj('cup',a)
        #print(a[0])

def main(args=None):
    rclpy.init(args=args)
    oak_detect = OakDetect()
    rclpy.spin(oak_detect)
    oak_detect.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
