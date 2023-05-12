from googletrans import Translator

def translate_lyrics(lyrics, source_lang):
    translator = Translator(service_urls=['translate.google.com'])
    translated_lyrics = translator.translate(lyrics, src=source_lang, dest='en').text
    return translated_lyrics

# Example usage
lyrics = "Despacito\nQuiero respirar tu cuello despacito"
source_lang = 'es'
translated_lyrics = translate_lyrics(lyrics, source_lang)
print(translated_lyrics)
