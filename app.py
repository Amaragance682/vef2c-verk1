from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """#.format(time=the_time)

@app.route('/sida2')
def page2():
    return"""
    <h1>Hello heroku</h1>
    <p>jeff timi er: {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """
@app route('/sida3')
def page3():
    return render_template('sida3.html')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)