from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + ".html")

@app.route('/form_submit', methods=['POST', 'GET'])
def form_submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('thankyou')
    else:
        return 'something went wrong'
