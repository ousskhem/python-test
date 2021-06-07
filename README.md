
# python-test
GET /api/v1/instrument/price requires 2 mandatory queryparams:
- symbol: Instrument code (exp: IBM, AAPL..)
- region: should be one of these values ["US", "BR", "AU", "CA", "FR", "DE", "HK", "IN", "IT", "ES", "GB", "SG"].
		Any other value will default region to "US" (as implemented in rapidAPI GET market/v2/get-quotes).	 
