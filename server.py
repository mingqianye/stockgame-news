from flask import Flask, jsonify
from flask_caching import Cache
import tushare as ts
import sys

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def process(item):
    return {"title": item["title"], "content": item["content"]}

@app.route("/news")
@cache.cached(timeout=60)
def hello():
    result = ts.get_latest_news(top=20,show_content=True).to_dict('records')
    return jsonify(list(map(process, result)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
