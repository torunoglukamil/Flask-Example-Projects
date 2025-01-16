from flask import render_template
from app import app
from app.models.model_contact_form import ContactFormModel

@app.route("/", methods=["GET", "POST"])
def contact_us():
    contact_form = ContactFormModel()
    if contact_form.validate_on_submit():
        print(f"Name:{contact_form.name.data}, E-mail:{contact_form.email.data}, Message:{contact_form.message.data}")
    else:
        print("Invalid Credentials")
    return render_template("contact_us.html", form=contact_form)
