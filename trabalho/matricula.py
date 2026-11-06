print("=🏋🏽🔥= CADASTRO DA ACADEMIA =💪🏼🎧=")
print("Para fazer a matricula na academia, precisamos que informe sua idade")
idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Matrícula não autorizada. A academia aceita alunos a partir dos 16 anos")
elif idade >= 16 and idade < 18:
    print("Sua idade exige autorização de um responsável para realizar a matrícula")
    autorizacao = input("Você possui autorização? (S/N): ")

    if autorizacao == "N":
        print("Matrícula pendente. Retorne com a autorização de um responsável")
    elif autorizacao == "S":
        print("Autorização confirmada! Apresente seu documento para concluir a matrícula")
    else:
        print("Opção inválida. Por favor, responda com S ou N!!")

else:
    print("Idade permitida! Sua matrícula pode ser realizada normalmente")
