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

add_executable(vostro_publisher src/vostro_publisher.cpp)
target_link_libraries(vostro_publisher ${catkin_LIBRARIES})
add_dependencies(vostro_publisher ${catkin_EXPORTED_TARGETS})

add_executable(aadi_publisher src/aadi_publisher.cpp)
target_link_libraries(aadi_publisher ${catkin_LIBRARIES})
add_dependencies(aadi_publisher ${catkin_EXPORTED_TARGETS})
