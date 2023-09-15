# TaskLoad

O TaskLoad é um sistema eficaz para o gerenciamento de tarefas que simplifica a organização do trabalho diário. O objetivo principal do sistema é facilitar a gestão de atividades, garantindo centralização e controle dessas ao usuário. 

## 💈 Projeto em Produção
[Acesse aqui](https://taskload.fly.dev/docs)

## 📑 Documento de Requisitos de Software
[Acesse aqui](https://docs.google.com/document/d/16b-CBfULJDxG_XRGAQ6Nx4gNHEHyOLCYVKQ7KwPh5As/edit?usp=sharing)

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

* Python na versão >=3.11
* Docker
* Poetry

### 📈 Comandos automatizados
Todos os comandos automatizados foram criados utilizando o [taskipy](https://github.com/taskipy/taskipy) e podem acessados no [pyproject.toml](https://github.com/arturj9/taskload/blob/main/pyproject.toml) do projeto. Todos contêm a seguinte estrutura:

```
task <comando_especifico>
```

### 📡 Ativar ambiente virtual
* Poetry
  
```
poetry shell
```

* Pip
```
Crie um ambiente virtual e ative
```

### 📦 Instalação de dependências
* Poetry
  
```
poetry install
```

* Pip
```
pip install -r requirements.txt
```

### 🔧 Execução
* Docker
  
```
docker compose up
```

* Poetry e Pip
  
```
task run
```
  
### 📄 Formatação
```
task format
```

### ⚙️ Executando os testes

```
task test
```

## 📄 Licença

Este projeto está sob a MIT License - veja o arquivo [LICENSE.md](https://github.com/arturj9/taskload/blob/main/LICENSE) para detalhes.

