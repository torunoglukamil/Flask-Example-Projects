from flask import render_template, request
from app import app, captcha

@app.route('/', methods=['POST', 'GET'])
def captcha_form():
    if request.method == "POST":
        if captcha.validate():
            return "success"
        else:
            return "fail"
    return render_template('captcha_form.html')
