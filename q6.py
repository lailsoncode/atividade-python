nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media < 50:
    print("Aluno reprovado")
elif media >= 70:
    print("Aluno aprovado")
else:
    print("Aluno em recuperação")