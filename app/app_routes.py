from app import app, questions
from flask import render_template, flash, redirect, session, send_file, send_from_directory
from app.form import LoginForm
from wtforms.fields.core import Label
from fillpdf import fillpdfs

# Helper functions for managing inputed field data in session object
def get_fields():
    if "fields" in session:
        return session["fields"]
    else:
        return {}

def set_field(field_num, val):
    if "fields" not in session:
        session["fields"] = {}
        
    session["fields"][field_num] = val
    session.modified = True


# Main Route
@app.route('/')
def home():
    print(session)
    return render_template('main.html', title="Home")


# Route for asking user to fill a field
@app.route('/test-form/<field_num>', methods=['GET', 'POST'])
def ask_question(field_num):
    
    form = LoginForm()
    question = questions[int(field_num)]
    form.field1.label = Label("post", question)
    if form.validate_on_submit():

        set_field(question, form.field1.data)
        return redirect('/test-form/' + str(int(field_num) + 1))

    return render_template('form.html', field_num = field_num, form=form)

# Route for showing user the fields they have filled
@app.route('/confirm')
def confirm():
    return render_template('confirm.html', title="Home", dict=get_fields())

# Route for sending completed form
@app.route('/get-form')
def get_filled_form():
    pdf_template = "app/static/test-copy.pdf"
    pdf_output = "app/static/output.pdf"
    
    fillpdfs.write_fillable_pdf(pdf_template, pdf_output, get_fields())
    return send_from_directory(app.static_folder, "output.pdf")




   


    
 
  