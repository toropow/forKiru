#!flask/bin/python
from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/kiru', methods=['GET'])
def get_name_1():
    return jsonify({'name': 'Kiru'})


@app.route('/vasu', methods=['GET'])
def get_name_2():
    return jsonify({'name': 'Vasuuuu'})


@app.route('/natu', methods=['GET'])
def get_name_3():
    return jsonify({'name': 'Natuuu'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)