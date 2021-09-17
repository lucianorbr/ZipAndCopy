import shutil
from datetime import datetime

caminho_original = 'caminho de origem da pasta'
caminho_novo = 'caminha de destino da pasta'
caminho_data = caminho_novo + " -" + datetime.now().strftime("%d%m%Y")


shutil.make_archive(caminho_data, 'zip', caminho_original, 'Files')