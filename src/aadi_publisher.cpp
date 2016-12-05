#include "ros/ros.h"
#include "aadi_publisher.h"

int main(int argc, char **argv)
{  
  ros::init(argc, argv, "aadi_publisher") ;
  
  ros::NodeHandle nHandle ;
  
  AADI a(nHandle) ;
  
  ros::spin() ;
  return 0 ;
}
