
class MyMetaClass(type):
    def my_custom_method(self):
        print("my custom method called")

    def print_two_times(self):
        print(f"1 - {self}\n2 - {self}")

    @classmethod
    def __prepare__(mcs, cls, bases):
        namespace = super().__prepare__(cls, bases)
        print('Namespace for object configured!')
        return namespace

    def __new__(mcs, cls, bases, dct):
        dct['my_custom_method'] = MyMetaClass.my_custom_method
        dct['print_two_times'] = MyMetaClass.print_two_times
        bases += (str,)
        class_ = super().__new__(mcs, cls, bases, dct)

        print('New object created!')
        return class_

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("New type initialized")


class MyClass(metaclass=MyMetaClass):
    pass


class MyStr(str):
    def __str__(self):
        return super().__str__() + ' changed'


if __name__ == "__main__":
    my_obj = MyClass("hi")
    my_obj.my_custom_method()
    my_obj.print_two_times()
    mystr = MyStr
    for letter in 'hello':
        print(mystr(letter))



