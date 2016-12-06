cmake_minimum_required(VERSION 2.8.3)
project(rocon_flip)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rocon_gateway
  rocon_hub
  roscpp
  rospy
  std_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(original_msg_publisher src/original_msg_publisher.cpp)
target_link_libraries(original_msg_publisher ${catkin_LIBRARIES})
add_dependencies(original_msg_publisher ${catkin_EXPORTED_TARGETS})

add_executable(msg_receiver src/msg_receiver.cpp)
target_link_libraries(msg_receiver ${catkin_LIBRARIES})
add_dependencies(msg_receiver ${catkin_EXPORTED_TARGETS})
