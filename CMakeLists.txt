CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
project(wolf_demo_apriltag_imu)


find_package(catkin REQUIRED COMPONENTS)

catkin_package(
  CATKIN_DEPENDS rospy
)

# Declare a python script
catkin_install_python(PROGRAMS scripts/publisher_pose.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

