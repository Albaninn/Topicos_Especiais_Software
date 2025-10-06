import os
import shutil

# ------------------- CONFIGURAÇÃO -------------------
# Altere os valores abaixo de acordo com a sua necessidade.

# 1. Coloque o caminho para a primeira pasta de fotos.
pasta_fotos_1 = r"D:\DCIM\100D3100"

# 2. Coloque o caminho para a segunda pasta de fotos.
pasta_fotos_2 = r"D:\DCIM\101D3100"

# 3. Coloque o caminho para a pasta onde as fotos renomeadas serão salvas.
#    (Se a pasta não existir, o script vai criá-la para você).
pasta_destino = r"D:\DCIM\1"

# 4. Escolha um prefixo para os novos nomes dos arquivos.
prefixo_novo_nome = "Treino_SJP_02_10"

# ------------------- FIM DA CONFIGURAÇÃO -------------------


def organizar_fotos(origem1, origem2, destino, prefixo):
    """
    Copia e renomeia arquivos de duas pastas de origem para uma pasta de destino.
    """
    print("Iniciando o processo de organização de fotos...")

    # Lista para armazenar o caminho completo de todos os arquivos de fotos
    todos_os_arquivos = []

    # Pega todos os arquivos da primeira pasta
    try:
        for nome_arquivo in sorted(os.listdir(origem1)):
            caminho_completo = os.path.join(origem1, nome_arquivo)
            if os.path.isfile(caminho_completo): # Garante que é um arquivo
                todos_os_arquivos.append(caminho_completo)
        print(f"Encontrados {len(todos_os_arquivos)} arquivos em '{origem1}'")
    except FileNotFoundError:
        print(f"ERRO: A pasta '{origem1}' não foi encontrada. Verifique o caminho.")
        return

    # Pega todos os arquivos da segunda pasta
    arquivos_pasta2 = []
    try:
        for nome_arquivo in sorted(os.listdir(origem2)):
            caminho_completo = os.path.join(origem2, nome_arquivo)
            if os.path.isfile(caminho_completo):
                arquivos_pasta2.append(caminho_completo)
        print(f"Encontrados {len(arquivos_pasta2)} arquivos em '{origem2}'")
        todos_os_arquivos.extend(arquivos_pasta2)
    except FileNotFoundError:
        print(f"ERRO: A pasta '{origem2}' não foi encontrada. Verifique o caminho.")
        return

    # Cria a pasta de destino se ela não existir
    if not os.path.exists(destino):
        os.makedirs(destino)
        print(f"Pasta de destino criada em: '{destino}'")

    # Inicia o contador para os novos nomes
    contador = 1
    total_arquivos = len(todos_os_arquivos)
    
    # Define o número de zeros à esquerda (ex: 0001, 0002)
    padding = len(str(total_arquivos))

    # Loop para copiar e renomear cada arquivo
    for arquivo_original in todos_os_arquivos:
        # Pega a extensão do arquivo (ex: .jpg, .cr2, .png)
        extensao = os.path.splitext(arquivo_original)[1]

        # Monta o novo nome do arquivo
        # str(contador).zfill(padding) cria o número com zeros à esquerda (ex: 0001)
        novo_nome = f"{prefixo}_{str(contador).zfill(padding)}{extensao}"

        # Monta o caminho completo de destino
        caminho_final = os.path.join(destino, novo_nome)

        # Copia o arquivo para o destino com o novo nome
        # Usamos copy2 para tentar preservar os metadados da foto (data, hora, etc.)
        shutil.copy2(arquivo_original, caminho_final)

        print(f"Copiado: '{os.path.basename(arquivo_original)}' -> '{novo_nome}'")

        # Incrementa o contador para o próximo arquivo
        contador += 1

    print("\n---------------------------------------------------")
    print(f"Processo concluído com sucesso!")
    print(f"{total_arquivos} fotos foram copiadas e renomeadas na pasta '{destino}'.")


# Executa a função principal
if __name__ == "__main__":
    organizar_fotos(pasta_fotos_1, pasta_fotos_2, pasta_destino, prefixo_novo_nome)