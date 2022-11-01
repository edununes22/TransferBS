seg = int(input("Digite a quantidade de alunos que votaram na segunda-feira: "))
ter = int(input("Digite a quantidade de alunos que votaram na terça-feira: "))
qua = int(input("Digite a quantidade de alunos que votaram na quarta-feira: "))
qui = int(input("Digite a quantidade de alunos que votaram na quinta-feita: "))
sex = int(input("Digite a quantidade de alunos que votaram na sexta-feira: "))

if seg > ter and seg > qua and seg > qui and seg > sex:
    print("O dia escolhido foi segunda-feira! A votação ficou da seguinte forma:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\nQuinta-feira: {} votos\nSexta-feira: {} votos"
    .format(seg, ter, qua, qui, sex))
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("O dia escolhido foi terça-feira! A votação ficou da seguinte forma:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\nQuinta-feira: {} votos\nSexta-feira: {} votos"
    .format(seg, ter, qua, qui, sex))
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("O dia escolhido foi quarta-feira! A votação ficou da seguinte forma:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\nQuinta-feira: {} votos\nSexta-feira: {} votos"
    .format(seg, ter, qua, qui, sex))
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("O dia escolhido foi quinta-feira! A votação ficou da seguinte forma:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\nQuinta-feira: {} votos\nSexta-feira: {} votos"
    .format(seg, ter, qua, qui, sex))
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("O dia escolhido foi sexta-feira! A votação ficou da seguinte forma:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\nQuinta-feira: {} votos\nSexta-feira: {} votos"
    .format(seg, ter, qua, qui, sex))
else: 
    print("Empate! A votação ficou da seguinte forma:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\nQuinta-feira: {} votos\nSexta-feira: {} votos"
    .format(seg, ter, qua, qui, sex))
    