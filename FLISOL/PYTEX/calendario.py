ano = 365
mes = 31
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
semana = ['Dom','Seg','Ter','Qua','Qui','Sex','Sab']
a=0
for i in meses:
    print(i)
    for day in range(1,mes+1):
        print(semana[0],day,sep='-')
	a=a+1
    