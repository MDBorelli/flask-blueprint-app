from app import create_app

app = create_app() # Cria a aplicação chamando a factory


# Executa o servidor de desenvolvimento do Flask
# debug=True ativa o modo de depuração para 
# reiniciar o servidor a cada alteração
if __name__ == 'main':
    app.run(debug=True)

# python -m venv venv
# pip install flask
# .\venv\Scripts\activate
# $env:FLASK_APP="run.py"
# flask run