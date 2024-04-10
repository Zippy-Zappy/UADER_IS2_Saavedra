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
        resultado = f"{producto.mostrar_envio()}."

        return resultado

#las concrete factory van a sobreescribir el método de operación
#para cambiar el resultado del producto
class TipoEnvio(ABC):
    @abstractmethod
    def mostrar_envio(self) -> str:
        pass

class ConcreteFactory1(Factory):
    def metodo_factory(self) -> TipoEnvio:
        return EntregaDelivery()
    
class ConcreteFactory2(Factory):
    def metodo_factory(self) -> TipoEnvio:
        return EntregaCliente()

class ConcreteFactory3(Factory):
    def metodo_factory(self) -> TipoEnvio:
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
    print(f"Transacción completa. {creator.mostrar_envio()}", end="")

if __name__ == "__main__":
    print("Entrega por delivery:")
    client_code(ConcreteFactory1())
    print()
    print("\nEntrega por mostrador:")
    client_code(ConcreteFactory2())
    print()
    print("\nUsted se dirigirá al local.")
    client_code(ConcreteFactory3())


print()
print("Consigna 4:")
class Factura:
    def __init__(self, importe):
        self.importe = importe
    
#utiliza el Factory Method.
class FacturaFactory(ABC):
    def crear_factura(self, importe):
        pass

#Concrete Factories    
class FacturaIVAResponsable(Factura):
    def __str__(self):
        return f"Factura IVA Responsable, importe: ${self.importe}"

class FacturaIVANoInscripto(Factura):
    def __str__(self):
        return f"Factura IVA No Inscripto, importe: ${self.importe}"

class FacturaIVAExento(Factura):
    def __str__(self):
        return f"Factura IVA Exento, importe: ${self.importe}"

#implementación de interfaz FacturaFactory
class FactoryResponsable(FacturaFactory):
    def crear_factura(self, importe):
        return FacturaIVAResponsable(importe)

class FactoryNoInscripto(FacturaFactory):
    def crear_factura(self, importe):
        return FacturaIVANoInscripto(importe)

class FactoryExento(FacturaFactory):
    def crear_factura(self, importe):
        return FacturaIVAExento(importe)

#equivale al code_client
def generar_factura(factory, importe):
    factura = factory.crear_factura(importe)
    print(factura)

if __name__ == "__main__":
    print()
    generar_factura(FactoryResponsable(), 100)
    print()
    generar_factura(FactoryNoInscripto(), 500)
    print()
    generar_factura(FactoryExento(), 1000)

print()
print("Consigna 5:")

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_body(self) -> None:
        pass

    @abstractmethod
    def produce_wing_1(self) -> None:
        pass

    @abstractmethod
    def produce_wing_2(self) -> None:
        pass

    @abstractmethod
    def produce_turbine_1(self) -> None:
        pass

    @abstractmethod
    def produce_turbine_2(self) -> None:
        pass

    @abstractmethod
    def produce_undercarriage(self) -> None:
        pass

class Product():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes del producto: {', '.join(self.parts)}", end="")

#concrete builder, implementa los pasos
class AvionBuilder(Builder):
    def __init__(self) -> None:
        """
        para que contenga un producto vacío
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_body(self) -> None:
        self._product.add("Body")

    def produce_wing_1(self) -> None:
        self._product.add("Ala 1")

    def produce_wing_2(self) -> None:
        self._product.add("Ala 2")

    def produce_turbine_1(self) -> None:
        self._product.add("Turbina 1")
    
    def produce_turbine_2(self) -> None:
        self._product.add("Turbina 2")
    
    def produce_undercarriage(self) -> None:
        self._product.add("Tren de aterrizaje")

#el director, ejecuta los pasos en cierta secuencia. Es opcional.
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_body()

    def build_full_featured_product(self) -> None:
        self.builder.produce_wing_1()
        self.builder.produce_wing_2()
        self.builder.produce_turbine_1()
        self.builder.produce_turbine_2()
        self.builder.produce_undercarriage()

    def build_parcial(self) -> None:
        self.builder.produce_wing_2()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = AvionBuilder()
    director.builder = builder

    print("Producto básico: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Producto completo: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_wing_1()
    builder.produce_wing_2()
    builder.product.list_parts()

    print("\n")