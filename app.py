import flask
from flask import jsonify, request
from stock_detail import get_web_page,get_stock_info

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/getStock', methods=['GET'])
def city_name():
    if 'stock' in request.args:
        stock = request.args['stock']
    else:
        return "Error: No stock provided. Please specify a stock."
    results = []
    page=get_web_page('TPE: '+stock)
    if page:
        stock = get_stock_info(page)
        for k, v in stock.items():
            key =k.replace("：","")
            results.append({key:v})
            # print(k, v)
    return jsonify(results)


app.run()