from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)

def convert_usd_to_brl(amount_in_usd):
    # API endpoint for exchange rates
    api_endpoint = 'https://api.exchangerate-api.com/v4/latest/USD'
    # Fetch exchange rates from the API
    response = requests.get(api_endpoint)
    data = response.json()
    # Get the exchange rate of BRL to USD
    brl_to_usd_rate = data['rates']['BRL']
    # Convert amount from USD to BRL
    amount_in_brl = amount_in_usd * brl_to_usd_rate
    return amount_in_brl

@app.route('/')
def convert():
    amount_in_usd = float(request.args.get('amount'))
    amount_in_brl = convert_usd_to_brl(amount_in_usd)
    return jsonify({"amount_in_brl": amount_in_brl})

if __name__ == '__main__':
    app.run()
    

    




