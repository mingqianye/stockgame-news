from flask import Flask, jsonify
from flask_caching import Cache
from flask_compress import Compress
import tushare as ts
import sys, os
import dateutil

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
Compress(app)

def to_iso8601(ts):
    return dateutil.parser.parse(ts).isoformat()

def process(item):
    return {"title": item["title"], "content": item["content"], "time": to_iso8601(item["time"])}


@app.route("/news")
@cache.cached(timeout=1000)
def hello():
    app.logger.info("Connecting to Tushare...")
    result = ts.get_latest_news(top=50,show_content=True).to_dict('records')
    return jsonify({"news": list(map(process, result))})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
