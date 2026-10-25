import math


def validate_positive(value: float, name: str = "Значення") -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} має бути числом, а не bool.")

    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(f"{name} має бути числом.") from error

    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{name} має бути скінченним числом більше нуля.")
    return number


def cm_to_m(height_cm: float) -> float:
    return validate_positive(height_cm, "Зріст") / 100