from validate import validate_positive
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    weight = validate_positive(weight_kg, "Маса")
    height = validate_positive(height_m, "Зріст")

    return weight / height**2
