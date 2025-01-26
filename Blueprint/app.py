from flask import Flask
from api.api_admin import apiAdmin
from api.api_products import apiProducts
from api.api_users import apiUsers

app = Flask(__name__)

app.register_blueprint(apiAdmin)
app.register_blueprint(apiProducts)
app.register_blueprint(apiUsers)

if __name__ == "__main__":
    app.run(debug = True)
