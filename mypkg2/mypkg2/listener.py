import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node): #Nodeクラスの継承
    
    def __init__(self): #初期化
        super().__init__("Listener")
        self.create_subscription(Int16, "countup", self.cb, 10)
    
    def cb(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
rclpy.spin( ListenerNode() ) #ノードをspinにしかける