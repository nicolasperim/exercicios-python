def validar_senha(senha_digitada):
    senha_cadastrada = "python123"
    return senha_digitada == senha_cadastrada

for i in range(2, -1, -1):  
    senha = input("Digite a senha: ")

    if validar_senha(senha):
        print("Acesso concedido!")
        break
    else:
        print(f"SENHA INCORRETA! Restam {i} tentativas.")
else:
    print("Conta bloqueada")