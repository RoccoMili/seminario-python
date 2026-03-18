import random

words = {
    "datos": ["variable", "cadena", "entero", "lista"],
    "general": ["python", "programa", "funcion", "bucle"],
}

guessed = []
attempts = 6
points = 0

categories = ", ".join(words.keys())
category = input(f"¡Bienvenido al Ahorcado! Elegí una categoría de las siguientes: {categories}\n")

while category.lower() not in words:
    category = input(f"Categoría inválida. Elegí una categoría de las siguientes: {categories}\n")

# NOTA: La consigna pide "al jugar varias rondas seguidas": para no usar funciones todavía
# porque corresponde a otra clase, voy a tomar otro approach distinto con un for externo
# Dejo en claro que esto era más fácil llamándolo con una función. 

sampled_words = random.sample(words[category], k=len(words[category]))

print()

for word in sampled_words:
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            points += 6
            print(f"¡Ganaste! Quedaste con {points} puntos")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()
        
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif not letter.isalpha() or len(letter) != 1:
            print("Entrada no válida")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            points -= 1
            print("Esa letra no está en la palabra.")

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}. Tenés 0 puntos.")

    # Extra, especialmente útil cuando hice debugging
    if word != sampled_words[-1]:
        keep_going = input("¿Querés seguir jugando? Responder NO para terminar\n")
        if keep_going.lower() == "no":
            break
    else:
        print("¡No hay más en esta categoría!")

    guessed.clear()
    progress = ""
    attempts = 6
    points = 0

    print()