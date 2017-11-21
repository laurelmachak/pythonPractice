from flask import Flask, render_template
#import webbrowser

# so you can access resource files
app = Flask(__name__)

# url and view function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# debug True saying we want the debugger
# working in the background
if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
    #webbrowser.open("http://127.0.0.1:5000/")

# note that 0.0.0.0 means the app will be accesisible
# to any device on the network


# nav to http://127.0.0.1:5000/
