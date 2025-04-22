def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years

def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    try:
        return time_seconds / (1 - speed_of_light_fraction)
    except ZeroDivisionError:
        return float('inf')

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть числове значення.")

def main():
    print(" Калькулятор 'Таємниці Всесвіту' ")

    while True:
        print("\nОберіть розрахунок:")
        print("1 - Космічна відстань")
        print("2 - Спрощена гравітація")
        print("3 - Наближення сповільнення часу")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            v = get_float_input("Введіть частку швидкості світла (від 0 до 1): ")
            t = get_float_input("Введіть час у роках: ")
            result = calculate_cosmic_distance(v, t)
            print(f" Космічна відстань: {result} світлових років.")

        elif choice == "2":
            m1 = get_float_input("Введіть масу першого об'єкта: ")
            m2 = get_float_input("Введіть масу другого об'єкта: ")
            cf = input("Введіть космічний фактор (натисніть Enter для 1.0): ")
            cf = float(cf) if cf else 1.0
            result = calculate_simplified_gravity(m1, m2, cf)
            print(f" Спрощена гравітаційна взаємодія: {result}")

        elif choice == "3":
            v = get_float_input("Введіть частку швидкості світла (від 0 до 1, але не 1): ")
            t = get_float_input("Введіть час у секундах: ")
            result = calculate_time_dilation_approximation(v, t)
            print(f" Наближення сповільнення часу: {result} секунд.")

        elif choice == "0":
            print("Дякуємо за використання калькулятора. До нових зустрічей у Всесвіті! ")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
