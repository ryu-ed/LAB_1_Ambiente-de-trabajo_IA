#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Int32
def callback(data):
	rospy.loginfo(rospy.get_caller_id() + " Recibo %d" , data.data)
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", Int32, callback)
	rospy.spin()
if __name__ == '__main__':
	listener()

