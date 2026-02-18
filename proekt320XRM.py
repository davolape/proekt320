def funk320XRM(x):
    """Преобразовать заданное десятичное число в двоичную систему счисления."""
    if x < 0:
        return "-" + bin(abs(x))[2:]
    return bin(x)[2:]

if __name__ == "__main__":
    number = int(input("Введите десятичное число: "))
    print("Двоичное представление:", funk320XRM(number))