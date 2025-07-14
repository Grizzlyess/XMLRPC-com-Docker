from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import math
import random

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC',)


with SimpleXMLRPCServer(('0.0.0.0', 8000), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    print("Servidor XML-RPC iniciado na porta 8000...")

    def adicionar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y

    def multiplicar(x, y):
        return x * y

    def dividir(x, y):
        if y == 0:
            raise ValueError("Erro: divisão por zero não é permitida.")
        return x / y

    def raiz_quadrada(num):
        if num < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        return math.sqrt(num)

    def potencia(base, exp):
        return math.pow(base, exp)

    def modulo(x , y):
        if y == 0: 
            raise ValueError("Erro: divisão por zero não é permitida.")
        return x % y

    def ordenar(lista_numeros):
        try:
            numeros_validos = [float(n) for n in lista_numeros]
            return sorted(numeros_validos)
        except (ValueError, TypeError):
            raise ValueError("Entrada inválida. A função deve receber uma lista de números.")
        
    def adivinhe_numero(num):
        surpresa = random.randint(1,100000)
        if num <= 0:
            raise ValueError("O numero deve ser maior e diferente de 0")
        
        return surpresa

        
        


    server.register_function(adicionar, 'add')
    server.register_function(subtrair, 'sub')
    server.register_function(multiplicar, 'mult')
    server.register_function(dividir, 'div')
    server.register_function(raiz_quadrada, 'sqrt')
    server.register_function(potencia, 'pow')
    server.register_function(modulo, 'mod')
    server.register_function(ordenar, 'sort')
    server.register_function(adivinhe_numero,'adv')


    server.serve_forever()