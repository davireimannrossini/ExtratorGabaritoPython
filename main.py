import os
import cv2
import pytesseract
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

# Define as coordenadas das ROIs para o OCR
roi_nome_ocr = (288, 259, 743, 43)
roi_ra_ocr = (1087, 259, 153, 43)
roi_data_ocr = (1347, 259, 193, 43)

roi_turma_ocr = (298, 304, 168, 43)
roi_unidade_ocr = (1401, 304, 132, 43)

roi_ciclo_ocr = (1353, 342, 182, 43)
roi_tema_ocr = (991, 343, 990, 43)
roi_avaliacao = (1353, 342, 182, 43)

# Configuração do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Trata todas as imagens encontradas com o OpenCV
dadosEstudantes = []

for image_name in images:
    # Caminho completo para a imagem
    image_path = os.path.join(urlUploads, image_name)

    # Carrega a imagem usando o OpenCV
    image = cv2.imread(image_path)

    # Extrair as ROIs para OCR
    avaliacao = image[roi_avaliacao[1]:roi_avaliacao[1]+roi_avaliacao[3], roi_avaliacao[0]:roi_avaliacao[0]+roi_avaliacao[2]]
    data_ocr = image[roi_data_ocr[1]:roi_data_ocr[1]+roi_data_ocr[3], roi_data_ocr[0]:roi_data_ocr[0]+roi_data_ocr[2]]
    nome_ocr = image[roi_nome_ocr[1]:roi_nome_ocr[1]+roi_nome_ocr[3], roi_nome_ocr[0]:roi_nome_ocr[0]+roi_nome_ocr[2]]
    ra_ocr = image[roi_ra_ocr[1]:roi_ra_ocr[1]+roi_ra_ocr[3], roi_ra_ocr[0]:roi_ra_ocr[0]+roi_ra_ocr[2]]
    turma_ocr = image[roi_turma_ocr[1]:roi_turma_ocr[1]+roi_turma_ocr[3], roi_turma_ocr[0]:roi_turma_ocr[0]+roi_turma_ocr[2]]
    unidade_ocr = image[roi_unidade_ocr[1]:roi_unidade_ocr[1]+roi_unidade_ocr[3], roi_unidade_ocr[0]:roi_unidade_ocr[0]+roi_unidade_ocr[2]]
    ciclo_ocr = image[roi_ciclo_ocr[1]:roi_ciclo_ocr[1]+roi_ciclo_ocr[3], roi_ciclo_ocr[0]:roi_ciclo_ocr[0]+roi_ciclo_ocr[2]]
    tema_ocr = image[roi_tema_ocr[1]:roi_tema_ocr[1]+roi_tema_ocr[3], roi_tema_ocr[0]:roi_tema_ocr[0]+roi_tema_ocr[2]]

    # Converter as ROIs para escala de cinza
    avaliacao_gray = cv2.cvtColor(avaliacao, cv2.COLOR_BGR2GRAY)
    data_ocr_gray = cv2.cvtColor(data_ocr, cv2.COLOR_BGR2GRAY)
    nome_ocr_gray = cv2.cvtColor(nome_ocr, cv2.COLOR_BGR2GRAY)
    ra_ocr_gray = cv2.cvtColor(ra_ocr, cv2.COLOR_BGR2GRAY)
    turma_ocr_gray = cv2.cvtColor(turma_ocr, cv2.COLOR_BGR2GRAY)
    unidade_ocr_gray = cv2.cvtColor(unidade_ocr, cv2.COLOR_BGR2GRAY)
    ciclo_ocr_gray = cv2.cvtColor(ciclo_ocr, cv2.COLOR_BGR2GRAY)
    tema_ocr_gray = cv2.cvtColor(tema_ocr, cv2.COLOR_BGR2GRAY)

    # Aplicar OCR nas ROIs
    avaliacao_texto = pytesseract.image_to_string(avaliacao_gray, lang='eng')
    data_ocr_texto = pytesseract.image_to_string(data_ocr_gray, lang='eng')
    nome_ocr_texto = pytesseract.image_to_string(nome_ocr_gray, lang='eng')
    ra_ocr_texto = pytesseract.image_to_string(ra_ocr_gray, lang='eng')
    turma_ocr_texto = pytesseract.image_to_string(turma_ocr_gray, lang='eng')
    unidade_ocr_texto = pytesseract.image_to_string(unidade_ocr_gray, lang='eng')
    ciclo_ocr_texto = pytesseract.image_to_string(ciclo_ocr_gray, lang='eng')
    tema_ocr_texto = pytesseract.image_to_string(tema_ocr_gray, lang='eng')

    # Realize a análise dos campos e extraia os dados relevantes
    nome = nome_ocr_texto.strip()
    ra = ra_ocr_texto.strip()
    turma = turma_ocr_texto.strip()
    avaliacao = avaliacao_texto.strip()
    data = data_ocr_texto.strip()

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
