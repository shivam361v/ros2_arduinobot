import rclpy # Import the rclpy library -> allows us to use the ROS2 Python client library
from rclpy.node import Node # Import the Node class -> allows us to create a node
from std_msgs.msg import String # Import the String message type -> allows us to publish a string

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.pub_ = self.create_publisher(String, "chatter", 10) # Create a publisher with the topic name "chatter" and the message type String
        self.counter_ = 0 # Create a counter variable
        self.frequency_ = 1.0 # Create a frequency variable
        self.get_logger().info("Publishing at %d Hz" % self.frequency_) # Print a message to the console
        self.timer_ = self.create_timer(self.frequency_, self.timer_callback) # Create a timer that calls the timer_callback function at a frequency of 1 Hz

    def timer_callback(self):
        msg = String() # Create a String message
        msg.data = "Hello World: %d" % self.counter_ # Set the message data to "Hello World: <counter>"
        self.pub_.publish(msg) # Publish the message
        self.counter_ += 1


def main():
    rclpy.init() # Initialize the ROS client library
    simple_publisher = SimplePublisher() # Create an instance of the SimplePublisher class
    rclpy.spin(simple_publisher) # Spin the node
    simple_publisher.destroy_node() # Destroy the node explicitly
    rclpy.shutdown() # Shutdown the ROS client library



if __name__ == 'main':
    main() # Call the main function