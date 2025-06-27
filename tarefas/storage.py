import json
import os

CAMINHO_PASTA = "data"
CAMINHO_ARQUIVO = os.path.join(CAMINHO_PASTA, "tarefas.json")

def garantir_estrutura():
    if not os.path.exists(CAMINHO_PASTA):
        os.makedirs(CAMINHO_PASTA)
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)

def carregar_tarefas():
    garantir_estrutura()
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def salvar_tarefas(lista):
    garantir_estrutura()
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)