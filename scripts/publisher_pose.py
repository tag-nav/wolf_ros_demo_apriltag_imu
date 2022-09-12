#!/usr/bin/env python


"""
Publisher a constant pose
"""

import rospy
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Image

INPUT_TOPIC = '/camera/infra1/image_rect_raw'
POSE_TOPIC = '/pose_altitude'
RATE = 100  # Hz
POSE = [0,0, 0.2, 0,0,0,1]

pub = rospy.Publisher(POSE_TOPIC, PoseStamped, queue_size=10)
msg_pose = PoseStamped()

msg_pose.pose.position.x = POSE[0]
msg_pose.pose.position.y = POSE[1]
msg_pose.pose.position.z = POSE[2]
msg_pose.pose.orientation.x = POSE[3]
msg_pose.pose.orientation.y = POSE[4]
msg_pose.pose.orientation.z = POSE[5]
msg_pose.pose.orientation.w = POSE[6]


def callback(msg_in: Image):
    msg_pose.header.stamp = msg_in.header.stamp
    pub.publish(msg_pose)


def main():
    rospy.Subscriber(INPUT_TOPIC, Image, callback)
    rospy.init_node('pose_publisher', anonymous=True)
    rospy.spin()
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass