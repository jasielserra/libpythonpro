from unittest.mock import Mock

import pytest

from  libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario

@pytest.mark.parametrize(
                'usuarios',
                [
                    [
                        Usuario(nome='Jasiel', email='jasiel_serra@hotmail.com'),
                        Usuario(nome='Luciano', email='jasiel_serra@hotmail.com')
                    ],
                    [
                        Usuario(nome='Luciano', email='jasiel_serra@hotmail.com')
                    ]
                ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jasiel_serra@hotmail.com',
        'Utilizando lib enviador de emails',
        'Confira o funcionamento destas funcionalidades'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jasiel', email='jasielserra@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jasiel_serra@hotmail.com',
        'Utilizando lib enviador de emails',
        'Confira o funcionamento destas funcionalidades'
    )
    enviador.enviar.assert_called_once_with(
        'jasiel_serra@hotmail.com',
        'jasielserra@gmail.com',
        'Utilizando lib enviador de emails',
        'Confira o funcionamento destas funcionalidades'
    )