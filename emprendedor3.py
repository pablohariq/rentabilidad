precio = int(input("Ingrese el precio de la suscripción (use números enteros) \n >"))
numero_usuarios = int(input("Ingrese el número de usuarios (use números enteros) \n >"))
gastos_totales = int(input("Ingrese los gastos totales (use números enteros) \n >"))
utilidades_anterior = int(input("Ingrese las utilidades del año anterior \n >"))

utilidades = precio * numero_usuarios - gastos_totales
razon_utilidades = round(utilidades/utilidades_anterior, 2)

print(f"Las utilidades de este año son de ${utilidades}, y corresponden a {razon_utilidades} veces las utilidades del año anterior ({razon_utilidades*100}%).")