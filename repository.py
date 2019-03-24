from flask import Flask, request, redirect, url_for, render_template, session

from flaskext.mysql import MySQL

app = Flask(__name__)

#DATABASE
#Configuracion para la coneccion a la base de datos

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistemanotas'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
"""SELECT * FROM usarios JOIN profesores WHERE usuarios.id = profesores.id_usuario and profesores.id = %s """
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#INSERTS
# Metodos para insertar los datos en su respectivas tablas

def insert_user(id, nombre, email, pass1, pass2):
    if(pass1==pass2):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM profesores WHERE id = %s """, id)
        prof = cur.fetchone()
        if(prof==None):
            cur.execute("""SELECT * FROM usuarios WHERE email = %s """, email)
            user = cur.fetchone()
            if(user==None):
                cur.execute('INSERT INTO usuarios (email, password) VALUES (%s, %s)',(email, pass1))
                conn.commit()
                u = get_user(email, pass1)
                cur.execute('INSERT INTO profesores (id, nombre, user_id) VALUES (%s, %s, %s)',(id, nombre, u[0]))
                conn.commit()
                return 'Usuario creado satisfactoriamente'
            else:
                return 'Ya existe un usuario con este email, por favor eliga otro'
        else:
            return 'Ya existe un usario con esta cedula, por favor eliga otra'
    else:
        return 'Las contraseñas no coinciden'

def insert_estudent(id, nombre, telef, email):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT id FROM estudiantes WHERE id = %s """, id)
    alum = cur.fetchone()
    if(alum==None):
        cur.execute('INSERT INTO estudiantes (id, nombre) VALUES (%s, %s)',(id, nombre))
        cur.execute('INSERT INTO datos_estudiantes (id_estudiante, telefono, email) VALUES (%s, %s, %s)',(id, telef, email))
        conn.commit()
        return 'Estudiante agregado exitosamente'
    else:
        return 'Ya existe un este estudiante con esta cedula'


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GETTERS
#Sacan los datos de las tablas o valores especificos de las mismas

def get_user(email, password):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM usuarios WHERE email = %s and password = %s """, (email, password))
    return cur.fetchone()

def get_profesor(email, password):
    conn = mysql.connect()
    cur = conn.cursor()
    user = get_user(email, password)
    if(user!=None):
        cur.execute("""SELECT profesores.id, profesores.nombre, usuarios.email FROM profesores JOIN usuarios WHERE usuarios.id = profesores.user_id and usuarios.id= %s""", user[0])
        prof = cur.fetchone()
        if(prof!=None):
            return (prof, 'Bienvenido ' + prof[1])
        else:
            return (None, 'Algo salio mal')
    else:
        return (None, "Email o clave invalidos")

def get_estudents():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT estudiantes.id, estudiantes.nombre, datos_estudiantes.email, datos_estudiantes.telefono
    FROM estudiantes JOIN datos_estudiantes WHERE estudiantes.id = datos_estudiantes.id_estudiante""")
    list = cur.fetchall()
    return list

def get_estudent(id):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM estudiantes JOIN datos_estudiantes WHERE  estudiantes.id = %s and datos_estudiantes.id_estudiante = %s  """, (id, id))
    return cur.fetchone()

def get_estudents_notes():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT id, nombre, email, telefono, nota
                    FROM estudiantes AS t1 INNER JOIN datos_estudiantes AS t2 ON t1.id = t2.id_estudiante
                    INNER JOIN notas_estudiantes AS t3 ON t2.id_estudiante = t3.id_estudiante""")
    list = cur.fetchall()
    return list

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#UPDATES Y DELETES
#Metodos que modifiquen o eliminen datos de las tablas

def delete_estudent(id):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""DELETE FROM estudiantes WHERE id = %s """, id)
    cur.execute("""DELETE FROM datos_estudiantes WHERE id_estudiante = %s """, id)
    conn.commit()

def update_notes(list):
    conn = mysql.connect()
    cur = conn.cursor()
    for lista in list:
        cur.execute("""
            UPDATE notas_estudiantes
            SET nota = %s
            WHERE id_estudiante = %s""", (lista[1], lista[0]))
    conn.commit()

def update_estudent(id, nombre, telef, email):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE estudiantes
        SET nombre = %s
        WHERE id = %s""", (nombre, id))
    cur.execute("""
        UPDATE datos_estudiantes
        SET email = %s,
            telefono = %s
        WHERE id_estudiante = %s""", (email, telef, id))
    conn.commit()
