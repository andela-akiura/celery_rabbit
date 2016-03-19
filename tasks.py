from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    i = 0
    for i in range(100000000):
        i + 1
    return i


@app.task
def multiply(a, b):
    return a * b


def isprime(n):
    for m in range(2, int(n**0.5)+1):
        if not n % m:
            return False
    return True


@app.task
def sum_n_primes(n):
    primes = []
    for i in range(2, n):
        if isprime(i):
            primes.append(i)
    # return [i for i in range(n) if i]
    return sum(primes)

print sum_n_primes(156)
