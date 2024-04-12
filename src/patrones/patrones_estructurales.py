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

    ping.execute(direccion_ip_test)