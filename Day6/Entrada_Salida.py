mi_archivo = open("Day6/prueba.txt")

print(mi_archivo.read())

print(mi_archivo.readline().rstrip())
print(mi_archivo.readline().rstrip())
print(mi_archivo.readline().rstrip())

todas = mi_archivo.readlines()
print(todas)

mi_archivo.close()

