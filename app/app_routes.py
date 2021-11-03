from app import app
from flask import render_template, flash, redirect, session
from app.form import LoginForm
from wtforms.fields.core import Label
from fillpdf import fillpdfs

@app.route('/')
def home():

    print(session)
    return render_template('main.html', title="Home")

questions = [
    "Alien Registration Number",
    "U.S Social Security Number",
    "USCIS Online Account Number",
    "Complete Last Name",
    "First Name",
    "Middle Name"
]

@app.route('/test-form/<field_num>', methods=['GET', 'POST'])
def login(field_num):
    
    form = LoginForm()
    form.field1.label = Label("post", questions[int(field_num)])
    if form.validate_on_submit():
        

        #if field_num != '0':
        #    print(session["fields"][str(int(field_num) - 1)])
        if "fields" not in session:
            session["fields"] = {}

        session["fields"][field_num] = form.field1.data
        session.modified = True
        

        return redirect('/test-form/' + str(int(field_num) + 1))
    return render_template('form.html', title='Sign In', form=form)


@app.route('/get_filled')
def get_filled():
    pdf_template = "i-589_form.pdf"
    pdf_output = "output.pdf"
    print(fillpdfs.get_form_fields(pdf_template))
    '''data_dict = {
        'Text2': 'Name',
        'Text4': 'LastName',
        'box': 'Yes',
    }

    fillpdfs.write_fillable_pdf(pdf_template, 'new.pdf', data_dict)

    # If you want it flattened:
    fillpdfs.flatten_pdf('new.pdf', 'newflat.pdf')'''


    
 
  