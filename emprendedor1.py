precio = int(input("Ingrese el precio de la suscripción (use números enteros) \n >"))
numero_usuarios = int(input("Ingrese el número de usuarios (use números enteros) \n >"))
gastos_totales = int(input("Ingrese los gastos totales (use números enteros) \n >"))

utilidad = precio * numero_usuarios - gastos_totales

print(f"La utilidad es de ${utilidad}.")