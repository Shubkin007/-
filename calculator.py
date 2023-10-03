def main():
    try:
        num1 = float(input("Введите первое число : "))
        operator = input("Введите арифметический оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно!")
                return
            else:
                result = num1 / num2
        else:
            print("Ошибка: Неверный оператор! Введите один из: +, -, *, /")
            return

        print(f"Результат: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Ошибка: Некорректный ввод. Пожалуйста, введите числа и арифметический оператор корректно.")

if __name__ == "__main__":
    main()
