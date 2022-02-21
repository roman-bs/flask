import os
import redis


from flask import Flask, request, render_template



app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_client = redis.Redis(host=redis_host, port=6379, db=0)



@app.route("/")
def hello_world():
    if request.method == "POST":
        if "key" in request.values:
            redis_client
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
