def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero"

while True:
    print("\nWybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjdź")

    wybor = input("Wprowadź numer operacji (1/2/3/4/5): ")

    if wybor == '5':
        print("Wyłączanie")
        break

    try:
        liczba1 = float(input("Wprowadź pierwszą liczbę: "))
        liczba2 = float(input("Wprowadź drugą liczbę: "))
    except ValueError:
        print("Wprowadź poprawne liczby!")
        continue

    if wybor == '1':
        print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print(liczba1, "/", liczba2, "=", dzielenie(liczba1, liczba2))
    else:
        print("Nieprawidłowy wybór. Wybierz ponownie.")
