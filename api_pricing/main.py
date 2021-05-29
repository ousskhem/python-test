import flask
from flask import request
from rapidAPI import get_instrument_price
import model

app = flask.Flask(__name__)


@app.route('/api/v1/instrument/price', methods=['GET'])
def get_price():
    if request.args.keys() >= {"symbol", "region"}:
        return get_instrument_price(request.args["symbol"], request.args["region"])
    else:
        result = model.instrument_price.copy()
        result["message"] = "Error: No symbol or region code provided. " \
                            "Please specify a symbol and region code as query params for this request. " \
                            "If region query parm is provided with empty value the search will defaulted to US " \
                            "region. "
        return result


if __name__ == "__main__":
    app.run()
