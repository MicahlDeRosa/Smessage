from flask import Flask, render_template

from wtforms_fields import RegistrationForm

app = Flask(__name__)
app.secret_key = "replace later"


@app.route('/', methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return "Great Job"


    return render_template("index.html", form=reg_form)


if __name__ == '__main__':
    app.run()
