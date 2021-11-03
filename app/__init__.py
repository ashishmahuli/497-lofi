from flask import Flask, session
from fillpdf import fillpdfs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

def generate_questions():
    pdf_template = "app/static/test-copy.pdf"
    x= fillpdfs.get_form_fields(pdf_template)
    return list(x.keys())

questions = generate_questions()

from app import app_routes