from translate import Translator
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def translate_text(text, dest_language):
    try:
        language_map = {
            'hindi': 'hi', 'spanish': 'es', 'french': 'fr', 'german': 'de',
            'english': 'en', 'chinese': 'zh', 'japanese': 'ja', 'russian': 'ru',
            'arabic': 'ar', 'bengali': 'bn', 'tamil': 'ta', 'telugu': 'te',
            'marathi': 'mr', 'gujarati': 'gu'
        }
        lang_code = language_map.get(dest_language.lower(), 'hi')
        translator = Translator(to_lang=lang_code)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"Translation error: {e}")
        return None

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    language = input("Translate to (language name): ")
    result = translate_text(text, language)
    if result:
        speak(f"Translation: {result}")
    else:
        speak("Could not translate the text.")


