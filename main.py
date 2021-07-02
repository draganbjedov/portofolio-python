from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/work/<int:work_id>')
def work(work_id):
    return render_template(f'work.html', id = work_id)

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(f'{page_name}.html')


if __name__ == '__main__':
    app.run(debug=True)
