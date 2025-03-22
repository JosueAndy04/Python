from random import choice
# Ahorcado

# Elegir palabra
# Texto de donde elegir
parrafo = """
            Headlines jungle is the only rule
            Front page roar of the nation cool
            Turn it up this is my attitude
            Take it or leave it
            """
# Plabra elegida
word = choice(list(set(parrafo.lower().split())))


# Mostrar los guiones que expresan la cantidad de letras
def guiones(word):
    """
    The function "guiones" takes a word as input and returns a list of dashes with the same length as
    the word.
    
    :param word: Thank you for providing the code snippet. Could you please provide the word for which
    you would like to generate dashes (guiones)?
    :return: The function `guiones` is returning a list of dashes (`-`) with the same length as the
    input word.
    """
    guiones = []
    for n in word:
        guiones.append("-")
    return guiones


# Pedir letra
def pedir_letra():
    """
    This Python function prompts the user to input a letter and validates if it is a valid letter.
    :return: The function `pedir_letra` is returning the validated letter input by the user.
    """
    letter = val_letter(input("Elige una letra: "))

    while letter is False:
        print("Escoge una letra valida")
        letter = val_letter(input("Elige una letra: "))
    else:
        return letter


# validar que sea letra
def val_letter(letter):
    """
    The function `val_letter` checks if a given input is a lowercase letter and returns the letter if it
    is, otherwise returns False.
    
    :param letter: The function `val_letter` takes a parameter `letter` which is expected to be a single
    character. The function checks if the input `letter` is a lowercase letter from 'a' to 'z'. If the
    input `letter` is not a lowercase letter, the function returns `False`
    :return: If the input `letter` is a valid lowercase letter from the English alphabet, it will return
    the input `letter`. Otherwise, it will return `False`.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    if letter not in letters:
        return False
    else:
        return letter


# Letra que si se encuentra
def ver_letter_word(letter, word):
    """
    The function `ver_letter_word` checks if a given letter is present in a word and returns the letter
    if it is, otherwise it returns False.
    
    :param letter: The `ver_letter_word` function takes two parameters: `letter` and `word`. The
    function checks if the `letter` is present in the `word`. If the `letter` is found in the `word`,
    the function returns the `letter`. If the `letter` is not found
    :param word: It seems like you have not provided the value for the `word` parameter in the
    `ver_letter_word` function. Could you please provide the word for which you want to verify the
    presence of a specific letter?
    :return: If the letter is found in the word, the function will return the letter. If the letter is
    not found in the word, the function will return False.
    """
    if letter not in word:
        return False
    else:
        return letter


# Letra repetida
def letra_repetida(letter, word):
    """
    The function checks if a given letter is repeated in a word and returns False if it is, otherwise it
    returns the letter.
    
    :param letter: The `letter` parameter in the `letra_repetida` function is a single character that
    you want to check for repetition in the `word` parameter
    :param word: Thank you for providing the parameters for the function. Could you please also provide
    the value of the `word` parameter so that I can assist you further with the `letra_repetida`
    function?
    :return: If the letter is not found in the word, the function will return the letter.
    """
    if letter in word:
        print("Letra repetida")
        return False
    else:
        return letter


# ordenar letras
def ordenar_letras(letter, guiones, word):
    """
    The function "ordenar_letras" takes a letter, a list of dashes, and a word, and replaces the dashes
    with the letter at corresponding positions in the word.
    
    :param letter: The `letter` parameter in the `ordenar_letras` function represents the letter that
    you want to find and place in the corresponding position within the `guiones` list based on its
    occurrence in the `word` string
    :param guiones: The `guiones` parameter seems to represent a list of placeholders or dashes that
    correspond to the letters in the `word`. The function `ordenar_letras` appears to be attempting to
    replace the dashes with the specified `letter` in the `word`
    :param word: The `word` parameter in the `ordenar_letras` function is a string that contains the
    word for which you want to fill in the dashes with the specified letter
    :return: The function `ordenar_letras` is returning the updated list `guiones` with the letter
    filled in at the corresponding positions where it matches in the `word`.
    """
    i = 0
    for le in word:
        if word[i] == letter:
            guiones[i] = word[i]
            i += 1
        else:
            i += 1
    return guiones


# Perder vida
def vidas(vida, b):
    """
    The function "vidas" decreases the value of the variable "vida" by 1 if the boolean variable "b" is
    False.
    
    :param vida: The `vida` parameter in the `vidas` function represents the current number of lives or
    health points. The function checks the value of the `b` parameter and decreases the `vida` by 1 if
    `b` is `False`. Otherwise, it returns the current `vida` value
    :param b: The parameter `b` in the `vidas` function is a boolean value that determines whether a
    life should be deducted from the `vida` parameter. If `b` is `False`, then a life is deducted from
    `vida`; otherwise, no life is deducted
    :return: The function `vidas` will return the updated value of `vida` if `b` is `False`, otherwise
    it will return the original value of `vida`.
    """
    if b is False:
        vida -= 1
        return vida
    else:
        return vida


# Ganar
def ganar(word_gues, word_win):
    """
    The function `ganar` compares two words and returns a message if they are the same after removing
    duplicates and sorting.
    
    :param word_gues: The `word_gues` parameter seems to represent the word guessed by a player in a
    game. It is expected to be a string containing the characters guessed by the player
    :param word_win: It seems like you were about to provide the `word_win` parameter for the `ganar`
    function. Please go ahead and provide the value of `word_win` so that I can assist you further
    :return: a message indicating whether the player has won the game or not. If the sorted unique
    characters in the guessed word match the sorted unique characters in the winning word, it will
    return 'Has ganado, la palabra es "{word_win}"', where {word_win} is the actual winning word.
    """
    word_gues = list(set(word_gues))
    word_win1 = list(set(word_win))
    word_gues.sort()
    word_win1.sort()
    word_gues = "".join(word_gues)
    word_win1 = "".join(word_win1)
    if word_gues == word_win1:
        return f'Has ganado, la palabra es "{word_win}"'


# Main
def main(word):
    """
    The main function in this Python code takes a word as input, allows the user to guess letters, and
    provides feedback on correct and incorrect guesses until the word is fully guessed or the player
    runs out of lives.
    
    :param word: The code you provided seems to be a part of a game or program where a player needs to
    guess a word. It includes functions for managing the game flow, such as checking guessed letters,
    updating the displayed word, and tracking remaining lives
    """
    v = len(word)
    word_guest = []
    print(guiones(word))
    word_print = guiones(word)
    while v > 0:
        print(f"Te quedan: {v}, vidas")
        letter = letra_repetida(ver_letter_word(pedir_letra(), word), word_guest)
        if letter is False:
            v = vidas(v, letter)
            print(word_print)
        else:
            word_print = ordenar_letras(letter, word_print, word)
            word_guest.append(letter)
            if len(set(word_guest)) == len(set(word)):
                word_guest = "".join(word_guest)
                print(ganar(word_guest, word))
                break
            else:
                print(word_print)
    else:
        print(f"Has perdido, la palabra es: '{word}'")


main(word)
