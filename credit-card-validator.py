def validator(card_number):
    digits = [int(d) for d in str(card_number)]
    for i in range(-2, -len(digits)-1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)
    return total % 10 == 0
def main():
    card_number = input("Insira um número de cartão de crédito: ")
    
    if validator(card_number):
        print("O número do cartão de crédito é válido.")
    else:
        print("O número do cartão de crédito é inválido.")

if __name__ == "__main__":
    main()