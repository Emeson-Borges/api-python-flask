from flask import Flask, jsonify, make_response, request

from bd import Carros

#Instancear uma variavel para o App
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Decorador para declarar uma rota
@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
       jsonify(
           msg='Lista de Carros.',
           data=Carros
       )
    )

#Criar dados
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
            jsonify(
                message='Carro cadastrado com Sucesso',
                carro=carro
            )
        ) 
        
    
    
#Startar o App
app.run()