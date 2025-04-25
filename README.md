# Calculadora de Costo Total de Producto

Este programa permite calcular el costo total de un producto, aplicando un descuento. El usuario debe ingresar el nombre del producto, el precio unitario, la cantidad y el porcentaje de descuento. El programa valida que los datos ingresados sean correctos antes de realizar el cálculo.

## Descripción

El código solicita la siguiente información al usuario:

1. **Nombre del producto**: El nombre del producto cuyo costo se va a calcular.
2. **Precio unitario**: El costo de un solo artículo del producto.
3. **Cantidad**: La cantidad de productos a adquirir.
4. **Descuento**: El porcentaje de descuento que se aplicará sobre el costo total.

Luego, el programa realiza las siguientes operaciones:
- Calcula el costo total sin aplicar descuento.
- Calcula el monto del descuento.
- Muestra el costo total después de aplicar el descuento.

## Características

- **Validación de entradas**: El programa valida que los valores ingresados sean correctos y dentro de los rangos esperados:
  - El **precio unitario** debe ser un número positivo.
  - La **cantidad** debe ser un número entero positivo.
  - El **descuento** debe estar entre 0 y 100 (incluyendo ambos valores).
  
Si el usuario ingresa un valor no válido, el programa mostrará un mensaje de error y pedirá la entrada nuevamente.

- **Cálculo de costo total**: El programa calcula el costo total utilizando la siguiente fórmula:

