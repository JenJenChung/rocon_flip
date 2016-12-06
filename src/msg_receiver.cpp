#include "ros/ros.h"
#include "msg_receiver.h"

int main(int argc, char **argv)
{  
  ros::init(argc, argv, "msg_receiver") ;
  
  ros::NodeHandle nHandle ;
  
  AADI a(nHandle) ;
  
  ros::spin() ;
  return 0 ;
}
