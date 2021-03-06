#include <ros/ros.h>
#include <ros/console.h>
#include <string>
#include "std_msgs/String.h"

class Receiver{
  public:
    Receiver(ros::NodeHandle) ;
    ~Receiver(){}
  private:
    ros::Subscriber subHelloString ;
    ros::Subscriber subHelloStringNoNamespace ;
    ros::Publisher pubHandshake ;

    std::string gate_name ;
    
    void stringCallback(const std_msgs::String&) ;
} ;

Receiver::Receiver(ros::NodeHandle nh){
  subHelloString = nh.subscribe("/sender/original_message", 10, &Receiver::stringCallback, this) ;
  subHelloStringNoNamespace = nh.subscribe("/original_message", 10, &Receiver::stringCallback, this) ;
  pubHandshake = nh.advertise<std_msgs::String>("handshake", 10, true) ;
  
  ros::param::get("/gateway/name",gate_name) ;
}

void Receiver::stringCallback(const std_msgs::String& msg){
  ROS_INFO("Message received from sender!") ;
  ROS_INFO_STREAM("Message reads: " << msg.data ) ;
  
  std_msgs::String s ;
  s.data = "Hello from " + gate_name + "!" ;
  pubHandshake.publish(s) ;
}
