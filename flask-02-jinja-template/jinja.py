from flask import Flask, render_template
<<<<<<< HEAD
app = Flask(__name__)
@app.route('/')
def head():
    return render_template('index.html', number1=112500, number2=225200)
@app.route('/mult')
=======

app = Flask(__name__)

@app.route('/')

def head():
    return render_template('index.html', number1=888, number2=9999)


@app.route('/mult')

>>>>>>> 4231baa69c0f9c0c07dea11a8cb8b265ed9f8327
def number():
    x=15
    y=20
    return render_template('body.html', num1=x, num2=y, mult=x*y)
<<<<<<< HEAD
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
=======

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
>>>>>>> 4231baa69c0f9c0c07dea11a8cb8b265ed9f8327
