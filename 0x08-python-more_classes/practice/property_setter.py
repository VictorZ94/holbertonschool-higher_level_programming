# class SampleClass:
    
#     def __init__(self, a):
#         ## private varibale or property in Python
#         self.__a = a

#     ## getter method to get the properties using an object
#     def get_a(self):
#         return self.__a

#     ## setter method to change the value 'a' using an object
#     def set_a(self, a):
#         self.__a = a

# ## creating an object
# obj = SampleClass(10)

# ## getting the value of 'a' using get_a() method
# print(obj.get_a())

# ## setting a new value to the 'a' using set_a() method
# obj.set_a(45)

# print(obj.get_a())

# print(obj.__dict__)

class SampleClass1:
    
    def __init__(self, a):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.set_a(a)

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):

        ## condition to check whether 'a' is suitable or not
        if a > 0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2
            
## creating an object for the class 'SampleClass1'
obj = SampleClass1(16)

print(obj.get_a())