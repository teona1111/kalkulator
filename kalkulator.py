def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def zmnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        raise ValueError("Deljenje z nic ni dovoljeno.")
    return a / b

def potenciraj(a, b):
    return a ** b

if __name__ == "__main__":
    print("Preprost kalkulator")
    x = float(input("Vnesi prvo stevilo: "))
    y = float(input("Vnesi drugo stevilko: "))
    op = input("Izberi operacijo (+, -, *, /): ")

    if op == "+":
        print("Rezultat:", sestej(x, y))
    elif op == "-":
        print("Rezultat:", odstej(x, y))
    elif op == "*":
        print("Rezultat:", zmnozi(x, y))
    elif op == "/":
        print("Rezultat:", deli(x, y))
    else:
        print("Neveljavna operacija.")
