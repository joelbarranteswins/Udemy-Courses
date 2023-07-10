resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')
else: #se ejecuta cuando no sucedio ninguna exception
    print('No se arrojó ninguna excepción')
finally: #siempre se ejecuta haya o no una exception
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')