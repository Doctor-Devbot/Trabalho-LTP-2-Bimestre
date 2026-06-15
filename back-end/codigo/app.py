from flask import Flask
from flask import request
from flask import make_response
from routes.atividade_router import atividade_bp 

app = Flask(__name__)
app.register_blueprint(atividade_bp)

if __name__ == "__main__":
    app.run(debug=True)