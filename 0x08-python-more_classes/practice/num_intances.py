"""class C:
    counter = 0

    def __init__(self):
        #it's the same to use C.counter 
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

x = C()
print("Number of instances: : " + str(C.counter))
y = C()
print("Number of instances: : " + str(C.counter))
z = C()
print("Number of instances: : " + str(C.counter))
del x
print("Number of instances: : " + str(C.counter))
del y
print("Number of instances: : " + str(C.counter))
del z
print("Number of instances: : " + str(C.counter))
"""

class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())