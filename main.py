
class MyMetaClass(type):
    def my_custom_method(self):
        print("my custom method called")

    def print_two_times(self):
        print(f"1 - {self}\n2 - {self}")

    @classmethod
    def __prepare__(mcs, cls, bases):
        namespace = super().__prepare__(cls, bases)
        print('Namespace for object configured!')
        print(namespace)
        return namespace

    def __new__(mcs, cls, bases, dct):
        dct['my_custom_method'] = MyMetaClass.my_custom_method
        dct['print_two_times'] = MyMetaClass.print_two_times
        bases += (str,)
        class_ = super().__new__(mcs, cls, bases, dct)

        print('New object created!')
        print(class_)
        return class_

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("New type initialized")


class MyClass(metaclass=MyMetaClass):
    pass


class MyStr(str):
    # def greetings(self):
    #     print(f"Hello! I'm {self}!")

    # def __init__(self, *args, **kwargs):
    #     self.greetings()

    def __str__(self):
        return super().__str__() + ' changed'

    # def __repr__(self):
    #     return f"my repr -> {self.__class__.__name__}: {self}"


if __name__ == "__main__":
    print("Start...")
    my_obj = MyClass("hi")
    my_obj.my_custom_method()
    my_obj.print_two_times()

    print('Some new code snippet!')

    mystr = MyStr
    for letter in 'hello':
        print(mystr(letter))



