import os
from cryptography.fernet import Fernet


CHAVE_PATH = os.path.join(os.getcwd(), 'chave_secreta.key')


def carregar_ou_gerar_chave():
    # Verifica se o arquivo da chave existe
    if os.path.exists(CHAVE_PATH):
        with open(CHAVE_PATH, 'rb') as file:
            chave = file.read()
    else:
        # Gera uma nova chave e salva no arquivo
        chave = Fernet.generate_key()
        with open(CHAVE_PATH, 'wb') as file:
            file.write(chave)
    return chave


def criptografar_texto(texto, chave):
    f = Fernet(chave)
    return f.encrypt(texto.encode()).decode()


def descriptografar_texto(texto_criptografado, chave):
    f = Fernet(chave)
    return f.decrypt(texto_criptografado.encode()).decode()
