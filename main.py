from flask import flask, render_template, request
import os

#define a pasta onde estão os arquivos HTML 
# (neste caso, a raiz do produto)
template_dir = os.path.abspath(os.path.dirname(__file__))
app = flask(__name__, template_folder=template_dir)

#Direcionamento para a página index.html
@app.route("/")
def nome ():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3000)