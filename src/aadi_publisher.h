#include <ros/ros.h>
#include <ros/console.h>
#include "std_msgs/String.h"

class AADI{
  public:
    AADI(ros::NodeHandle) ;
    ~AADI(){}
  private:
    ros::Subscriber subHelloString ;
    ros::Publisher pubHandshake ;
    
    void stringCallback(const std_msgs::String&) ;
} ;

AADI::AADI(ros::NodeHandle nh){
  subHelloString = nh.subscribe("/vostro/vostro_message", 10, &AADI::stringCallback, this) ;
  pubHandshake = nh.advertise<std_msgs::String>("handshake", 10, true) ;
}

void AADI::stringCallback(const std_msgs::String& msg){
  ROS_INFO("Message received from vostro gateway!") ;
  ROS_INFO_STREAM("Message reads: " << msg.data ) ;
  
  std_msgs::String s ;
  s.data = "Hello from AADI1!" ;
  pubHandshake.publish(s) ;
}
