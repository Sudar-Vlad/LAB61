from validate import validate_positive
def interpret_bmi(bmi: float) -> str:

    value = validate_positive(bmi, "ІМТ")

    if value < 18.5:
        return "Недостатня вага"
    if value < 25:
        return "Нормальна вага"
    if value < 30:
        return "Надмірна вага"

    return "Ожиріння"
