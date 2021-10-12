import speech_recognition as sr

r = sr.Recognizer()


def convert(file_path):
    with sr.AudioFile(file_path) as source:
        audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, language="ru_RU"))
            print('working on...')
            return text
        except:
            return 'Произошла ошибка при распозновании текста. Убедитесь, что вы загружаете файл формата .wav'
