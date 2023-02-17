class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('Teste de exception!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')