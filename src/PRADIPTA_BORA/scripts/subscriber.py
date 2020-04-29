#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int64

name = ""
number = 0
def callback_name(data):
	global name
	name = data.data
def callback_number(data):
	global number
	number = data.data
	rospy.loginfo("If you want to call {0}, then call on this {1}".format(name, number))
def listener():
	rospy.init_node("listener")

	rospy.Subscriber("name_listener", String, callback_name)
	rospy.Subscriber("num_listener", Int64, callback_number)
	rospy.spin()

if __name__ == '__main__':
	listener()
