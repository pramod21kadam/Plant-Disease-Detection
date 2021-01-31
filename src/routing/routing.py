from packages.packages import *
from application import App
app = App()

@app.route('/')
def home():
    return render_template('index.html')
