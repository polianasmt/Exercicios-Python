import random
import sys

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contagem_regressiva_1 = 10
contagem_regressiva_2 = 11

resultados_1 = 0
resultados_2 = 0

for digito in nove_digitos:
    resultados_1 += int(digito) * contagem_regressiva_1
    contagem_regressiva_1 -= 1
    
digito_1 = (resultados_1 * 10) % 11
comparacao_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

for digito_2 in dez_digitos:
    resultados_2 += int(digito_2) * contagem_regressiva_2
    contagem_regressiva_2 -= 1

digito_2 = (resultados_2 * 10) % 11
comparacao_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

#print(comparacao_1, comparacao_2)

print(cpf_gerado)
# if nove_digitos == cpf_gerado:
#     print("O cpf '{}' é valido.".format(nove_digitos))
# else:
#     print("O cpf '{}' não é valido.".format(nove_digitos))