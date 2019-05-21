#!/usr/bin/env python
import rospy
import time
import threading
import roslib; roslib.load_manifest('ur_driver')
from control_msgs.msg import *
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import JointState
import math
from ur3_throwing.srv import ur3_throw
from std_srvs.srv import Empty

"""
	This python script is responsible for:
		- movement for throwing given the joint velocity input

	There will be 1 service running which handles both the function mentioned above.
"""

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
              'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

global position_list
position_list = [];

def callback(data):
	# creating a queue for the joint states
	lock.acquire()
	position_list.append(data.position)

	if len(position_list) > 20:
		position_list.pop(0)
	lock.release()

#trajectory = JointTrajectory()
def ur3_throwing_server():
	#create node
	rospy.init_node('ur3_throwing')
	global lock
	lock = threading.Lock()

	global joint_speed_pub

    # create publisher to publish to the ur_driver/joint_speed
	joint_speed_pub = rospy.Publisher('ur_driver/joint_speed',JointTrajectory, queue_size=60)

	# subscriber
	rospy.Subscriber("/joint_states",JointState, callback)

	# create a service
	s = rospy.Service('ur3_throw',Empty,ThrowTrajectory)

	rospy.spin()

def ThrowTrajectory(req):

	test_move_with_stop()
	list = []
	return list


def test_move_with_stop():

	rate = rospy.Rate(135)
	trajectory = JointTrajectory()

	trajectory.header.stamp=rospy.Time.now()
	trajectory.joint_names = JOINT_NAMES

	wrist_speed = -1
	elbow_speed = -2.5
	traj = True
	wrist_moving = False
	count = 0

	lock.acquire()
	elbow = position_list[len(position_list)-1][2]
	elbow = math.degrees(elbow)
	lock.release()

	while True:
		# gets joint angle
		if count is 4:
			lock.acquire()
			elbow = position_list[len(position_list)-1][2]
			elbow = math.degrees(elbow)
			lock.release()
			count = 0

		# for giving the boost needed when reaching the top
		if elbow < 70 and wrist_moving == False:
			wrist_speed = -5.5
			wrist_moving = True

		# for making sure the arm stops after a certain joint angle
		if elbow > 25:
			trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, elbow_speed, wrist_speed, 0, 0], accelerations=[0, 0, 1.8, 2.5, 0, 0])]
		else:
			# for elbow_speed
			if elbow_speed < -0.08:
				elbow_speed += 0.04
			else:
				elbow_speed = 0
				traj = False

			if wrist_speed < -0.2:
				wrist_speed += 0.15
			else:
				wrist_speed = 0

			trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, elbow_speed, wrist_speed, 0, 0])]

		# for debugging
		#rospy.loginfo("elbow_speed :" + str(elbow_speed) + "   wrist_speed :" + str(wrist_speed) + "   joint angle :" + str(elbow))
		joint_speed_pub.publish(trajectory)

		if traj == False:
			break

		count += 1
		rate.sleep()

	trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, 0, 0, 0, 0])]
	joint_speed_pub.publish(trajectory)

if __name__ == '__main__': ur3_throwing_server()
