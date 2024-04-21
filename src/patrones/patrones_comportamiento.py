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

print()
print("Consigna 3:")
'''
Implemente una clase bajo el patrón observer donde una serie de clases están
subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4
caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio
coinciden. Implemente 4 clases de tal manera que cada una tenga un ID
especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con
ID para el que tenga una clase implementada.
'''
import random

class Sujeto(ABC):
    @abstractmethod
    def attach(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def detach(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
    
class Observador(ABC):
    @abstractmethod
    def update(self, sujeto: Sujeto) -> None:
        pass

class ConcreteSubject(Sujeto):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: str = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observador] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observador: Observador) -> None:
        print("Sujeto: agregué un observador.")
        self._observers.append(observador)

    def detach(self, observador: Observador) -> None:
        self._observers.remove(observador)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Sujeto: notificando a los observadores...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSujeto: estoy haciendo algo...")
        lista = ["ABCD", "EFGH", "WXYZ", "LALO", "IJKL", "DCBA", "MNOPQ", "LEET"]
        self._state = random.choice(lista)

        print(f"Sujeto: mi estado cambió a: {self._state}")
        self.notify()

class ObservadorA(Observador):
    def update(self, sujeto: Sujeto) -> None:
        if sujeto._state == "WXYZ":
            print("Observador XWYZ reacciona al evento.")

class ObservadorB(Observador):
    def update(self, sujeto: Sujeto) -> None:
        if sujeto._state == "ABCD":
            print("Observador ABCD reacciona al evento.")

class ObservadorC(Observador):
    def update(self, sujeto: Sujeto) -> None:
        if sujeto._state == "LALO":
            print("Observador LALO reacciona al evento.")

class ObservadorD(Observador):
    def update(self, sujeto: Sujeto) -> None:
        if sujeto._state == "EFGH":
            print("Observador EFGH reacciona al evento.")
        
if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ObservadorA()
    subject.attach(observer_a)

    observer_b = ObservadorB()
    subject.attach(observer_b)

    observer_c = ObservadorC()
    subject.attach(observer_c)

    observer_d = ObservadorD()
    subject.attach(observer_d)

    subject.some_business_logic()
    subject.some_business_logic()
