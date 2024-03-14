nota1 = float(input("Digite a sua primeira nota\n"))
nota2 = float(input("Digite a sua segunda nota\n"))
nota3 = float(input("Digite a sua terceira nota\n"))

calculo = (nota1 + nota2 + nota3) /3

if nota1< 0 or nota1> 10 or nota2< 0 or nota2> 10 or nota3< 0 or nota3> 10:
    print("Digite uma nota valida, entre 0 e 10")
elif calculo >=8:
    print("A sua média é: ", calculo, "e você está aprovado!!")
else:
    print("A sua média é: ", calculo, "e você está reprovado!!")