

def criar_arquivo_index(itens_inventario: dict, model_index: dict) -> str:
    pass


def gerar_pagina_index(itens_inventario: dict, model_index: dict) -> str:
    """
    Ciar o arquivo de índice baseado no json de itens

    return: retorna a página index pronta para ser gerado o arquivo
    """

    # Carregar as partes dos arquivos para serem usados como modelo

    arq_page_index = open(f'{model_index["path"]}/{model_index["filePage"]}', mode="r", encoding="utf-8")
    page_index_model = arq_page_index.read()
    arq_page_index.close()

    arq_item_index = open(f'{model_index["path"]}/{model_index["fileItem"]}', mode="r", encoding="utf-8")
    item_index_model = arq_item_index.read()
    arq_item_index.close()

    item_final: str = ""

    # Pega cada item de grupo do inventário e cria os links para a página index
    for item_inventario in itens_inventario.items():

        item_href: str =  item_index_model.replace(
                                "[[href-item]]",
                                f"view/{item_inventario[0]}.html" 
                           )

        item_grupo: str =  item_href.replace(
                                "[[item-grupo]]",
                                item_inventario[1]['titulo']
                           )

        item_completo: str =  item_grupo.replace(
                                "[[descricao-item-grupo]]",
                                item_inventario[1]['descricaoGrupo']
                           )

        item_final = item_final + item_completo


    pagina_index: str = page_index_model.replace(
                                "[[itens-inventario]]",
                                item_final
                                )

    print("\n\n")
    print("-"*40)
    print(pagina_index)

    return pagina_index



