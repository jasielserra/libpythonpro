import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br','jasiel_serra@hotmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'jasiel_serra@gmail.com',
        'Testando feature enviador de email',
        'Primeira Turma Guido Van Rossum aberta',
        )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','jasiel']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'jasiel_serra@gmail.com',
            'Testando feature enviador de email',
            'Primeira Turma Guido Van Rossum aberta',
        )



