
from pathlib import (
    Path
)

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
    "pathView": f"{Path(__file__).parent.parent.parent}/site-inventario/view"
}

