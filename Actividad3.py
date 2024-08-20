# Calcular el porcentaje de una compra

precio_original = float (input("Ingrese el precio original de la compra:"))
descuento = int (input("Ingrese el porcentaje del descuento:"))

#Calcular el descuento

precioDescuento = (precio_original) * (descuento / 100)
precioFinal = precio_original - precioDescuento

print ("El precio final de la compra, con el descuento es: ", precioFinal)
