from flask import render_template

class UserController:
    @staticmethod
    def index():
        return render_template('index.html')
    
    @staticmethod
    def politica():
        return render_template('politica.html')
    
    @staticmethod
    def teste():
        return render_template('teste.html') 
    
