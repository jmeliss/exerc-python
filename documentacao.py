#Documentando funcoes com docstring
#podemos ter acesso a uma documentacao de uma funcao em python assim:
#.__doc__  ou utilizando a funcao help()

def dizOi():
    return 'Oi!'

print(dizOi())
    """uma funcao simpples que retorna a string 'oi'"""

#quando se digita tres aspas duplas dentro da funcao e da enter (NO PYCHARM)
def exponecial(numero, exponente=2):
    """
    FUNCAO QUE RETORNA POR PADRAO O QUADRADO DO NUMERO OU NUMERO ELEVADO A POTENCIA POR PADRAO 2.
    ;param numero: numero que desejamos gerar o exponencial
    ;param potencia: potencia que queremos gerar o exponencial.
    ;return: retorna o exponencial de numero por potencia
    """
    return numero ** potencia


