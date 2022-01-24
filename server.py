from flask import Flask #import Flask Framework

from flask import url_for

from flask import render_template

from flask import request

from flask import redirect

import csv

app = Flask(__name__) #Initialising Flask

#print(__name__) #printing Name

@app.route('/') #decorator
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:  # opening our database.txt file in append mode (why append mode?)

        email = data['email']  # fetching data from our data dictionary created in html form

        subject = data['subject']  # fetching subject from our data dictionary created in html form

        message = data['message']  # fetching message from our data dictionary created in html form

        file = database.write(f'\n{email},{subject},{message}')  # writing data to our file in specified format


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:  # opening our database.csv file in append mode (why append mode?)

        email = data['email']  # fetching data from our data dictionary created in html form

        subject = data['subject']  # fetching subject from our data dictionary created in html form

        message = data['message']  # fetching message from our data dictionary created in html form

        # csv.writer takes some parameters- 1-file in which to write, 2 - delimiter-Line/Column breaker, 3-quotechar, 4-quoting

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST': #if we have post method
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something is wrong'


#We can use url parameters as follows
#@app.route('/<username>') #This is home directory
#def hello_world2(username = None):
#    return render_template('index.html', name = username)

