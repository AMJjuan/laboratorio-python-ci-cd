from calculadora import Calculator  # ← Importación CORRECTA

def main():
    calc = Calculator()
    print("=== CALCULADORA PYTHON ===")
    print(f"5 + 3 = {calc.sum(5, 3)}")

if __name__ == "__main__":
    main()