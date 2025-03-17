# Proyecto 2
# Preguntar por nombre y venta
# Frase que indique su nombre y el total de sus comisiones

# Preguntar nombre
nombre = input("Cual es tu nombre: ")
apellido = input("Cual es tu apellido: ")

# Preguntar por comisiones
ventas = float(input("Cual es el total de ventas del mes: "))
comision = float(ventas) * 0.13
resultado = round(ventas + comision, 2)

# Resultado
print(
    f"Hola {nombre} {apellido} tu comision es de: {comision} \nTus ventas son: {ventas} \nTotal: {resultado} "
)
