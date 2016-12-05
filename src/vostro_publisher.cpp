#include "ros/ros.h"
#include "vostro_publisher.h"

int main(int argc, char **argv)
{  
  ros::init(argc, argv, "vostro_publisher") ;
  
  ros::NodeHandle nHandle ;
  
  Vostro v(nHandle) ;
  
  ros::spin() ;
  return 0 ;
}
