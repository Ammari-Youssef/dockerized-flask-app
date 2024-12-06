from flask import Flask
# import redis

app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    # retries = 5
    # while True:
    #     try:
    #         return cache.incr('hits')
    #     except redis.exceptions.ConnectionError as exc:
    #         if retries == 0:
    #             raise exc
    #         retries -= 1
    return 1

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello, World! This page has been visited {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
