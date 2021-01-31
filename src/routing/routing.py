from packages.packages import redirect, render_template, session
from application import App
app = App()

@app.route('/')
def home():
    return render_template('index.html')
