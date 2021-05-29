import requests
import json
import model
import config

headers = {
    "X-RapidAPI-Key": config.GET_QUOTES_API_CONFIG['rapidapi_key'],
    "X-RapidAPI-Host": config.GET_QUOTES_API_CONFIG['rapidapi_host'],
    "Content-Type": "application/json"
}


def get_instrument(symbol, region):
    querystring = {
        "symbols": symbol,
        "region": region
    }

    response = requests.request("GET", config.GET_QUOTES_API_CONFIG['url'], headers=headers, params=querystring)
    return json.loads(response.text)["quoteResponse"]["result"]


def get_instrument_price(symbol, region):
    result = model.instrument_price.copy()

    result["symbol"] = symbol
    result["region"] = region

    if symbol == "" or region == "":
        result["message"] = "Please specify a symbol and region code as query params for this request. "
        return result

    if region not in config.GET_QUOTES_API_CONFIG["region"]:
        result["message"] = "The region code provided is not in the following list {}." \
                            "Therefore, The region is set by default to US".format(config.GET_QUOTES_API_CONFIG["region"])

    instruments = get_instrument(symbol, region)

    if instruments != [] and "regularMarketPrice" in instruments[0].keys():
        result["regularMarketPrice"] = instruments[0]["regularMarketPrice"]

    return result
