import os
from unittest import result
from flask import Blueprint, jsonify, request, render_template


blueprint = Blueprint('home', __name__, url_prefix='/', template_folder='templates', static_folder='static',static_url_path='/static/')


@blueprint.route('/', methods=["GET"])
def index():  
    if request.method == 'GET':
      return render_template('index.html')


@blueprint.route('/api/v1/', methods=['POST'])
def process_form():
 
    result = request.form.to_dict(flat=False)
    return jsonify(result)

    #data = request.form
    #print(data['username'])
    #print(data['password'])    
    #return data



 