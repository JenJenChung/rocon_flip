#include <ros/ros.h>
#include <ros/console.h>
#include "std_msgs/String.h"
#include "std_msgs/Bool.h"

class Vostro{
  public:
    Vostro(ros::NodeHandle) ;
    ~Vostro(){}
  private:
    ros::Subscriber subHandshake ;
    ros::Publisher pubHelloString ;
    ros::Publisher pubAckHandshake ;
    
    void handshakeCallback(const std_msgs::String&) ;
} ;

Vostro::Vostro(ros::NodeHandle nh){
  subHandshake = nh.subscribe("/aadi1/handshake", 10, &Vostro::handshakeCallback, this) ;
  pubHelloString = nh.advertise<std_msgs::String>("vostro_message", 10, true) ;
  pubAckHandshake = nh.advertise<std_msgs::Bool>("vostro_ack", 10, true) ;
  
  std_msgs::String s ;
  s.data = "Hello from Vostro!" ;
  pubHelloString.publish(s) ;
}

void Vostro::handshakeCallback(const std_msgs::String& msg){
  ROS_INFO("Handshake received from remote gateway!") ;
  ROS_INFO_STREAM("Message reads: " << msg.data ) ;
  
  std_msgs::Bool b ;
  b.data = true ;
  pubAckHandshake.publish(b) ;
}
