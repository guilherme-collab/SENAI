from flask import flask, render_template, request
import os

#define a pasta onde estão os arquivos HTML 
# (neste caso, a raiz do produto)
template_dir = os.path.abspath(os.path.dirname(_file_))
app = flask(__name__, template_folder=template_dir)

