

from pathlib import (
    Path
)

from src.include import (
    index_html,
    view_html
)


# index_html = {
#     "pathIndex": f"{Path(__file__).parent.parent.parent}/site-inventario",
#     "arqIndex": "index.html"
# }

# view_html = {
#     "pathView": f"{Path(__file__).parent.parent.parent}/site-inventario/view"
# }


def gerar_pagina_index(itens_inventario: dict, model_index: dict) -> str:
    """
    Gerar a página de índice baseado no json de itens

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

    return pagina_index


def criar_arquivo_index(pagina_index: str) -> bool:
    """
    Cria o arquivo index com a página de índice baseado no json de itens

    return: retorna true se criar o arquivo
    """
        
    arquivo_html = Path(f"{index_html['pathIndex']}/{index_html['arqIndex']}")

    return criar_arquivo_html(arquivo_html, pagina_index)


def gerar_views(itens_inventario: dict, model_view: dict) -> bool:
    """
    Gerar os arquivos das views em html

    return: 
    """
    erro = 0

    # Carregar as partes dos arquivos para serem usados como modelo

    arq_page_view = open(f'{model_view["path"]}/{model_view["filePage"]}', mode="r", encoding="utf-8")
    page_view_model = arq_page_view.read()
    arq_page_view.close()

    arq_item_view = open(f'{model_view["path"]}/{model_view["fileItem"]}', mode="r", encoding="utf-8")
    item_view_model = arq_item_view.read()
    arq_item_view.close()

    # Pega cada item de grupo do inventário
    for item_inventario in itens_inventario.items():

        item_view: str = gerar_lista_view(item_inventario[1]['nomePasta'],
                                          item_inventario[1]['itens'], 
                                          item_view_model
                                         )

        pagina_view: str = gerar_pagina_view(item_inventario[1]['titulo'],
                                             item_view, 
                                             page_view_model
                                            )

        nome_arquivo: str = item_inventario[1]['nomePasta']

        exec_ok = criar_arquivo_view(nome_arquivo, pagina_view)

        if exec_ok:
            msg = f">> Criado com sucesso o arquivo: {nome_arquivo}.html"
        else:
            erro = erro + 1
            msg = f">> Problema na criação do arquivo: {nome_arquivo}.html"

        print(msg)

    if erro > 0:
        return False
    
    return True


def gerar_lista_view(nome_pasta: str, itens: list, item_view_html: str) -> str:
    """
    Gerar a lista dos view em html
    """

    itens_view: str = ""
    num_item: int = 1

    # Pega cada item 
    for item in itens:

        # print(item)

        path_imagem: str = item['pathImg']
        path_local_imagem: str = item['pathLocalArmazenado']

        path_imagem = path_imagem.replace("[[nomePasta]]",
                                           nome_pasta
                                        )
        
        path_local_imagem = path_local_imagem.replace("[[nomePasta]]",
                                                      nome_pasta
                                                    )

        item_view: str =  item_view_html.replace(
                                "[[href-img-item]]",
                                f"{path_imagem}/{item['arquivoImg']}" 
                            )

        item_view =  item_view.replace(
                            "[[descricao-item]]",
                            item['descricao']
                    )

        #  O .replace já muda todas das ocorrências

        # existe_num_id = item_view.find("[[num-local-item]]", 0)

        # # Atualiza todas as ocorrências de num-local-item
        # while (existe_num_id > 0):
            
        #     item_view =  item_view.replace(
        #                     "[[num-local-item]]",
        #                     str(num_item)
        #                 )

        #     existe_num_id = item_view.find("[[num-local-item]]", 0)

        item_view =  item_view.replace(
                        "[[num-local-item]]",
                        str(num_item)
                    )
        
        num_item = num_item + 1     # Adiciona mais um na contagem

        item_view =  item_view.replace(
                        "[[local-item]]",
                        item['localArmazenado']
                    )

        item_view =  item_view.replace(
                        "[[href-img-local]]",
                        f"{path_local_imagem}/{item['arquivoImgArmazenado']}"
                    )

        item_view =  item_view.replace(
                        "[[palavra-chave-item]]",
                        item['palavraChave']
                    )

        itens_view = itens_view + item_view

    # print(itens_view)

    return itens_view


def gerar_pagina_view(titulo: str, itens_html: str, page_view_html: str) -> str:
    """
    Gerar a página em html do arquivo das views

    """

    pagina_view: str = page_view_html.replace(
                            "[[item-grupo]]",
                            titulo
                        )

    pagina_view = pagina_view.replace(
                        "[[itens]]",
                        itens_html
                    )

    # print(pagina_view)

    return pagina_view


def criar_arquivo_view(nome_arquivo: str, pagina_view: str) -> bool:
    """
    Cria o arquivo view com os itens baseado no json de itens

    return: retorna true se criar o arquivo
    """
        
    arquivo_html = Path(f"{view_html['pathView']}/{nome_arquivo}.html")
    
    return criar_arquivo_html(arquivo_html, pagina_view)


def criar_arquivo_html(arquivo_html: str, conteudo_html: str) -> bool:
    """
    Cria o arquivo html

    return: retorna true se criar o arquivo
    """

    try:
        
        # print(arquivo_html)

        arq_view = open(arquivo_html, "w", encoding='utf-8')
        bytes = arq_view.write(conteudo_html)
        # print(bytes)
        arq_view.close()

        return True

    except Exception as e:

        return False

