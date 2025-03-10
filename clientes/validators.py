import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return CPF.validate(numero_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o número de celular é válido ()"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular)
    return resposta
        

       
        