print("Consigna 1:")
'''
Provea una clase ping que luego de creada al ser invocada con un método
“execute(string)” realice 10 intentos de ping a la dirección IP contenida en
“string” (argumento pasado), la clase solo debe funcionar si la dirección IP
provista comienza con “192.”. Provea un método executefree(string) que haga
lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
www.google.com usando el método executefree de ping y re-envie a execute
de la clase ping en cualquier otro caso. (Modele la solución como un patrón
proxy).
'''

from abc import ABC, abstractmethod
import os

class IPing(ABC): #corresponde al Subject, la interfaz que conecta ambas
    @abstractmethod
    def execute(self, direccion_ip: str) -> None:
        pass

    @abstractmethod
    def executefree(self, direccion_ip: str) -> None:
        pass

class Ping(IPing):  #Equivale a RealSubject
    def execute(self, direccion_ip: str) -> None:
        if direccion_ip.startswith("192."):
            for _ in range(10):
                os.system(f"ping {direccion_ip}")
        else:
            print("La dirección IP no empieza con 192.")
    
    def executefree(self, direccion_ip: str) -> None:
        for _ in range(10):
            os.system(f"ping {direccion_ip}")

class PingProxy(IPing): #equivale a Proxy

    def __init__(self, ping: Ping) -> None:
        self.ping = ping

    def execute(self, direccion_ip: str) -> None:
        if direccion_ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(direccion_ip)

    def executefree(self, direccion_ip: str) -> None:
        for _ in range(10):
            os.system(f"ping {direccion_ip}")

if __name__ == "__main__":
    instancia = Ping()
    ping = PingProxy(instancia)

    direccion_ip = "192.168.0.254"
    direccion_ip_test = "192.168.1.200"
    direccion_ip_fail = "190.168.0.254"

    #ping.execute(direccion_ip_test)

print()
print("Consigna 2:")
'''
Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
de 10 mts. Genere una clase que represente a las láminas en forma genérica al
cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
patrón bridge en la solución).
'''
class TrenBridge(ABC): #Implementation
    @abstractmethod
    def mostrar_tren(self) -> str:
        pass

class Tren: #Abstraction
    def __init__(self, tren_laminador: TrenBridge) -> None:
        self.tren_laminador = tren_laminador
    
    def mostrar(self) -> str:
        return f"Se enviará a: {self.tren_laminador.mostrar_tren()}"

class TrenLaminadorCinco(TrenBridge): #ConcreteImplementation
    def mostrar_tren(self) -> str:
        return f"Tren Laminador de 5 metros."

class TrenLaminadorDiez(TrenBridge): #ConcreteImplementation
    def mostrar_tren(self) -> str:
        return f"Tren Laminador de 10 metros."

if __name__ == "__main__":
    implementacion_cinco = TrenLaminadorCinco()
    lamina_cinco = Tren(implementacion_cinco)
    print(lamina_cinco.mostrar())

    implementacion_diez = TrenLaminadorDiez()
    lamina_diez = Tren(implementacion_diez)
    print(lamina_diez.mostrar())

print()
print("Consigna 3:")
'''
Represente la lista de piezas componentes de un ensamblado con sus
relaciones jerárquicas. Empiece con un producto principal formado por tres
sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
que representen esa configuración y la muestren. Luego agregue un subconjunto
opcional adicional también formado por cuatro piezas. (Use el patrón
composite).
'''
from typing import List

class ComponenteComposite(ABC):
    @abstractmethod
    def mostrar(self) -> str:
        pass

class Pieza(ComponenteComposite): #clase concreta para piezas individuales
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def mostrar(self) -> str:
        return f"{self.nombre}"

class Subconjunto(ComponenteComposite): #clase concreta para subconjuntos
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self._children: List[ComponenteComposite] = [] 
    
    def agregar(self, componente: ComponenteComposite) -> None:
        self._children.append(componente)
    
    def eliminar(self, componente: ComponenteComposite) -> None:
        self._children.remove(componente)
    
    def mostrar(self) -> str:
        resultados = []
        for child in self._children:
            resultados.append(child.mostrar())
        return f"{self.nombre}{resultados}"
    
if __name__ == "__main__":
    pieza1 = Pieza("Pieza A")
    pieza2 = Pieza("Pieza B")
    pieza3 = Pieza("Pieza C")
    pieza4 = Pieza("Pieza D")
    subconjunto1 = Subconjunto("Subconjunto A")
    subconjunto1.agregar(pieza1)
    subconjunto1.agregar(pieza2)
    subconjunto1.agregar(pieza3)
    subconjunto1.agregar(pieza4)
    
    pieza5 = Pieza("Pieza E")
    pieza6 = Pieza("Pieza F")
    pieza7 = Pieza("Pieza G")
    pieza8 = Pieza("Pieza H")
    subconjunto2 = Subconjunto("Subconjunto B")
    subconjunto2.agregar(pieza5)
    subconjunto2.agregar(pieza6)
    subconjunto2.agregar(pieza7)
    subconjunto2.agregar(pieza8)

    pieza9 = Pieza("Pieza I")
    pieza10 = Pieza("Pieza J")
    pieza11 = Pieza("Pieza K")
    pieza12 = Pieza("Pieza L")
    subconjunto3 = Subconjunto("Subconjunto C")
    subconjunto3.agregar(pieza9)
    subconjunto3.agregar(pieza10)
    subconjunto3.agregar(pieza11)
    subconjunto3.agregar(pieza12)

    conjunto_principal = Subconjunto("Producto principal")
    conjunto_principal.agregar(subconjunto1)
    conjunto_principal.agregar(subconjunto2)
    conjunto_principal.agregar(subconjunto3)

    print(conjunto_principal.mostrar())

print()
print("Consigna 4:")
'''
Implemente una clase que permita a un número cualquiera imprimir su valor,
luego agregarle sucesivamente.
a. Sumarle 2.
b. Multiplicarle por 2.
c. Dividirlo por 3.
Mostrar los resultados de la clase sin agregados y con la invocación anidada a
las clases con las diferentes operaciones. Use un patrón decorator para
implementar.
'''
class Component():
    def mostrar_numero(self) -> int:
        pass


class ConcreteComponent(Component):
    def __init__(self, numero):
        self.numero = numero

    def mostrar_numero(self) -> int:
        return self.numero


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def mostrar_numero(self) -> int:
        return self._component.mostrar_numero()


class SumarleDos(Decorator):
    def operation(self) -> int:
        return self.component.mostrar_numero() + 2


class MultiplicarleDos(Decorator):
    def mostrar_numero(self) -> int:
        return self.component.mostrar_numero() * 2

class DividirleTres(Decorator):
    def mostrar_numero(self) -> int:
        return self.component.mostrar_numero() / 3


def client_code(component: Component) -> None:
    print(f"RESULT: {component.mostrar_numero()}", end="")


if __name__ == "__main__":
    # This way the client code can support both simple components...
    numero = 10
    num_base_decorado = ConcreteComponent(numero)
    num_decorado = DividirleTres(MultiplicarleDos(SumarleDos(numero)))
    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = SumarleDos(num_base_decorado)
    decorator2 = MultiplicarleDos(decorator1)
    decorator3 = DividirleTres(decorator2)
    
    client_code(decorator3)

    print("\n")
   #debería funcionar así? ...