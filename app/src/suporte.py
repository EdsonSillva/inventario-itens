

def get_model(path: str, file: str):

    model: str = ""

    path_file_model = f'{path}/{file}'
    arq_model = open(path_file_model, mode="r", encoding="utf-8")
    model = arq_model.read()
    arq_model.close()

    return model

