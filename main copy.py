import os
import cv2
from datetime import datetime

# Altera o diretório atual para o Uploads de Redações
os.chdir(r"e:\Python\Redacao\Uploads")

# Pega o diretório atual
os.getcwd()

# Imprime o diretório Uploads de Redações
urlUploads = os.getcwd()
print(urlUploads)

# Gera lista com os arquivos do diretório
images = os.listdir(urlUploads)

# Lista com os arquivos
print(os.listdir(urlUploads))

# Trata todas as imagens encontradas com o OpenCV
dadosEstudantes = []

for image_name in images:
    # Caminho completo para a imagem
    image_path = os.path.join(urlUploads, image_name)

    # Carrega a imagem usando o OpenCV
    image = cv2.imread(image_path)

    # Realize a análise da imagem e extraia os dados relevantes
    # Substitua esta parte com a lógica adequada para analisar a imagem
    nome = "John Doe"
    ra = "123456"
    turma = "A"
    avaliacao = "Aprovado"
    data = datetime.now()

    # Adicione os dados ao array dadosEstudantes
    dadosEstudantes.append({
        'nome': nome,
        'ra': ra,
        'turma': turma,
        'avaliacao': avaliacao,
        'data': data,
        'path': image_path
    })

    # Exemplo de impressão dos dados para cada imagem
    print("Dados do estudante:")
    print("Nome:", nome)
    print("RA:", ra)
    print("Turma:", turma)
    print("Avaliação:", avaliacao)
    print("Data:", data)
    print("Path:", image_path)
    print()

# Exemplo de impressão dos dados para todas as imagens
print("Dados de todos os estudantes:")
for estudante in dadosEstudantes:
    print(estudante)