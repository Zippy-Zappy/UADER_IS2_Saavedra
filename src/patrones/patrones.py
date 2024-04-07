class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def factorial(self, num):
        if num < 0:
            return "El factorial de un negativo no existe."
        if num == 0:
            return 1
        if num > 0:
            return num * self.factorial(num - 1)


s1 = Singleton()
s2 = Singleton()
# if s1 == s2:
#     print("hola")
# if id(s1) == id(s2):
#     print("Singleton funciona.")
# else:
#     print("no funciona.")
print(s1.factorial(1))
print(s2.factorial(5))
