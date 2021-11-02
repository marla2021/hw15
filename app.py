from flask import Flask, jsonify
from functions import animal_by_id


app = Flask(__name__)


@app.route('/<int:itemid>')
def info(itemid):
    result = animal_by_id(itemid)
    if not result:
        return "Животного с таким ID не найдено", 404
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)