import os
from flask import Flask
from config import Config
from controllers.user_controller import UserController

app = Flask(__name__, template_folder=os.path.join('views', 'templates'))
app.config.from_object(Config)

app.add_url_rule('/', 'index', UserController.index)
app.add_url_rule('/politica', 'politica', UserController.politica)
app.add_url_rule('/teste', 'teste', UserController.teste)


if __name__ == '__main__':
    app.run(debug=True)