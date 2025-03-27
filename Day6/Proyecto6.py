from pathlib import Path
from os import system

# Recetario
# Bienvenida
# Nombre e introduccion
print("Hola, mucho guste tenerte aqui")
print("Este es un recetario")
print("Dinos: ")
nombre = input("Como te llamas: ")
system("clear")
print(f"Bienvenido {nombre}, que es lo que quieres hacer")

ruta = Path(Path.home(), "Documents", "Python", "Day6", "Recetas")


# Cuantas recetas existen
def contar_recetas(path):
    """
    The function `contar_recetas` counts the number of recipe files in a specified directory and its
    subdirectories.

    :param path: It looks like there is a small mistake in the code. The variable `path` is not being
    used inside the function. You should replace `Path(ruta)` with `Path(path)` to correctly use the
    input parameter
    :return: The function `contar_recetas` is returning the total count of recipe files found in the
    specified path.
    """
    count = 0
    for txt in Path(ruta).glob("**/*.txt"):
        count += 1
    print(f"Existen {count} recetas, actualmente")
    return count


# Crear una lista de categorias
def crear_list_categorias(path):
    """
    This Python function creates a list of categories based on the directory names in a specified path.

    :param path: It looks like there is a small mistake in your code. You are using `ruta` instead of
    `path` inside the function. You should replace `ruta` with `path` in the for loop
    :return: The function `crear_list_categorias` returns a list of category names extracted from the
    directories in the specified path.
    """
    categorias = []
    count = 0
    for direct in Path(ruta).iterdir():
        categorias.append(direct.stem)
        count += 1
    return categorias


# Crear una lista de recetas
def crear_list_recetas(direction):
    """
    The function `crear_list_recetas` creates a list of recipe names from text files in a specified
    directory.

    :param direction: The `direction` parameter in the `crear_list_recetas` function seems to represent
    the directory path where the text files containing recipes are stored. The function reads all the
    text files in that directory and appends their filenames (without the extension) to a list called
    `recetas`. Finally, it
    :return: The function `crear_list_recetas` is returning a list of recipe names extracted from text
    files in the specified directory.
    """
    recetas = []
    count = 0
    for txt in Path(ruta, str(direction)).glob("*.txt"):
        recetas.append(txt.stem)
        count += 1
    return recetas


# Mostrar Categorias
def mostrar_categorias(path):
    """
    This Python function iterates through a given path and prints out the stem of each directory along
    with a count.

    :param path: It looks like there is a small mistake in the code you provided. The parameter name in
    the function definition is `path`, but inside the function, you are using `ruta`. You should update
    `ruta` to `path` in the function for it to work correctly
    :return: the last directory in the given path after iterating through all directories and printing
    their names with an index.
    """
    count = 0
    for direct in Path(ruta).iterdir():
        count += 1
        print(f"[{count}] {direct.stem}")
    return direct


# Mostrar Recetas
def mostrar_recetas(path, dir):
    """
    This Python function displays a list of recipe files in a specified directory.

    :param path: The `path` parameter in the `mostrar_recetas` function seems to represent the directory
    path where the recipe files are stored. It is used to locate the directory containing the recipe
    files
    :param dir: The `dir` parameter in the `mostrar_recetas` function seems to represent the directory
    within the `path` where the recipe files are stored. It is used to specify the specific directory
    where the function should look for recipe files (files with a `.txt` extension) when listing them
    out
    :return: The function `mostrar_recetas` is returning the last `txt` file that was processed in the
    loop.
    """
    print("--Estas son las recetas--")
    count = 0
    for txt in Path(ruta, str(dir)).glob("*.txt"):
        count += 1
        print(f"[{count}] {txt.stem}")
    return txt


# Elegir categoria
def elegir_categoria(categoria, list_categoria):
    """
    The function `elegir_categoria` checks if a given category is in a list of categories and returns
    the category if it exists, otherwise it returns a message indicating that the category does not
    exist.

    :param categoria: The `categoria` parameter represents the category that you want to check for
    existence in the `list_categoria` parameter. The function `elegir_categoria` will return the
    category if it exists in the list, otherwise it will return "No existe esa categoria" (which means
    "That category does not
    :param list_categoria: The `list_categoria` parameter is likely a list of categories that the
    function `elegir_categoria` will check against to see if the input `categoria` is valid. The
    function will return the input `categoria` if it is found in the `list_categoria`, otherwise it will
    return the message
    :return: If the `categoria` is in the `list_categoria`, then the `categoria` itself is being
    returned. If the `categoria` is not in the `list_categoria`, then the string "No existe esa
    categoria" is being returned.
    """
    if categoria in list_categoria:
        return categoria
    else:
        return "No existe esa categoria"


# Elegir receta
def elegir_receta(receta, list_receta):
    """
    The function "elegir_receta" checks if a given recipe is in a list of recipes and returns the
    filename of the recipe if it exists, otherwise it returns a message indicating that the recipe does
    not exist.

    :param receta: The `receta` parameter in the `elegir_receta` function is a string representing the
    name of a recipe. The function checks if this recipe exists in the `list_receta`, which is a list of
    available recipes. If the recipe is found in the list, the function returns
    :param list_receta: list_receta is a list containing the names of available recipes. The function
    elegir_receta takes two parameters - receta (the name of a specific recipe) and list_receta (the
    list of available recipes). The function checks if the given recipe name is in the list of available
    recipes
    :return: If the `receta` is found in the `list_receta`, the function will return the `receta` with
    ".txt" appended to it. If the `receta` is not found in the `list_receta`, the function will return
    "No existe esa receta".
    """
    if receta in list_receta:
        return receta + ".txt"
    else:
        return "No existe esa receta"


# Leer receta
def leer_receta(categoria, receta):
    """
    The function `leer_receta` reads and prints the contents of a recipe file located in a specified
    category.

    :param categoria: The `categoria` parameter in the `leer_receta` function seems to represent the
    category or type of recipe you want to read. It could be something like "desserts", "main dishes",
    "appetizers", etc
    :param receta: The `receta` parameter in the `leer_receta` function likely refers to the name or
    identifier of a specific recipe within a given category. When calling the `leer_receta` function,
    you would pass the category (e.g., "Desserts") and the specific recipe
    """
    ruta_leer = Path(ruta, categoria, receta)
    print(ruta_leer.read_text())


# Validar si exite la categoria
def validar_exits_cat(op):
    """
    The function `validar_exits_cat` checks if a specified file or directory exists in a given path and
    returns the file/directory name if it exists, otherwise returns False.

    :param op: It looks like the function `validar_exits_cat` is checking if a file or directory exists
    at a specific path based on the input parameter `op`. The function returns `op` if the file or
    directory exists, otherwise it returns `False`
    :return: If the `cat_exits` variable is `True`, the function will return the value of `op`.
    Otherwise, it will return `False`.
    """
    cat_exits = Path(ruta, op).exists()
    if cat_exits is True:
        return op
    else:
        return False


# Validar si existe la receta
def validar_exits_recet(op):
    """
    The function `validar_exits_recet` checks if a file or directory exists at the specified path.

    :param op: The function `validar_exits_recet` takes a parameter `op`, which is a file path. The
    function checks if the file exists at the given path using the `Path(op).exists()` method. If the
    file exists, it returns the file path `op`, otherwise it returns `
    :return: If the path specified by the variable `op` exists, the function `validar_exits_recet` will
    return the path (`op`). Otherwise, it will return `False`.
    """
    recet_exits = Path(op).exists()
    if recet_exits is True:
        return op
    else:
        return False


# Escribir receta
def escribir_receta(ruta, categoria):
    """
    This Python function writes a recipe to a specified file path within a given category, checking if
    the recipe already exists before writing.

    :param ruta: The parameter "ruta" in the function "escribir_receta" is a string representing the
    directory path where the recipe file will be saved
    :param categoria: La categoría de la receta, por ejemplo: postres, platos principales, ensaladas,
    etc
    :return: The function `escribir_receta` is returning a string message depending on whether the
    recipe file already exists or not. If the recipe file does not exist, the function will write the
    recipe content to the file and return a message indicating that the recipe has been created. If the
    recipe file already exists, the function will return a message indicating that the recipe already
    exists.
    """
    ruta_escribir = Path(ruta, categoria)
    nombre = input("Nombre de tu receta: ") + ".txt"
    archivo = ruta_escribir / nombre
    if validar_exits_recet(archivo) is False:
        archivo.write_text(input("Escribe la receta: "))
        return f"La receta: {nombre}, ha sido creada"
    else:
        return f"La receta: {nombre}, existe"


# Crear categoria
def crear_categoria(ruta):
    """
    The function `crear_categoria` creates a new category folder at the specified path if it does not
    already exist.

    :param ruta: The parameter "ruta" in the function "crear_categoria" is likely a string representing
    the path where the new category will be created. It is the directory path where the new category
    folder will be created using the input provided by the user
    :return: The function `crear_categoria` is returning a message indicating whether the category was
    successfully created or if it already exists. The specific message returned depends on the result of
    the `validar_exits_cat` function, which is not defined in the provided code snippet.
    """
    categoria = input("Nombre de la categoria nueva: ")
    if validar_exits_cat(categoria) is False:
        Path(ruta, categoria).mkdir()
        return f"La categoria: {categoria}, ha sido creada"
    else:
        return f"La categoria: {categoria}, ya existe"


# Eliminar receta
def eliminar_receta(categoria, receta):
    """
    This Python function deletes a recipe file within a specified category.

    :param categoria: Categoria refers to the category or type of recipe that you want to delete. It
    could be something like "Desserts", "Main Dishes", "Appetizers", etc
    :param receta: The `receta` parameter in the `eliminar_receta` function represents the name of the
    recipe that you want to delete from a specific category
    :return: The function `eliminar_receta` is returning a message indicating whether the recipe was
    successfully deleted or if it doesn't exist. If the recipe exists and is successfully deleted, it
    will return a message saying "La receta: {receta}, ha sido eliminada". If the recipe does not exist,
    it will return a message saying "La receta: {receta}, no existe".
    """
    receta_eliminar = Path(ruta, categoria, receta)
    if validar_exits_recet(receta_eliminar) is False:
        return f"La receta: {receta}, no existe"
    else:
        receta_eliminar.unlink()
        return f"La receta: {receta}, ha sido eliminada"


# Eliminar categoria
def eliminar_categoria(categoria):
    """
    The function `eliminar_categoria` deletes a category if it exists in a specified path.

    :param categoria: The function `eliminar_categoria(categoria)` is designed to delete a category (or
    folder) named `categoria` within a specified directory (`ruta`). Before deleting the category, it
    checks if the category exists by calling the function `validar_exits_cat(categoria)`
    :return: The function `eliminar_categoria(categoria)` is returning a message indicating whether the
    category has been successfully deleted or if it does not exist.
    """
    if validar_exits_cat(categoria) is False:
        return f"La categoria: {categoria}, no existe"
    else:
        Path(ruta, categoria).rmdir()
        return f"La receta: {categoria}, ha sido eliminada"


# Valida opcion
def validar_op(input_op):
    """
    The function "validar_op" checks if the input is within a specified list of valid options and
    returns the input if it is valid, otherwise returns False.

    :param input_op: The function `validar_op` takes an input parameter `input_op` and checks if it is
    one of the values "1", "2", "3", "4", "5", or "6". If it is, the function returns the input_op
    value. If it is not,
    :return: If the input_op is not one of the values "1", "2", "3", "4", "5", or "6", the function will
    return False. Otherwise, it will return the input_op itself.
    """
    if input_op not in ["1", "2", "3", "4", "5", "6"]:
        return False
    else:
        return input_op


# Pedir opcion
def pedir_op(op):
    """
    The function `pedir_op` prompts the user to choose a valid option from a menu until a valid option
    is selected.

    :param op: The function `pedir_op(op)` seems to be designed to prompt the user to choose a valid
    option from a list of options related to managing recipes and categories. The function will keep
    asking for input until a valid option is selected
    :return: The function `pedir_op(op)` is returning the validated and chosen option `op` after the
    user has selected a valid option from the menu.
    """
    while op is False:
        system("clear")
        print("Escoge una opcion valida")
        print("Tienes estas opciones: ")
        print("-----------------------")
        print("[1] Leer receta")
        print("[2] Crear receta")
        print("[3] Crear categoria")
        print("[4] Eliminar receta")
        print("[5] Eliminar categoria")
        print("[6] Finalizar programa")
        print("-----------------------")
        op = validar_op(input("Elige una opcion valida: "))
    else:
        return op


# Validar si opcion esta en las recetas
def validar_categoria_receta(op, cate_rece):
    """
    The function `validar_categoria_receta` checks if a given option is within a list of recipe
    categories and returns the option if it is, otherwise returns False.
    
    :param op: The `op` parameter in the `validar_categoria_receta` function is the category option that
    you want to validate against a list of recipe categories (`cate_rece`). The function checks if the
    provided category option (`op`) is present in the list of recipe categories. If it is present,
    :param cate_rece: It seems like you have not provided the `cate_rece` parameter in your message.
    Could you please provide the values for the `cate_rece` parameter so that I can assist you further
    with the `validar_categoria_receta` function?
    :return: If the value of `op` is not in the list `cate_rece`, then the function will return `False`.
    Otherwise, it will return the value of `op`.
    """
    if op not in cate_rece:
        return False
    else:
        return op


# Pedir opcion para categoria
def pedir_cat(op):
    """
    The function `pedir_cat` prompts the user to select a valid category option until a valid input is
    provided.
    
    :param op: The `op` parameter in the `pedir_cat` function seems to be a boolean value that controls
    a loop. When `op` is `False`, the function will repeatedly prompt the user to choose a valid option
    until a valid category is selected. Once a valid category is selected, the function
    :return: The function `pedir_cat` is returning the variable `op` when the condition `op is False` is
    no longer met.
    """
    while op is False:
        system("clear")
        print("Escoge una opcion valida")
        mostrar_categorias(ruta)
        op = validar_categoria_receta(
            input("Escribe una opcion valida: "), crear_list_categorias(ruta)
        )
    else:
        return op


# Pedir opcion para receta
def pedir_rece(op, cat):
    """
    The function `pedir_rece` prompts the user to select a valid option from a list of recipes within a
    specified category until a valid option is chosen.
    
    :param op: The parameter "op" in the function "pedir_rece" seems to be a boolean variable that is
    used as a condition in a while loop. It is initially set to False and the loop continues as long as
    "op" is False. The loop displays a message to choose a valid option
    :param cat: The parameter `cat` in the function `pedir_rece` seems to represent the category of
    recipes. It is used to filter and display recipes based on the chosen category
    :return: The function `pedir_rece` is returning the variable `op` when the condition `op is False`
    is no longer met.
    """
    while op is False:
        system("clear")
        print("Escoge una opcion valida")
        mostrar_recetas(ruta, cat)
        op = validar_categoria_receta(
            input("Escribe una opcion valida: "), crear_list_recetas(cat)
        )
    else:
        return op


# Utiliza loop while
def main(ruta):
    """
    The function `main` in the provided Python code is a program that allows users to manage recipes and
    categories, providing options to read, create, delete recipes and categories, and exit the program.
    
    :param ruta: The code you provided seems to be a Python program that manages recipes and categories.
    The `ruta` parameter in the `main` function likely represents the path or location where the recipe
    data is stored or will be stored
    :return: The function `main` is returning the string "Gracias" when the loop condition `while op >=
    0` is no longer met, indicating that the program has finished.
    """
    contar_recetas(ruta)
    print("Tienes estas opciones: ")
    print("-----------------------")
    print("[1] Leer receta")
    print("[2] Crear receta")
    print("[3] Crear categoria")
    print("[4] Eliminar receta")
    print("[5] Eliminar categoria")
    print("[6] Finalizar programa")
    print("-----------------------")
    op = int(pedir_op(validar_op(input("Ingresa un numero entre el 1 - 6: "))))
    while op >= 0:
        match op:
            case 1:
                system("clear")
                print("--Leer Receta--")
                print("Tienes estas opciones:")
                print("----------------------")
                mostrar_categorias(ruta)
                op1 = pedir_cat(
                    validar_categoria_receta(
                        input("Escribe que categoria quieres ver: "),
                        crear_list_categorias(ruta),
                    )
                )
                system("clear")
                mostrar_recetas(ruta, op1)
                op2 = pedir_rece(
                    validar_categoria_receta(
                        input("Escribe que receta quieres leer: "),
                        crear_list_recetas(op1),
                    ),
                    op1,
                )
                print(op2)
                categoria = elegir_categoria(op1, crear_list_categorias(ruta))
                receta = elegir_receta(op2, crear_list_recetas(categoria))
                leer_receta(categoria, receta)
                print("----------------------")
                main(ruta)
            case 2:
                system("clear")
                print("--Crear Receta--")
                print("Tienes estas opciones:")
                print("----------------------")
                mostrar_categorias(ruta)
                op1 = pedir_cat(
                    validar_categoria_receta(
                        input("Escribe que categoria quieres anadir: "),
                        crear_list_categorias(ruta),
                    )
                )
                categoria = elegir_categoria(op1, crear_list_categorias(ruta))
                escribir_receta(ruta, categoria)
                print("----------------------")

                main(ruta)
            case 3:
                system("clear")
                print("--Crear Categoria--")
                print("----------------------")
                mostrar_categorias(ruta)
                print(crear_categoria(ruta))
                print("----------------------")
                main(ruta)
            case 4:
                system("clear")
                print("--Eliminar Receta--")
                print("Tienes estas opciones:")
                print("----------------------")
                mostrar_categorias(ruta)
                op1 = pedir_cat(
                    validar_categoria_receta(
                        input("Escribe que categoria quieres ver: "),
                        crear_list_categorias(ruta),
                    )
                )
                system("clear")
                mostrar_recetas(ruta, op1)
                op2 = pedir_rece(
                    validar_categoria_receta(
                        input("Escribe que receta quieres eliminar: "),
                        crear_list_recetas(op1),
                    ),
                    op1,
                )
                categoria = elegir_categoria(op1, crear_list_categorias(ruta))
                receta = elegir_receta(op2, crear_list_recetas(categoria))
                print(eliminar_receta(categoria, receta))
                print("----------------------")
                main(ruta)
            case 5:
                system("clear")
                print("--Eliminar Categoria--")
                print("Tienes estas opciones:")
                print("----------------------")
                mostrar_categorias(ruta)
                op1 = pedir_cat(
                    validar_categoria_receta(
                        input("Escribe que categoria quieres eliminar: "),
                        crear_list_categorias(ruta),
                    )
                )
                categoria = elegir_categoria(op1, crear_list_categorias(ruta))
                eliminar_categoria(categoria)
                print("----------------------")
                main(ruta)
            case 6:
                system("clear")
                print("--Finalizar--")
                op = -1
    else:
        return "Gracias"


print(main(ruta))
