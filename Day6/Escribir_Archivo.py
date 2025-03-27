archivo = open('Day6/prueba.txt', 'w')
archivo.write('Soy una malddita prueba nueva')
archivo.writelines(['hola','mundo','aqui'])
archivo.close()

archivo = open('Day6/prueba.txt', 'a')
archivo.write('Soy una malddita prueba nueva')
archivo.writelines(['hola','mundo','aqui'])
archivo.close()