# Ingreso de datos
nombre_producto = input("Ingrese el nombre del producto: ")

# Validar precio unitario
while True:
    try:
        precio_unitario = float(input("Ingrese el precio unitario: "))
        if precio_unitario <= 0:
            print("Error: El precio debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Error: Ingrese un número válido para el precio.")

# Validar cantidad
while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número positiva.")
        else:
            break
    except ValueError:
        print("Error: Ingrese un número entero válido para la cantidad.")

# Validar descuento
while True:
    try:
        descuento = float(input("Ingrese el porcentaje de descuento (0-100): "))
        if 0 <= descuento <= 100:
            break
        else:
            print("Error: El descuento debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingrese un número válido para el descuento.")

# Calcular el costo total
costo_sin_descuento = precio_unitario * cantidad
monto_descuento = costo_sin_descuento * (descuento / 100)
costo_total = costo_sin_descuento - monto_descuento

# Mostrar el resultado
print(f"\nEl costo total de '{nombre_producto}' es: ${costo_total:.2f}")

