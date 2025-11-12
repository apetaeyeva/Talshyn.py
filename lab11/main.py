import logging
from datetime import datetime
import os

logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - ERROR - %(message)s")

def calculate_final_amount(principal, rate, years, n=12):
    if principal <= 0 or rate <= 0 or years <= 0:
        raise ValueError("Все значения должны быть положительными.")
    amount = principal * (1 + rate / (100 * n)) ** (n * years)
    return round(amount, 2)

def save_result(principal, rate, years, result):
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(f"Вклад: {principal} тг\nСтавка: {rate}%\nСрок: {years} лет\nИтоговая сумма: {result} тг\n")
    print("\n✅ Результаты сохранены в файл result.txt\n")

def show_results():
    if os.path.exists("result.txt"):
        print("\n📄 Содержимое result.txt:\n")
        with open("result.txt", "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("\n⚠️ Файл result.txt ещё не создан.\n")

def show_errors():
    if os.path.exists("errors.log"):
        print("\n🚨 Содержимое errors.log:\n")
        with open("errors.log", "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("\n✅ Ошибок пока нет!\n")

def main_menu():
    while True:
        print("========== 💰 ФИНАНСОВЫЙ КАЛЬКУЛЯТОР ==========")
        print("1. Выполнить расчёт")
        print("2. Показать результаты (result.txt)")
        print("3. Показать ошибки (errors.log)")
        print("4. Выход")
        print("===============================================")
        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            try:
                principal = float(input("Введите сумму вклада (тг): "))
                rate = float(input("Введите годовую процентную ставку (%): "))
                years = float(input("Введите срок вклада (в годах): "))
                result = calculate_final_amount(principal, rate, years)
                print(f"\n💵 Итоговая сумма через {years} лет: {result} тенге")
                save_result(principal, rate, years, result)
            except ValueError:
                print("\n⚠️ Ошибка: введены некорректные данные.\n")
                logging.error("Некорректный ввод данных.")
            except Exception as e:
                print(f"\n❌ Произошла ошибка: {e}\n")
                logging.error(str(e))
        elif choice == "2":
            show_results()
        elif choice == "3":
            show_errors()
        elif choice == "4":
            print("\n👋 Программа завершена.\n")
            break
        else:
            print("\n⚠️ Неверный выбор. Введите число от 1 до 4.\n")

if __name__ == "__main__":
    main_menu()