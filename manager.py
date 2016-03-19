from flask import Flask
from tasks import sum_n_primes


app = Flask(__name__)


@app.route('/sum/<int:n>')
def sum_of_n_primes(n):
    return str(sum_n_primes(n))

@app.route('/sums/<int:n>')
def asum_of_n_primes(n):
    result = sum_n_primes.delay(n)
    return str(sum_n_primes.delay(n))


if __name__ == '__main__':
    app.run(debug=True)
