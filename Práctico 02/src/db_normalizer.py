def conditions(student):
    if student["name"] is None or not str(student["name"]).strip():
        return False
    if student["grade"] is None or not student["grade"].isnumeric():
        return False
    else:
        return True

def normalize(db):
    normalized = [student for student in db if conditions(student)]
    for student in normalized:
        student["name"] = student["name"].strip().title()
        student["status"] = student["status"].strip().title()
    normalized_keys = {}
    for student in normalized:
        current_key = student["name"].lower()
        if current_key not in normalized_keys:
            normalized_keys[current_key] = student
        else:
            if int(student["grade"]) > int(normalized_keys[current_key]["grade"]):
                normalized_keys[current_key] = student
    normalized = sorted(list(normalized_keys.values()), key=lambda s: s["name"])
    return normalized