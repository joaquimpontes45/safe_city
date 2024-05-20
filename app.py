import os
from flask import Flask, render_template,url_for,request,redirect
from conexao import conectar
if os.environ.get('VIRTUAL_ENV') is None:
    print("A venv não está ativa. Ativando...")
    os.system('.venv/Scripts/activate')



app = Flask(__name__,static_folder='static')

@app.route("/denuncia", methods=['GET', 'POST'])
def denunciar():
    if request.method =='POST':
        nome_denunciante= request.form.get('nome_denuncia')
        numero= request.form.get('numero')
        cidade= request.form.get('cidade')
        bairro= request.form.get('bairro')
        rua= request.form.get('rua')
        tipo_do_crime= request.form.get('tipo_do_crime')
        data= request.form.get('data')
        hora= request.form.get('hora')
        cor= request.form.get('cor')
        sexo= request.form.get('sexo')
        altura= request.form.get('altura')
        descricao= request.form.get('descricao')
        if nome_denunciante and rua:
            conn= conectar()
            conn.execute('INSERT INTO  denuncias (Nome, telefone, cidade, bairro, rua, tipo_do_crime, data, hora, cor_criminoso, sexo, Altura, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (nome_denunciante, numero, cidade, bairro, rua, tipo_do_crime, data, hora, cor, sexo, altura, descricao))
            conn.commit()
            conn.close()
            return redirect(url_for('login', mensagem="Denuncia realizada com sucesso"))
    return render_template('site/denunciar.html')
@app.route("/")
def login():
    mensagem = request.args.get('mensagem')
    return render_template('site/login_user.html',mensagem=mensagem)

                                                                      #  ROTAS ADMIN


@app.route('/admin')
def listagem_de_denuncias():
    conn=conectar()
    denuncia= conn.execute('SELECT * FROM denuncias').fetchall()
    conn.close()
    return render_template('admin/form_denuncia.html',denuncias=denuncia,)

@app.route('/admin/ver_denuncia/<int:id>',methods=['GET','POST'])
def ver_denuncia(id):
    conn=conectar()
    denuncia= conn.execute('SELECT * FROM denuncias WHERE id= ?',(id,)).fetchone()
    conn.close()
    return render_template('admin/ver_denuncia.html', denuncia=denuncia)

app.run(debug=True)


