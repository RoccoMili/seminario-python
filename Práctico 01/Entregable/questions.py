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
    
word = random.choice(words[category.lower()])

print()

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