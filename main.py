## Mini-ETL de Vendas Imobiliárias ##

### O objetivo é transformar dados brutos de vendas em um relatório de desempenho organizado
### Tem como foco principal consolidar conceitos fundamentais como variáveis, tipos de dados, condicionais (if/else) e formatação de strings.
### Preparando o terreno para o uso de ferramentas mais avançadas como o Pandas.

nome_corretor = str(input("Por favor, informe o nome do corretor: ")).upper().strip()
valor_venda = float(input("\nAgora me informe o valor da venda: "))
print("\nAviso: Digite o Mẽs por numerico por favor! ")
mes_venda = int(input("Agora me diga o mês da venda:"))

#Calculo comissao
if valor_venda >= 500000:
    comissao = valor_venda * 0.05
else:
    comissao = valor_venda * 0.03

#Status e feedback
if comissao > 20000:
    status = "ELITE"
    feedback = "PARABÉNS!!!!"
else:
    status = "PADRÃO"
    feedback = "Boa Sorte na próxima vez!!!"

#Resultado
print(f"""
{'-'*30}
RELATÓRIO DE DESEMPENHO - MÊS {mes_venda}
{'-'*30}
Corretor:      {nome_corretor}
Venda Total:   R$ {valor_venda:,.2f}
Comissão:      R$ {comissao:,.2f}
Status:        {status}
{'-'*30}
{feedback}
""")
