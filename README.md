# Desafio Globo Full Stack

> O desafio consiste em desenvolver uma aplicação que deve importar arquivos contendo dados de alimentos, tratar esses 
> dados e disponibiliza-los para o usuário de uma forma que ele possa saber qual alimento é mais rico em proteínas, 
> carboidratos ou gorduras.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você tem uma máquina `Windows`.
* Você instalou a versão mais recente do `Docker for Windows`.

## 🚀 Instalando e rodando

Para instalar o projeto, siga estas etapas:

Linux e macOS:
```
docker-compose -f docker-compose.yml run --rm backend python manage.py migrate
docker-compose -f docker-compose.yml run --rm backend python manage.py createsuperuser
# Informe o nome de usuário e senha do usuário `admin`
docker-compose -f docker-compose.yml up -d
```

Windows:
```
docker-compose -f docker-compose.yml run --rm backend python manage.py migrate
docker-compose -f docker-compose.yml run --rm backend python manage.py createsuperuser
# Informe o nome de usuário e senha do usuário `admin`
docker-compose -f docker-compose.yml up -d
```

## ☕ Usando

Primeiro faça o upload dos arquivos com os dados dos alimentos, siga estas etapas:

- Acesse o admin utilizando o seguinte endereço: [http://localhost:8000/admin](http://localhost:8000/admin)
- Logue com o usuário e senha que você criou na instalação
- Clique me `Imported files` e depois `Add imported file`
- Faça o upload do arquivo txt que você deseja incluir e clique em `Save`.

Agora visualize os dados importados acessando o seguinte endereço: [http://localhost:5000](http://localhost:5000)

### Ajustes e melhorias que ainda precisam ser feitas

- [ ] Estilos do frontend
