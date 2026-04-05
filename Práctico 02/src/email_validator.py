def validate(email):
    separated = email.strip().split("@")
    if len(separated) != 2:
        return False

    nombre, dominio = separated    

    # Esta primer cláusula es innecesaria si uso email.startswith(args), 
    # pero para tener más legibilidad añadimos ese condicional

    if len(nombre) == 0 or nombre.startswith(("@", ".")):
        return False
    elif dominio.count(".") == 0:
        return False
    elif dominio.endswith(("@", ".")):
        return False
    elif len(dominio.split(".")[-1]) < 2:
        return False
    else:
        return True