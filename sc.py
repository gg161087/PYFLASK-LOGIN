from app import app
from config import config
from flask_wtf.csrf import CSRFProtect

csrf=CSRFProtect()
app.config.from_object(config['development'])
csrf.init_app(app)
app.run(debug=True)