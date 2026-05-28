"""
Uma função é um bloco de código que realiza uma tarefa específica.

define uma vez -> chama quando quiser -> reaproveita sempre


"""
#sintaxe
def nome_da_funcao(parametro):
    #bloco de código
    #instruções usando os parâmetros
    return resultado #opcional

#exemplo
def somar(a, b):
    resultado = a + b
    return resultado

#chamando a função
soma = somar(3, 5) #soma recebe 8
print(soma)

