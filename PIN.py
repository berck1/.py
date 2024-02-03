var = int(input('Qual é o PIN? '))

while var != 11:
   var = int(input('Tentar Novamente. '))

if var == 11:
    print('Correto.')
