import pandas as pd
import requests
from faker import Faker
from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    text = '<p>Welcome to Task_4 created by Artem Goldaev</p>'
    text += f'''
    <a href={url_for("requirements")}>Requirements page</a></br>
    <a href={url_for("generate_users")}>Generate-users page</a></br>
    <a href={url_for("mean")}>Mean page</a></br>
    <a href={url_for("space")}>Space page</a></br>
    '''
    return text


@app.route('/requirements/')
def requirements():
    with open('requirements.txt') as f:
        req = f.readlines()

    res = ''
    for lib in req:
        lib_formatted = lib.replace('\n', '')
        res += f'<p>{lib_formatted}</p>'

    return f'<a href={url_for("main_page")}>Main page</a></br>' + res


@app.route('/generate-users/', methods=['GET'])
def generate_users():
    fake = Faker()
    args = request.args
    count = args.get('count')
    if count is None:
        return f'<a href={url_for("main_page")}>Main page</a></br>' \
               f'<p>You should add parameter count to see results</p>'
    try:
        count = int(count)
    except ValueError as e:
        return f'<a href={url_for("main_page")}>Main page</a></br>' \
               f'<p>Parameter count must have int</p>'
    users = f'<a href={url_for("main_page")}>Main page</a></br>'
    users_emails = []
    for _ in range(count):
        first_name = fake.first_name()
        user_email = (first_name + fake.last_name()).lower() + '@' + fake.free_email_domain()
        users += f'<p>{first_name} {user_email}</p>'
        users_emails.append({'name': first_name, 'email': user_email})

    return render_template('emails.html', emails=users_emails)


@app.route('/mean/')
def mean():
    df = pd.read_csv('hw.csv')
    mean_height = round(df['Height(Inches)'].mean() * 2.54, 2)
    mean_weight = round(df['Weight(Pounds)'].mean() * 0.453592, 2)
    return f'''
    <a href={url_for("main_page")}>Main page</a></br>
    <p>mean_height = {mean_height}</p>
    <p>mean_weight = {mean_weight}</p>
    '''


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronaut = r.json()['number']
    return f'<a href={url_for("main_page")}>Main page</a></br>' \
           f'<p>Number of astronauts in space: {astronaut}</p>'


if __name__ == '__main__':
    app.run(debug=True)
