from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

print("Consigna 1:")
'''
Cree una clase bajo el patrón cadena de responsabilidad donde los números del
1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que
identifique la necesidad de consumir el número lo hará y caso contrario lo
pasará al siguiente en la cadena. Implemente una clase que consuma números
primos y otra números pares. Puede ocurrir que un número no sea consumido
por ninguna clase en cuyo caso se marcará como no consumido.
'''


class ManejadorNumeros(ABC):
    @abstractmethod
    def set_siguiente(self, handler: ManejadorNumeros) -> ManejadorNumeros:
        pass

    @abstractmethod
    def manejar_numero(self, numero) -> Optional[str]:
        pass


class AbstractHandler(ManejadorNumeros):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: ManejadorNumeros = None

    def set_siguiente(self, handler: ManejadorNumeros) -> ManejadorNumeros:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def manejar_numero(self, numero: int) -> str:
        if self._next_handler:
            return self._next_handler.manejar_numero(numero)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class ManejadorPrimo(AbstractHandler):
    def manejar_numero(self, numero: int) -> str:
        if self.es_primo(numero):
            return f"{numero} es primo."
        else:
            return super().manejar_numero(numero)
    
    def es_primo(self, numero: int) -> bool:
        if numero < 2:
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

class ManejadorPares(AbstractHandler):
    def manejar_numero(self, numero: int) -> str:
        if self.es_par(numero):
            return f"{numero} es par."
        else:
            return super().manejar_numero(numero)
    
    def es_par(self, numero: int) -> bool:
        return (numero % 2 == 0)

def client_code(handler: ManejadorNumeros) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for num in range(1, 101):
        result = handler.manejar_numero(num)
        if result:
            print (f"{result}")
        else:
            print (f"{num} no es par ni primo.")


if __name__ == "__main__":
    primos = ManejadorPrimo()
    pares = ManejadorPares()

    primos.set_siguiente(pares)
    client_code(primos)

print()
print("Consigna 2:")
'''
Implemente una clase bajo el patrón iterator que almacene una cadena de
caracteres y permita recorrerla en sentido directo y reverso.
'''
from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticalOrderIterator(Iterator):
    _position: int = None

    _reverse: bool = False

    def __init__(self, collection: CadenaCollecion, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class CadenaCollecion(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_iterador_reverso(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def agregar_objeto(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    coleccion = CadenaCollecion()
    coleccion.agregar_objeto("Primero")
    coleccion.agregar_objeto("Segundo")
    coleccion.agregar_objeto("Tercero")

    print("Recorrido directo:")
    print("\n".join(coleccion))
    print("")

    print("Recorrido reverso:")
    print("\n".join(coleccion.get_iterador_reverso()), end="")
    print("\n")
