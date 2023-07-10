resultado = None
a = 10
b = 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
#la Exception es el padre de todas las classes de exceptiones en python
#es decir que es de mayor jerarquia y no es necesario usarlo.
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')