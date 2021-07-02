from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/work/<int:work_id>')
def work(work_id):
    return render_template(f'work.html', id=work_id)


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(f'{page_name}.html')


@app.route('/contact_form', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
    return redirect(
        url_for(endpoint='.page', page_name='contact_ok', contact_name=name))


if __name__ == '__main__':
    app.run(debug=True)
