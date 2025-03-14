import sqlite3

from flask import Flask,request, jsonify


app = Flask(__name__) 

def init_db():
    # sqlite3 cria o arquivo database.db e se conecta com a variável conn (connection)
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para criar a tabela LIVROS, caso ela ainda não exista
        conn.execute(
            """ 
                CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     image_url TEXT NOT NULL
                )    
            """
        )
        
init_db()

@app.route("/doar", methods =["POST"])
def doar():
    
    dados = request.get_json()
    
    print(f"Seus Dados Foram Retornados {dados}")
    
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("imagem_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro":"Todos os campos são obrigatórios."}), 400

    with sqlite3.connect("database.db") as conn:
        conn.execute(""""
        INSERT INTO LIVROS (titulo,categoria,autor,imagem_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
""")

    conn.commit()
    
    return jsonify({"mensagem":"Livro cadastrado com sucesso."}), 201

# Se o arquivo app.py for o arquivo principal da nossa aplicação, rode a api no modo de depuração
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração
    # O modo debug faz com que as mudanças no código sejam aplicadas automaticamente, sem necessidade de 
    app.run(debug=True)