

from pathlib import (
    Path
)

import os

from src.include import (
    index_html,
    view_html,
    imagem_model,
    retorno_path_enum,
    model_enum
)

from src.suporte import (
    get_model
)


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
                                "[[nome-item-grupo]]",
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

    # path_file_page = f'{model_view["path"]}/{model_view["filePage"]}'
    # arq_page_view = open(path_file_page, mode="r", encoding="utf-8")
    # page_view_model = arq_page_view.read()
    # arq_page_view.close()

    # path_file_view = f'{model_view["path"]}/{model_view["fileItem"]}'
    # arq_item_view = open(path_file_view, mode="r", encoding="utf-8")
    # item_view_model = arq_item_view.read()
    # arq_item_view.close()

    page_view_model = get_model(f'{model_view["path"]}', f'{model_view["filePage"]}')

    itens_html_model: dict = {

        "item_view_model": get_model(f'{model_view["path"]}', f'{model_view["fileItem"]}'),

        "html_img_unica_model": get_model(f'{imagem_model["imagemUnica"]["path"]}',
                                        f'{imagem_model["imagemUnica"]["fileHtml"]}'
                                       ),

        "html_img_carrossel_model": get_model(f'{imagem_model["ImagemCarrossel"]["htmlItem"]["path"]}',
                                            f'{imagem_model["ImagemCarrossel"]["htmlItem"]["fileHtml"]}'
                                           ),

        "html_img_carrossel_tag_li_model": get_model(f'{imagem_model["ImagemCarrossel"]["htmlTagList"]["path"]}',
                                                   f'{imagem_model["ImagemCarrossel"]["htmlTagList"]["fileHtml"]}'
                                                  ),

        "html_img_carrossel_div_model": get_model(f'{imagem_model["ImagemCarrossel"]["htmlItemDiv"]["path"]}',
                                                f'{imagem_model["ImagemCarrossel"]["htmlItemDiv"]["fileHtml"]}'
                                              ),

        "html_img_carrossel_script_model": get_model(f'{imagem_model["ImagemCarrossel"]["htmlScript"]["path"]}',
                                                   f'{imagem_model["ImagemCarrossel"]["htmlScript"]["fileHtml"]}'
                                                  )
    }

    # item_view_model = get_model(f'{model_view["path"]}', f'{model_view["fileItem"]}')


    # Abrir Imagem única
    # Abrir carrossel imagem, tag_li, item, script
    # imagem_unica_model = get_model(f'{imagem_model["imagemUnica"]["path"]}',
    #                                f'{imagem_model["imagemUnica"]["fileHtml"]}'
    #                                )
    # imagem_carrossel_model = get_model(f'{imagem_model["ImagemCarrossel"]["htmlItem"]["path"]}',
    #                                    f'{imagem_model["ImagemCarrossel"]["htmlItem"]["fileHtml"]}'
    #                                   )
    # imagem_carrossel_tag_li_model = get_model(f'{imagem_model["ImagemCarrossel"]["htmlTagList"]["path"]}',
    #                                           f'{imagem_model["ImagemCarrossel"]["htmlTagList"]["fileHtml"]}'
    #                                          )
    # imagem_carrossel_div_model = get_model(f'{imagem_model["ImagemCarrossel"]["htmlItemDiv"]["path"]}',
    #                                        f'{imagem_model["ImagemCarrossel"]["htmlItemDiv"]["fileHtml"]}'
    #                                       )
    # imagem_carrossel_script_model = get_model(f'{imagem_model["ImagemCarrossel"]["htmlScript"]["path"]}',
    #                                           f'{imagem_model["ImagemCarrossel"]["htmlScript"]["fileHtml"]}'
    #                                          )
    # arquivos: list = get_arquivos(f'{model_view["path"]}')

    # Pega cada item de grupo do inventário
    for item_inventario in itens_inventario.items():

        item_view: str = ""
        script_carrossel: bool = False

        qtde_carrossel, item_view = gerar_lista_view(item_inventario[1]['nomePasta'],
                                                       item_inventario[1]['itens'], 
                                                       itens_html_model
                                                      )

        pagina_view: str = gerar_pagina_view(item_inventario[1]['titulo'],
                                             item_view, 
                                             page_view_model,
                                             qtde_carrossel
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


def gerar_lista_view(nome_pasta: str, itens: list, itens_model_html: dict) -> tuple[bool, str]:
    """
    Gerar a lista dos view em html
    """

    itens_view: str = itens_model_html['item_view_model']
    num_item: int = 1
    num_carrossel: int = 0              # contador para cada carrossel

    # Pega cada item 
    for item in itens:

        # print(item)

        item_view: str = ""

        path_imagem: str = item['pathImg']
        path_local_imagem: str = item['pathLocalArmazenado']

        path_imagem = path_imagem.replace("[[nomePasta]]",
                                           nome_pasta
                                        )
        
        path_local_imagem = path_local_imagem.replace("[[nomePasta]]",
                                                      nome_pasta
                                                    )

        if item['pathImgExtra']['ativa'] == False:

            # tratar imagem única

            item_view = monta_tag_img_unica(item_view,
                                            itens_model_html,
                                            f"{path_imagem}/{item['arquivoImg']}"
                                           )

            # img_unica_html = itens_model_html['html_img_unica_model']
            # img_unica_html =  img_unica_html.replace(
            #                         "[[href-img-item]]",
            #                         f"{path_imagem}/{item['arquivoImg']}" 
            #                     )
            # item_view =  item_view.replace(
            #                         "[[item-imagem]]",
            #                         img_unica_html 
            #                     )

        else:

            html_carrossel = monta_tag_carrossel(nome_pasta,
                                                 num_carrossel,
                                                 item,
                                                 itens_model_html
                                                )

            item_view =  item_view.replace(
                                    "[[item-imagem]]",
                                    html_carrossel 
                                )

            num_carrossel = num_carrossel + 1

        item_view =  item_view.replace(
                            "[[descricao-item]]",
                            item['descricao']
                    )

        #  O .replace já muda todas das ocorrências dentro da string

        # existe_num_id = item_view.find("[[num-local-item]]", 0)
        
        # Atualiza todas as ocorrências de num-local-item
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

    return num_carrossel, itens_view


def monta_tag_img_unica(item_view: str, itens_model_html: dict, pathArq: str ) -> str:

    img_unica_html = itens_model_html['html_img_unica_modelvitor']

    img_unica_html =  img_unica_html.replace("[[href-img-item]]",
                                             pathArq 
                                            )
    
    return  item_view.replace(
                "[[item-imagem]]",
                img_unica_html 
            )


def monta_tag_carrossel(nome_pasta: str, num_carrossel: int, item: dict, itens_model_html: dict) -> str:

    num_slide: int = 0          # contador para cada item do carrossel

    tags_li: str = ""
    tags_div: str = ""
    tag_carrossel: str = ""

    pathImagens: str = item['pathImgExtra']['path']
    pathImagens = pathImagens.replace("[[nomePasta]]",
                                        nome_pasta
                                     )

    arquivos_imagem: list = get_arquivos(pathImagens)

    for arq in arquivos_imagem:

        # Criando a tag li e div
        tag_li: str = itens_model_html['imagem_carrossel_tag_li_model']
        tag_div: str = itens_model_html['html_img_carrossel_tag_li_model']

        tag_li =  tag_li.replace(
                        "[[num-carrossel]]",
                        num_carrossel
                    )

        tag_li =  tag_li.replace(
                        "[[num-item-li]]",
                        num_slide
                    )

        class_active: str = ""
        active: str = ""

        if num_slide == 0:

            class_active = 'class="active"'
            active = 'active'

        tag_li =  tag_li.replace(
                        "[[class-active-item]]",
                        class_active
                    )

        tag_div =  tag_div.replace(
                        "[[active-item]]",
                        active
                    )

        tag_div=  tag_div.replace(
                        "[[href-img-item]]",
                        f"{pathImagens}/{arq}"
                    )

        tags_li = tags_li + tag_li
        tags_div = tags_div + tag_div

        num_slide = num_slide + 1

    tag_carrossel = itens_model_html['html_img_carrossel_model']

    tag_carrossel =  tag_carrossel.replace(
                    "[[num-carrossel]]",
                    num_carrossel
                )

    tag_carrossel =  tag_carrossel.replace(
                    "[[list-carroussel]]",
                    tags_li
                )

    tag_carrossel =  tag_carrossel.replace(
                    "[[item-carroussel]]",
                    tags_div
                )

    return tag_carrossel


def gerar_pagina_view(titulo: str, itens_html: str, page_view_html: str, itens_model_html: dict, qtde_carrossel: int) -> str:
    """
    Gerar a página em html do arquivo das views

    """

    itens_view: str = itens_model_html['item_view_model']

    pagina_view: str = page_view_html.replace(
                            "[[nome-item-grupo]]",
                            titulo
                        )

    pagina_view = pagina_view.replace(
                        "[[itens]]",
                        itens_html
                    )

    if qtde_carrossel > 0:

        tag_script = itens_model_html['html_img_carrossel_script_model']

        tag_script = tag_script.replace(
                            "[[qtdeCarrossel]]",
                            qtde_carrossel
                        )

        pagina_view =  pagina_view.replace(
                        "[[script-carrossel-imagem]]",
                        tag_script
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


def get_arquivos(path: str) -> list:

    arquivos = []

    itens_dir = os.listdir(path)

    for item in itens_dir:
        if Path(f'{path}/{item}').is_file():
            arquivos.append(item)

    return arquivos


def get_FAT(path: str, tipo: retorno_path_enum = retorno_path_enum.arquivo) -> list:

    retorno = []

    for dir, sub_pasta, arq in os.walk(path):
        if tipo == retorno_path_enum.arquivo:
            retorno.append(arq)
        elif tipo == retorno_path_enum.diretorio:
            retorno.append(dir)
        elif tipo == retorno_path_enum.subpasta:
            retorno.append(sub_pasta)
        else:
            retorno.append(arq)

    return retorno







# def gerar_lista_view(nome_pasta: str, itens: list, item_view_html: str) -> str:
#     """
#     Gerar a lista dos view em html
#     """

#     itens_view: str = ""
#     num_item: int = 1

#     # Pega cada item 
#     for item in itens:

#         # print(item)

#         path_imagem: str = item['pathImg']
#         path_local_imagem: str = item['pathLocalArmazenado']

#         path_imagem = path_imagem.replace("[[nomePasta]]",
#                                            nome_pasta
#                                         )
        
#         path_local_imagem = path_local_imagem.replace("[[nomePasta]]",
#                                                       nome_pasta
#                                                     )

#         if item['pathImgExtra']['ativa'] == False:

#             # tratar imagem única

#             img_unica = 

#         else:

#             # tratar carrossel

#             pass

#         # item_view: str =  item_view_html.replace(
#         #                         "[[href-img-item]]",
#         #                         f"{path_imagem}/{item['arquivoImg']}" 
#         #                     )

#         item_view =  item_view.replace(
#                             "[[descricao-item]]",
#                             item['descricao']
#                     )

#         #  O .replace já muda todas das ocorrências

#         # existe_num_id = item_view.find("[[num-local-item]]", 0)

#         # # Atualiza todas as ocorrências de num-local-item
#         # while (existe_num_id > 0):
            
#         #     item_view =  item_view.replace(
#         #                     "[[num-local-item]]",
#         #                     str(num_item)
#         #                 )

#         #     existe_num_id = item_view.find("[[num-local-item]]", 0)

#         item_view =  item_view.replace(
#                         "[[num-local-item]]",
#                         str(num_item)
#                     )
        
#         num_item = num_item + 1     # Adiciona mais um na contagem

#         item_view =  item_view.replace(
#                         "[[local-item]]",
#                         item['localArmazenado']
#                     )

#         item_view =  item_view.replace(
#                         "[[href-img-local]]",
#                         f"{path_local_imagem}/{item['arquivoImgArmazenado']}"
#                     )

#         item_view =  item_view.replace(
#                         "[[palavra-chave-item]]",
#                         item['palavraChave']
#                     )

#         itens_view = itens_view + item_view

#     # print(itens_view)

#     return itens_view

