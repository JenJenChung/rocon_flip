#include "ros/ros.h"
#include "original_msg_publisher.h"

int main(int argc, char **argv)
{  
  ros::init(argc, argv, "original_msg_publisher") ;
  
  ros::NodeHandle nHandle ;
  
  Vostro v(nHandle) ;
  
  ros::spin() ;
  return 0 ;
}
