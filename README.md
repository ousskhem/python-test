# python-test
Objective:
- The candidate has to do a python api to connect to "Yahoo Finance API Pricing" 
- Provided instrument's pricing through the python api
- When user send an intrument to the api, the api replied with a specific price.

Note:
- Basic cost is free for Pricing
- First 500 API calls is still free

Requirement:
- python 3.7
- code versioning with git
- send code through github (please provide the link)
			
# Run the api in your local environement:
- Make sure python 3.7 is installed
- Clone the project 
- Open a comand line terminal and change directory to the project folder
- Run the following command to get necessary dependencies: 
pip install .
- Change directory to api_pricing
- Run api_pricing: 
python main.py


# Test the api in your local environement
- Use postman, soapUI, google chrome browser...
- It's a GET request with 2 mandatory queryparams symbol and region
- url: http://127.0.0.1:5000/api/v1/instrument/price?symbol=TSLA&region=US
- symbol(queryparam): It's the instrument code. exp: IBM, AAPL, TSLA..
- region(queryparam): should be one of these values ["US", "BR", "AU", "CA", "FR", "DE", "HK", "IN", "IT", "ES", "GB", "SG"].
	  Any other value will default region to "US" (as implemented in rapidAPI GET market/v2/get-quotes).
		
# Easiest way to test:
- Open browser and navigate to http://127.0.0.1:5000/api/v1/instrument/price?symbol=TSLA&region=US
- Change instrument symbol in the url to get corresponding price. exp: IBM, AAPL..
		
		
