from flask import Flask, session, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['POST'])
def contact():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    
    ##ghost notes
