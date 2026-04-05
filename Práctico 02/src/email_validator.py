def validate(email):
    separated = email.strip().split("@")
    if len(separated) != 2:
        return False

    local, domain = separated    

    # Esta primer cláusula es innecesaria si uso email.startswith(args), 
    # pero para tener más legibilidad añadimos ese condicional

    if len(local) == 0 or local.startswith(("@", ".")):
        return False
    elif domain.count(".") == 0:
        return False
    elif domain.endswith(("@", ".")):
        return False
    elif len(domain.split(".")[-1]) < 2:
        return False
    else:
        return True