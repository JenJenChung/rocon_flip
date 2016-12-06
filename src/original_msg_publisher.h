#include <ros/ros.h>
#include <ros/console.h>
#include <string>
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
    
    std::string gate_name ;
    
    void handshakeCallback(const std_msgs::String&) ;
} ;

Vostro::Vostro(ros::NodeHandle nh){
  subHandshake = nh.subscribe("/receiver/handshake", 10, &Vostro::handshakeCallback, this) ;
  pubHelloString = nh.advertise<std_msgs::String>("original_message", 10, true) ;
  pubAckHandshake = nh.advertise<std_msgs::Bool>("msg_ack", 10, true) ;
  
  std_msgs::String s ;
  ros::param::get("gateway/name",gate_name) ;
  s.data = "Hello from " + gate_name + "!" ;
  pubHelloString.publish(s) ;
}

void Vostro::handshakeCallback(const std_msgs::String& msg){
  ROS_INFO("Handshake received from remote gateway!") ;
  ROS_INFO_STREAM("Message reads: " << msg.data ) ;
  
  std_msgs::Bool b ;
  b.data = true ;
  pubAckHandshake.publish(b) ;
}
