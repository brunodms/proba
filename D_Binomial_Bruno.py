from scipy.stats import binom

while True:
  print("Menu:\n 1 - Probabilidade Binomial Individual\n 2 - Probabilidade Binomial Acumulada\n 0 - Sair do programa")
  
  tp = int (input("Tipo de operação: "))

  if (tp == 0 or tp > 2):
    print("Encerrando programa...")
    break

  n = int (input ("Número de Observações(Inteiro): ")) 

  p = float (input ("Probabilidade de Sucesso(%): ")) 

  x = int (input ("Número de Sucessos(Inteiro): "))

  p = p / 100

  if (tp == 1):
    pbi = binom.pmf (x, n, p)
    print (f"Probabilidade Binomial Individual = {pbi:.2%}")

  elif (tp == 2):
    pba = binom.cdf(x, n, p)
    print (f"Probabilidade Binomial Acumulada = {pba:.2%}")
