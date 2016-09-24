import requests
from settings import API_KEY

# requires settings.py containing:
# API_KEY = "YOUR_API_KEY"

class GoogleTranslateSession(object):
	
	def __init__(self, api_key):
		self.API_KEY = api_key

	def translate(self, sourceLanguage, targetLanguage, text):
		url = ("https://www.googleapis.com/language/translate/v2?key=%s" +
				"&source=%s&target=%s&callback=translateText&q=%s") % (sourceLanguage,
				targetLanguage, self.API_KEY, text)

		return requests.get(url).json()

g = GoogleTranslateSession(API_KEY)
print g.translate("en", "de", "Hello")