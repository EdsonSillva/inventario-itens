
from pathlib import (
    Path
)

import enum

# variáveis importantes para execução da função [main.py]

_ARQUIVO_ITENS_ = "app/src/itens-json/lista-itens.json"

index_model = {
    "path": "app/src/model/index",
    "filePage": "01_page_index.html",
    "fileItem": "02_item_index.html"
}

view_model = {
    "path": "app/src/model/view",
    "filePage": "01_page_view.html",
    "fileItem": "02_item_view.html"
}


# variáveis importantes para execução da função [geracao_site.py]

index_html = {
    "pathIndex": f"{Path(__file__).parent.parent.parent}/site-inventario",
    "arqIndex": "index.html"
}

view_html = {
    "pathInventario": f"{Path(__file__).parent.parent.parent}/site-inventario",
    "pathView": f"{Path(__file__).parent.parent.parent}/site-inventario/view",
    "pathImg": f"{Path(__file__).parent.parent.parent}/site-inventario/img"
}

imagem_model = {

    "imagemUnica": {

        "path": "app/src/model/view/tipo_imagem",
        "fileHtml": "00_unica_imagem.html",
        "variaveis": ["[[href-img-item]]"]          # Local da imagem

    },

    "ImagemCarrossel": {

        "htmlItem": {

            "path": "app/src/model/view/tipo_imagem",
            "fileHtml": "01_carrossel_imagem.html",
            "variaveis": ["[[num-carrossel]]",        # Controle do carrossel de um item
                          "[[list-carroussel]]",      # Vai receber a lista de tag <li>
                          "[[item-carroussel]]"       # Vai receber a lista de item q estão refenciados na tag <li>
                        ]
        },

        "htmlTagList": {

            "path": "app/src/model/view/tipo_imagem",
            "fileHtml": "02_carrossel_tag_li.html",
            "variaveis": ["[[num-carrossel]]",        # Controle do carrossel de um item
                          "[[num-item-li]]",          # Número representando o item da tag <li>
                          "[[class-active-item]]"     # indica active ou não. Colocado no primeiro item da tag <li> 
                        ]
        },

        "htmlItemDiv": {

            "path": "app/src/model/view/tipo_imagem",
            "fileHtml": "03_carrossel_item.html",
            "variaveis": ["[[active-item]]",          # indica active ou não. Colocado no primeiro item da tag <li> 
                          "[[href-img-item]]",        # Controle do carrossel de um item
                        ]
        },

        "htmlScript": {
            
            "path": "app/src/model/view/tipo_imagem",
            "fileHtml": "04_carrossel_script.html",
            "variaveis": ["[[qtdeCarrossel]]"         # indica active ou não. Colocado no primeiro item da tag <li> 
                        ]
        }
    }
}


# enuns

class retorno_path_enum(enum.Enum):
    diretorio = 1
    arquivo = 2
    subpasta = 3


class model_enum(enum.Enum):
    page_view = 1
    item_view = 2
    
