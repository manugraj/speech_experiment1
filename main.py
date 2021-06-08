import speech_recognition as sr
import pyaudio
import text2emotion as te


def start_transcription() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('> Adjusting for ambient noise')
        r.adjust_for_ambient_noise(source, duration=5)
        print('\t>> Start speaking...')
        audio = r.listen(source)
        print("\t\t>> Speech transcription complete")
    try:
        return r.recognize_google(audio)
    except Exception as e:
        print(e)


def what_emotion(text):
    return te.get_emotion(text)


def main():
    test = start_transcription()
    print(f'TEXT: {test}')
    print(f'EMOTION: {what_emotion(test)}')


if __name__ == '__main__':
    main()
