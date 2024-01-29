from flask import Flask, request
from fibonacci import fibonacci

app = Flask(__name__)

@app.route('/web', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        n = int(request.form.get('N'))
        return '''
                    <h1>Num is: {}</h1>
                    <h2>First {} Fibonacci`s numbers are:</h2>
                    <h3>{}</h3>'''.format(n, n, ', '.join([str(elem) for elem in fibonacci(n)]))

    return '''
              <form method="POST">
                  <div><label>Input N: <input type="text" name="N"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/api', methods=['GET'])
def api():
    numbers = int(request.args.get('numbers'))
    return " ".join([str(i) for i in fibonacci(int(numbers))])

if __name__ == "__main__":
    app.run(debug=True)