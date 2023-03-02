num_list = []

i = 0

while i < 5:
    num = int(input("Digite um número: "))
    num_list.append(num)
    i += 1

listord = num_list[:]
listord.sort()
menornum = listord[0]
maiornum = listord[-1]

posmaior = num_list.index(maiornum) + 1
posmenor = num_list.index(menornum) + 1

print(f"Os números digitados são: {num_list}")
print(f"O maior número é: {maiornum} na posição: {posmaior}")
print(f"O menor número é: {menornum} na posição: {posmenor}")

