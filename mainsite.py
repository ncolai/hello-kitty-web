from flask import Flask, render_template, request, redirect
app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    page_author = "Nick Lai"
    page_name = "The Greatest Page Evahr"
    return render_template('index.html', author=page_author, name=page_name)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

if __name__ == '__main__':
    app.run()
