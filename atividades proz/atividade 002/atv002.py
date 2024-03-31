import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                idade = calcular_idade(ano_nascimento)
                print("\nNome:", nome_completo)
                print("Idade:", idade, "anos")
                break
            else:
                print("O ano de nascimento deve estar entre 1922 e 2021. Tente novamente.\n")
        except ValueError:
            print("Por favor, digite um ano válido (número inteiro).\n")

if __name__ == "__main__":
    main()
