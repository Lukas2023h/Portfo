from flask import Flask, render_template, send_from_directory, request, redirect
import csv
import os

app = Flask(__name__)

@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name=None):
    return render_template(page_name)

def write_to_database(data):
    with open('database.txt', 'a') as file:
        for k, v in data.items():
            file.write(f'{k}: {v}\n')
        file.write(f'\n')
        
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as file2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(file2, delimiter=',' ,quotechar='"', 
                                quoting=csv.QUOTE_MINIMAL, )
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        print(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'






@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')