from scipy.stats import binom 

n = float (input ("N° de observações: ")) 

p = float (input ("Probabilidade de sucesso: ")) 

x = int (input ("Quantidades de sucessos: ")) 

pbi = binom.pmf (x, n, p)
pba = binom.cdf(x, n, p)

print ("Probabilidade binomial individual = ", format(pbi, ".4f"))
print ("Probabilidade binomial acumulada = ",  format(pba, ".4f"))
