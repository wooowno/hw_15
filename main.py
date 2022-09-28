from flask import Flask, jsonify

from utils import get_item

app = Flask(__name__)


@app.route("/<int:itemid>")
def item_page(itemid):
    return jsonify(get_item(itemid))


if __name__ == '__main__':
    app.run()
