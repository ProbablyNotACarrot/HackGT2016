import requests
import settings
from GoogleTTS import audio_extract
translatedAudio = audio_extract(input_text='tunnel snakes rule apparently', args = {'language':'en','output':'outputto.mp3'})

# requires settings.py containing:
# API_KEY = "YOUR_API_KEY"

class GoogleTranslateSession(object):
	
	def __init__(self, api_key):
		self.API_KEY = api_key

	def translate(self, sourceLanguage, targetLanguage, text):
		url = ("https://www.googleapis.com/language/translate/v2?key=%s" +
				"&source=%s&target=%s&q=%s&client=p") % (self.API_KEY, 
				sourceLanguage, targetLanguage, text)

		return requests.get(url).json()["data"]["translations"][0]["translatedText"]

print GoogleTranslateSession(settings.API_KEY).translate("en", "fr", "Hello world")
