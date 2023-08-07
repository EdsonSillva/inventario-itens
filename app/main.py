"""
    Projeto Cadastro de itens pata visualização via navegador

    Autor: Edson Silva
    data: 08/23

"""

import json

from src.geracao_site import (
    criar_index
)


_ARQUIVO_ITENS_ = "app/src/itens/lista-itens.json"

index_model = {
    "path": "app/src/model/index",
    "filePage": "01_page_index.html",
    "fileItem": "02_item_index.html"
}

view_model = {
    "Path": "app/src/model/view",
    "filePage": "01_page_view.html",
    "fileItem": "02_item_view.html"
}

def main():

    arquivo_itens = open(_ARQUIVO_ITENS_, mode="r", encoding="utf-8" )

    itens_inventario = json.loads(arquivo_itens.read())
    arquivo_itens.close()

    print(itens_inventario)
    print(type(itens_inventario))

    # Criar o index
    
    ok = criar_index(itens_inventario, index_model)

    # Criar os arquivos dos itens





# Executando a função

main()
