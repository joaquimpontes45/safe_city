import os
if os.environ.get('VIRTUAL_ENV') is None:
    print("A venv não está ativa. Ativando...")
    os.system('.venv/Scripts/activate')


from flask import Flask, url_for, render_template
app = Flask(__name__,static_folder='static')

@app.route("/")
def hello_world():
    return render_template("site/login_user.html")

app.run(debug=True)
