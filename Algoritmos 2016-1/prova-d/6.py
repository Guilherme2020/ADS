'''
   semantica
   sintaxe
   erro logico
'''


nome = str(input())
sal_fixo = float(input())
tot_vendas = float(input())
comisao = tot_vendas*0.15

total_receber = comisao+sal_fixo

print ("TOTAL = R$ %.2f"%total_receber)