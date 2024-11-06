import json, pyaudio

from vosk import Model, KaldiRecognizer

model = Model("vosk-model-small-uz-0.22")
rec = KaldiRecognizer(model, 1600)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]


for text in listen():
    if text == "xayr":
        quit()
    elif text == "Salom":
        print("Helllooo Buddy")
