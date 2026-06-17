
from sistema import CarteraInversion, ProyectoMinero


cartera_minera_2024 = CarteraInversion()

print("--- Registrando nuevos proyectos en el sistema ---")
cartera_minera_2024.agregar_proyecto(ProyectoMinero("Reposición Ferrobamba", 1753, "Nuevo"))
cartera_minera_2024.agregar_proyecto(ProyectoMinero("Coimolache Sulfuros", 598, "Nuevo"))
cartera_minera_2024.agregar_proyecto(ProyectoMinero("Mina Justa Subterránea", 500, "Nuevo"))
cartera_minera_2024.agregar_proyecto(ProyectoMinero("Reposición Colquijirca", 431, "Nuevo"))
cartera_minera_2024.agregar_proyecto(ProyectoMinero("Ampliación Huancapetí", 345, "Nuevo"))
cartera_minera_2024.agregar_proyecto(ProyectoMinero("Ampliación Huachocolpa", 167, "Nuevo"))

print("¡Proyectos registrados con éxito!\n")

print("--- Calculando Reporte Analítico ---")
total_nuevos = cartera_minera_2024.calcular_total_por_tipo("Nuevo")

print(f"Monto total acumulado por nuevos proyectos: US$ {total_nuevos} millones")


if total_nuevos == 3794:
    print(" VALIDACIÓN MANUAL: El sistema calcula correctamente el monto de la lectura (US$ 3,794 millones).")
else:
    print(" ALERTA: Hubo un error en el cálculo, los montos no coinciden.")
