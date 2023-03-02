num_list = []

i = 0
maiornum = 0
menornum = 100000000
while i < 5:
    num = int(input("Digite um número: "))
    num_list.append(num)
    i += 1
    if num > maiornum:
        maiornum = num
    if num < menornum:
        menornum = num
print(f"Os números digitados são: {num_list}")
print(f"O maior número é: {maiornum}")
print(f"O menor número é: {menornum}")