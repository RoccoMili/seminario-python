# Me pareció buen uso de un módulo estándar, porque al trabajar con
# valores ASCII necesitaba algo de este estilo para hacer un translate
# (que era mi idea original). Tuve que investigarlo.
import string

def cipher(message, shift):
    alpha_shift = shift % 26
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    shifted_lower = lowercase[alpha_shift:] + lowercase[:alpha_shift]
    shifted_upper = uppercase[alpha_shift:] + uppercase[:alpha_shift]
    transtable = str.maketrans(lowercase + uppercase, shifted_lower + shifted_upper)
    return message.translate(transtable)