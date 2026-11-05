print("Para realizar a matrícula precisamos que identifique sua idade")
idade = int(input("Digite sua idade: "))

if idade <16:
    print("Pessoas menores que 16 anos não podem realizar a matrícula")
elif idade >= 16 and idade < 18:
    print("Pessoas entre 16 e 17 anos precisam de autorização")
else:
    print("Pessoas com 18 anos ou mais podem realizar matrícula normalmente")