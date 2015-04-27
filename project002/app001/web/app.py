from flask import Flask
from app001.utils import setupdb
from app001.web.views.admin import adminbp
from app001.utils.settings import DEBUG, USE_RELOADER


app = Flask(__name__)
app.register_blueprint(adminbp)
app.before_request(setupdb.refresh)

if __name__ == '__main__':
    app.run(debug=DEBUG, use_reloader=USE_RELOADER)
