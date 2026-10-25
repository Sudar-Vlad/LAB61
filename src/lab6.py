from bmi_calculator import calculate_bmi, interpret_bmi
from validate import cm_to_m, validate_positive

def main() -> None:
    """Отримати дані користувача та вивести ІМТ і його категорію."""
    init(autoreset=True)

    print("Калькулятор ІМТ для дорослих")
    print("Результат не є медичним діагнозом.\n")

    try:
        weight = validate_positive(
            input("Введіть масу тіла в кг: ").replace(",", "."),
            "Маса",
        )

        height_cm = validate_positive(
            input("Введіть зріст у см: ").replace(",", "."),
            "Зріст",
        )

        height_m = cm_to_m(height_cm)
        bmi = calculate_bmi(weight, height_m)
        category = interpret_bmi(bmi)


        print(f"\nВаш ІМТ: {bmi:.2f}")
        print( f"Категорія: {category}" )

    except ValueError as error:
        print(Fore.RED + f"Помилка: {error}")
if __name__ == "__main__":
    main()
