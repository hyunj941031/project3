from email.policy import default
from flask import Flask, render_template, request, url_for
import sqlite3
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/hotels', methods=['POST', 'GET'])
def hotels():
    conn = sqlite3.connect('C:/Users/pc/Desktop/Codestates/Section3/Project/Hotel_DB_API.db')
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Hotels")

    hotel_list = cursor.fetchall()

    if request.method == 'POST':
        city = request.form['city']
        grade = request.form.getlist('grade')
        # grade2 = request.form['grade2']
        # grade3 = request.form['grade3']
        # grade4 = request.form['grade4']
        # grade5 = request.form['grade5']
        # grade6 = request.form['grade6']
        score = request.form['score']
        review = request.form['review']
        # weekday = request.form['weekday']
        # friday = request.form['friday']
        # saturday = request.form['saturday']
        # sunday = request.form['sunday']
    elif request.method == 'GET':
        city = request.args.get('city')
        grade = request.args.get('grade')
        score = request.args.get('score')
        review = request.args.get(review)

    result_list = []
    for data in hotel_list:
        # if (data[1]==city) & (data[4] in grade) & (int(data[5])>=int(score)) & (int(data[6])>=int(review)):
        result_list.append(data[1:])

    if len(result_list) > 1:
        result_sample = random.choice(result_list)
    elif len(result_list) == 1:
        result_sample = result_list
    else:
        result_sample = ['-' for _ in range(len(hotel_list[0]))]

    image = result_sample[14]

    return render_template('result.html', result_sample = result_sample, image = image)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)