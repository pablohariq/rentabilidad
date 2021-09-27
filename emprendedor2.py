precio_normal = int(input("Ingrese el precio de la suscripción normal: \n >"))
usuarios_normal = int(input("Ingrese el número de usuarios de suscripción normal: \n >"))
usuarios_premium = int(input("Ingrese el número de usuarios de suscripción premium: \n >"))
gastos_totales = int(input("Ingrese los gastos totales: \n >"))

multiplicador_premium = 1.5 #define la razón de precio entre la suscripción premium y la normal
precio_premium = precio_normal * multiplicador_premium

utilidades = precio_normal * usuarios_normal + precio_premium * usuarios_premium - gastos_totales

print(f"Las utilidades totales son de ${utilidades:.2f}")