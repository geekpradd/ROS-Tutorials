#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64


def number_publisher():
	pub = rospy.Publisher("num_listener", Int64, queue_size=10)
	rospy.init_node('number_publisher')
	rate = rospy.Rate(5)
	while not rospy.is_shutdown():
		number = 8638224958
		rospy.loginfo(number)
		pub.publish(number)
		rate.sleep()

if __name__ == '__main__':
	try:
		number_publisher()
	except rospy.ROSInterruptException:
		pass

