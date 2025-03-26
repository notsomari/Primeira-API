# API Livros Doados VnW 📚

Essa é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai na Web, ela permite cadastrar e listar os livros doados! 😸
 
## Ferramentas Utilizadas ⚙️

- **Python**
- **Flask**
- **SQLite3**

## Como Rodar o Projeto? 📖

1. Faça o clone do repositório:
```bash
git clone <LINK_DO_REPOSITORIO>
cd nome_do_projeto
```
2. Criar um ambiente virtual (Obrigatório, mas fica ao seu critério!):

**Windows** 🪟

```bash
python -m venv venv 
source venv/Scripts/activate
```

**Linux/Mac** 🐧

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor: 🚀
```bash
python app.py
```

> A API estará disponível em  http://127.0.0.1:5000/

## Endpoints 📒

### POST /doar

Endpoint para cadastro das informações do livro doado.

**Envio (JSON)**
```json
{
    "titulo":"Ainda Estou aqui",
    "categoria":"Drama",
    "autor":"Walter Salles",
    "image_url":"https://exemplo.com"
}
```