"""
    Projeto Cadastro de itens para visualização via navegador

    Autor: Edson Silva
    data: 08/23

"""

import json

from src.geracao_site import (
    gerar_pagina_index,
    criar_arquivo_index,
    gerar_views,
)

from src.include import (
    _ARQUIVO_ITENS_,
    index_model,
    view_model

)

# _ARQUIVO_ITENS_ = "app/src/itens/lista-itens.json"

# index_model = {
#     "path": "app/src/model/index",
#     "filePage": "01_page_index.html",
#     "fileItem": "02_item_index.html"
# }

# view_model = {
#     "path": "app/src/model/view",
#     "filePage": "01_page_view.html",
#     "fileItem": "02_item_view.html"
# }

def main():

    arquivo_itens = open(_ARQUIVO_ITENS_, mode="r", encoding="utf-8" )

    itens_inventario = json.loads(arquivo_itens.read())
    arquivo_itens.close()

    # print(itens_inventario)
    # print(type(itens_inventario))

    # Gerar a página index - Ok
    
    pagina_index = gerar_pagina_index(itens_inventario, index_model)

    # codificar criar_arquivo_index()

    exec_ok = criar_arquivo_index(pagina_index)

    # TODO: Criar os arquivos dos itens

    if exec_ok:

        exec_ok = gerar_views(itens_inventario, view_model)

        if exec_ok:
            print("Criação do site com sucesso")
    


# Executar a ciação do site Inventário de Itens da Familia Sillva

print("Iniciando a criação do site invetário de itens da Família Sillva ...")

main()
