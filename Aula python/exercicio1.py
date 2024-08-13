# nome = "Igor"
# idade = 16
# Altura = 1.60
# casado = False
 
# print("nome: " + nome+", idade: "+str(idade))
# print("Altura: "+str(Altura)+" Casado: "+str (casado))

# print("Ola {}".format(nome))
# print("Ola",nome)
# print("Ola %s" % (nome))
# print(f"oLA {nome}")I

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

if (email == "Igor" and senha == "Massa"):
    print("Acesso permitido")
    opcao = input("1-saque 2- Depósito 3-Pix")
    match opcao:
        case 1:
            saque = input("Informar o valor do saque: ")
        case 2:
            dep = input("Informe o valor do deposito: ")
        case 3:
                    pix = input("Informae o calor do pix: ")
else:
    print("Acesso negado")