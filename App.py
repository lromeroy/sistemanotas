from flask import Flask, request, redirect, url_for, render_template, session, flash

from flaskext.mysql import MySQL

from repository import insert_estudent, get_profesor, get_estudents, delete_estudent, get_estudent, update_estudent, get_estudents_notes, update_notes, insert_user

app = Flask(__name__)

app.secret_key = 'mysecretkey'

# RUTAS -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def Index():
    if 'user' in session:

        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html', user = session['user'])

@app.route('/notas')
def notas():
    lista = get_estudents_notes()
    return render_template('notas.html', notas = lista, user = session['user'])

@app.route('/estudiantes')
def estudents():
    lista = get_estudents()
    return render_template('estudiantes.html', estudiantes = lista, user = session['user'])

@app.route('/edit/<id>')
def edit_estudent(id):
    est = get_estudent(id)
    return render_template('edit_estudent.html', estudiante = est, user = session['user'])

@app.route('/editar_notas')
def edit_notes():
    lista = get_estudents_notes()
    return render_template('editar_notas.html', notas = lista, user = session['user'])

@app.route('/register')
def register():
    return render_template('register.html')

# METODOS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iniciar Sesion
@app.route('/login', methods=['POST'])
def iniciar_sesion():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_profesor(email, password)
        if(user[0]!=None):
            session['user'] = user[0]
            flash(user[1])
            return redirect(url_for('home'))
        else:
            flash(user[1])
            return redirect(url_for('login'))

# Cerrar sesion
@app.route('/logout')
def cerrar_sesion():
    session.pop('user', None)
    return redirect(url_for('iniciar_sesion'))

# Agregar un estudiante
@app.route('/estudiantes', methods=['POST'])
def add_estudent():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telef']
        response = insert_estudent(id, nombre, telefono, email)
        flash(response)

        return redirect(url_for('estudents'))

# Registro de usuario
@app.route('/register', methods=['POST'])
def add_user():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        email = request.form['email']
        pass1 = request.form['password']
        pass2 = request.form['password2']
        response = insert_user(id, nombre, email, pass1, pass2)
        if(response=='Usuario creado satisfactoriamente'):
            flash(response)
            return redirect(url_for('login'))
        else:
            flash(response)
            return redirect(url_for('register'))

# Editar un usuario
@app.route('/update/<id>', methods=['POST'])
def update_estudents(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telef']
        update_estudent(id, nombre, telefono, email)
        flash('Estudiante editado satisfactoriamente')
        return redirect(url_for('estudents'))

# Editar las notas
@app.route('/update_notes', methods=['POST'])
def editar_notas():
    if request.method == "POST":
        list = get_estudents_notes()
        newlist = ((0, 0), (0, 0))
        for lista in list:
            nota = request.form['nota%d'%lista[0]]
            print(nota)
            newlist += ((lista[0], nota), )
        print(newlist)
        update_notes(newlist)
    return redirect(url_for('notas'))

# Borrar un estudiante
@app.route('/delete/<string:id>')
def delete_contact(id):
    delete_estudent(id)
    flash('Estudiante eliminado satisfactoriamente')
    return redirect(url_for('estudents'))



if __name__ == '__main__':
  app.run(host='127.0.0.1', debug = True)
