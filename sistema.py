
class ProyectoMinero:
    def __init__(self, nombre, inversion, tipo):
        self.nombre = nombre
        self.inversion = inversion  # Monto en millones de US$
        self.tipo = tipo            # Puede ser: "Nuevo", "Conservado" o "Modificado"

class CarteraInversion:
    def __init__(self):
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def calcular_total_por_tipo(self, tipo_buscado):
        # Filtra y suma la inversión de los proyectos que coincidan con el tipo
        total = sum(p.inversion for p in self.proyectos if p.tipo == tipo_buscado)
        return total
