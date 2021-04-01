import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

n = 0

class TalkerNode(Node):
    
    def __init__(self):
        super().__init__("Talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.timer = self.create_timer(0.5, self.cb)
        print("talker初期化メソッド")
    
    def cb(self):
        global n
        msg = Int16()
        msg.data = n
        self.pub.publish(msg)
        n += 1
        self.get_logger().info("Talk: %d" % n)


def main():
    rclpy.init()
    node = TalkerNode()
    try:
        rclpy.spin(node) #ノードをspinにしかける
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# # オリジナル
# rclpy.init()
# node = Node("talker")
# pub = node.create_publisher(Int16, "countup", 10)
# n = 0

# def cb():
#     global n
#     msg = Int16()
#     msg.data = n
#     pub.publish(msg)
#     n +=1

# node.create_timer(1, cb)
# rclpy.spin(node)
