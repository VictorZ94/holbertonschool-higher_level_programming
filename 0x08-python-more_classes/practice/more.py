class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(self):
        print("This class is about " + self._class_info + "!")   

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()
