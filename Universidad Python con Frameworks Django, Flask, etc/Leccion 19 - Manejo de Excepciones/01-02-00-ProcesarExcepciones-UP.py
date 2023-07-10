resultado = None
a = '10'
b = 0
try:
    resultado = a/b
except Exception as e:
    print(f'Ocurrió un error: {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')

#Tener en cuenta que el error TypeError, es una class
#dentro de python la cual menciona que hay un error de digitación