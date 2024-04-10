print("Consigna 1:")
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

print()
print("Consigna 2:")

from abc import ABC, abstractmethod

#Interfaz
class CalculadorImpuestos(ABC):
    @abstractmethod
    def calcular(self, base_imponible: float) -> float:
        pass

#Clases de negocio
class CalculadorIVA(CalculadorImpuestos):
    def calcular(self, base_imponible: float) -> float:
        return base_imponible * 0.21

class CalculadorIIBB(CalculadorImpuestos):
    def calcular(self, base_imponible: float) -> float:
        return base_imponible * 0.05
    
class CalculadorContribuciones(CalculadorImpuestos):
    def calcular(self, base_imponible: float) -> float:
        return base_imponible * 0.012

#Abstract Factory
class FabricaImpuestos(ABC):
    @abstractmethod
    def crearCalculadorIVA(self) -> CalculadorImpuestos:
        pass

    def crearCalculadorIIBB(self) -> CalculadorIIBB:
        pass

    def crearCalculadorContribuciones(self) -> CalculadorContribuciones:
        pass

#Abstract Fabricas Concretas
class FabricaImpuestosArgentina(FabricaImpuestos):
    def crearCalculadorIVA(self) -> CalculadorImpuestos:
        return CalculadorIVA()
    
    def crearCalculadorIIBB(self) -> CalculadorIIBB:
        return CalculadorIIBB()
    
    def crearCalculadorContribuciones(self) -> CalculadorContribuciones:
        return CalculadorContribuciones()

#otro podría ser FabricaImpuestosUruguay

if __name__ == "__main__":
    base_imponible = 1500
    factory = FabricaImpuestosArgentina()
    calculadora = factory.crearCalculadorIVA()
    total = calculadora.calcular(base_imponible)
    print(f"El total de impuestos sería {total}")

print()
print("Consigna 3:")

class Factory(ABC):
    @abstractmethod
    def metodo_factory(self):
        pass

    def mostrar_envio(self):
        #crea el objeto producto
        producto = self.metodo_factory()

        #se usa el producto
        resultado = f"Se ha completado la transacción."

        return resultado

#las concrete factory van a sobreescribir el método de operación
#para cambiar el resultado del producto
class TipoEnvio(ABC):
    @abstractmethod
    def mostrar_envio(self) -> str:
        pass

class ConcreteFactory1(Factory):
    def mostrar_envio(self) -> TipoEnvio:
        return EntregaDelivery()
    
class ConcreteFactory2(Factory):
    def mostrar_envio(self) -> TipoEnvio:
        return EntregaCliente()

class ConcreteFactory3(Factory):
    def mostrar_envio(self) -> TipoEnvio:
        return EntregaMostrador()



"""
Productos Concretos, implementan la interfaz de Producto (TipoEnvio)
"""


class EntregaDelivery(TipoEnvio):
    def mostrar_envio(self) -> str:
        return "Enviaremos al cadete."

class EntregaCliente(TipoEnvio):
    def mostrar_envio(self) -> str:
        return "Lo esperaremos en el local."

class EntregaMostrador(TipoEnvio):
    def mostrar_envio(self) -> str:
        return "Retire su producto por el mostrador."

def client_code(creator: Factory) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as creator.some_operation() the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    #Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.
    print(f"Operación completa. {creator.mostrar_envio()}", end="")

if __name__ == "__main__":
    print("Entrega por delivery:")
    client_code(EntregaDelivery())
    print()
    print("\nEntrega por mostrador:")
    client_code(EntregaMostrador())
    print()
    print("\nUsted se dirigirá al local.")
    client_code(EntregaCliente())