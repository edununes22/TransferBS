cont_par = 2
cont_impar = 1
notas_par = 0
notas_impar = 0 
while cont_impar <=50:
    print  ("Você está digitando as notas dos alunos ímpares. Por favor, insira a nota do aluno {}: ".format(cont_impar))
    nota = float(input(" "))
    notas_impar = notas_impar + nota
    cont_impar = cont_impar + 2

while cont_par <=50:
    print ("Você está digitando as notas dos alunos pares. Por favor, insira a nota do aluno {}: ".format(cont_par))
    nota = float(input(" "))
    notas_par = notas_par + nota
    cont_par = cont_par + 2

media_impar = notas_impar / 25
media_par = notas_par / 25
print("Média dos alunos ímpares: {}".format(media_impar))
print("Média dos alunos pares: {}".format(media_par))

if media_impar > media_par:
    print("Os alunos ímpares obtiveram a maior média de notas!")
else: 
    print("Os alunos pares obtiveram a maior média de notas!")
