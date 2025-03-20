serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")


match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

cliente = {"nombre": "Anderson", "edad": 25, "ocupacion": "estudiante"}

pelicula = {
    "titulo": "Rambo",
    "ficha_tecnica": {"protagonista": "Rocky", "director": "Rocky"},
}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(f'El cliente es: {nombre} con {edad} y es {ocupacion}')
        case {'titulo': titulo,
              'ficha_tecnica': {
                  'protagonista': protagonista,
                  'director': director
              }}:
            print('Es una pelicula')
            print(f'La pelicula es: {titulo}, protagonizada por: {protagonista} y dirigida por: {director}')
        case _:
            print('No se que es')
            
