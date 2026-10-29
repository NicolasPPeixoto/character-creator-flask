import os
from dotenv import load_dotenv
from flask import Flask, render_template
from routes.character import character_customization_bp
from database import Base, engine, session
from models.Character import Character

# carrega as variáveis definidas no arquivo .env (se ele existir) para os.environ
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")

    if not app.secret_key:
        raise RuntimeError(
            "SECRET_KEY nao definida. Crie um arquivo .env na raiz do projeto "
            "com uma linha SECRET_KEY=sua_chave_aqui (veja .env.example)."
        )

    @app.route('/')
    def index():
        return render_template("index.html")
    
    app.register_blueprint(character_customization_bp)
    
    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    


# Base.metadata.create_all(bind=engine)

# character_2 = Character(name="John", hair="vermelho", clothes="calça")

# session.add(character_2)

# session.commit()



    
    

    
        

