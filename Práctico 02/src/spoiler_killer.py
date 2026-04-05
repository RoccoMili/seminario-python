# Recurro a importar RegEx para simplificar, pero podría haber sido hecho de forma más compleja
# guardando las posiciones de las mayúsculas o iterando a partes.
import re

def kill_spoilers(text, words):
    filtered = text
    for word in words:
        filtered = re.sub(word, "*" * len(word), filtered, flags=re.IGNORECASE)
    return filtered