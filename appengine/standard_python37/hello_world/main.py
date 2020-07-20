
from flask import Flask, request
from emoji import emojize


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    name = request.args.get('name','World')
    return emojize(f'Hello {name}!')

if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)

