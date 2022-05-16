from flask import (
    Flask,
    abort,
    jsonify,
    redirect, 
    render_template, 
    request,
    url_for
)
import datetime
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5051111@localhost:5432/park'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Formulario(db.Model):
    __tablename__='estacionamiento'
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.String(40), nullable=False)
    name=db.Column(db.String(80), nullable=False)
    placa=db.Column(db.String(6), nullable=False)
    def __repr__(self):
        return f'Formulario: {self.id},{self.date},{self.name},{self.placa}'

db.create_all()

@app.route('/op1')
def op1():
    return render_template('op1.html', data=Formulario.query.order_by('id').all())

@app.route('/login', methods =['GET', 'POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'] != 'Pogbvam' or request.form['password']!='Ut3c':
            error="Cuenta o contraseña incorrecta, intente de nuevo."
        else:
            return redirect('/op1')
    return render_template('login.html', error=error)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/formulario', methods=['POST'])
def formulario():
    response={}
    error=False
    try:
        name = request.get_json()['name']
        placa = request.get_json()['placa']
        date=datetime.datetime.now().hour
        formulario=Formulario(date=date, name=name, placa=placa)
        db.session.add(formulario)
        db.session.commit()
        response['id']=formulario.id
        response['name'] = name
        response['placa'] = placa
        response['date'] = date

    except Exception as e:
        print(e)
        print(sys.exc_info())
        error=True
        db.session.rollback()
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(response)

@app.route('/create/<formulario_id>/delete', methods=['DELETE'])
def delete(formulario_id):
    success=True
    try:
        list=Formulario.query.get(formulario_id)
        db.session.delete(list)
        db.session.commit()
    except:
        success=False
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({
        'success': success
    })




if __name__=='__main__':
    app.run(port=5000, debug=True)

