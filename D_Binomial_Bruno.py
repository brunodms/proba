from scipy.stats import binom

n = float(input("N° de observações: "))

p = float(input("Probabilidade de sucesso: "))

x = int(input("Quantidades de sucessos: "))

p_x = binom.pmf(x, n, p)
 
print("P(x) = ", p_x)
