Bem vindo ao meu sistema de criptografia!!!

antes de  prosseguir, por favor, crie uma venv com o seguinte comando:

```bash
python3 -m venv (nome da venv)
```
lembre-se de ativar a venv

```bash
.\venv\Scripts\activate
```

para rodar o projeto é necessario tem instalado o PIP, python 3.12 e instalar tudo que se pede no arquivo requirements.txt

basta rodar este comando
```bash
    pip install -r requirements.txt
```
após concluido os passos acima, entre no diretorio do projeto (desafio1) e rode os seguintes comandos:

```bash
python manage.py makemigrations

python  manage.py migrate

```
para criar as tabelas no dbsqlite, e agora é  só rodar o comando abaixo para iniciar o servidor:

```bash
python manage.py runserver
```
ao iniciar irao aparecer 3 urls, va para de criptogafia,  e a partir daqui você pode criptografar e descriptografar o seu texto.