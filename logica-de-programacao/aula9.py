#Lista como parametros numa funcao
# Calcula aritmetica das notas de 15 alunos
# determinar o numero de alunos que tiveram nota maior  a media calculada
def media(n):
    print(sum(n)/len(n))

notas=[]
for x in range(15):
    notas.append(float(input("Digite a nota: ")))

media(notas)
