"""
    Projeto Cadastro de itens pata visualização via navegador

    Autor: Edson Silva
    data: 08/23

"""

import json

from src.cadastro import (
    cadastrar_item
)


_ARQUIVO_ITENS_ = "src/itens/lista-itens.json"

def main():

    arquivo = open(_ARQUIVO_ITENS_, "r")

    itens = json.loads(arquivo.read())

    print(itens)
    print(type(itens))

    print(itens['conectores'])


# Executando a função

main()
