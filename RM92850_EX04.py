minutos = int(input("Digite a quantidade de minutos que a sua máquina exibe: "))
fatorial = 1
while minutos > 0:
    fatorial = fatorial * minutos
    minutos = minutos - 1
senha = "LIBERDADE" + str(fatorial)
print("A senha é: {}".format(senha))