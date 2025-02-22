from collections import deque

class Banco:
    def __init__(self):
        # Inicializa las colas de clientes (normal y prioritaria)
        self.cola_normal = deque()
        self.cola_prioritaria = deque()
    
    def agregar_cliente(self, nombre, prioritario=False):
        # Agrega un cliente a la cola correspondiente
        if prioritario:
            self.cola_prioritaria.append(nombre)
        else:
            self.cola_normal.append(nombre)
        print(f"Cliente {nombre} agregado {'a la cola prioritaria' if prioritario else 'a la cola normal'}.")

    def atender_cliente(self):
        # Atiende al cliente con prioridad o de la cola normal
        if self.cola_prioritaria:
            cliente = self.cola_prioritaria.popleft()
            print(f"Atendiendo a cliente prioritario: {cliente}")
        elif self.cola_normal:
            cliente = self.cola_normal.popleft()
            print(f"Atendiendo a cliente: {cliente}")
        else:
            print("No hay clientes en espera.")
