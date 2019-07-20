import speech_recognition as sr
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

try:
    text = r.recognize_sphinx(audio, "ru-RU")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    
text = text.split(' ')

for i in range (len(text)):
    text[i] = morph.parse(text[i])[0].normal_form
#Теперь в text - распознанные слова в нормальной форме

#интенты (слова, позволяющие её определить) и возможные аргументы команды move (едь)
move_intents = ['поехать', 'ехать', 'едь', 'катиться']
move_args = ['сюда'] #ко мне, к Петру Петровичу

intersection = [i for i in text if i in move_intents]
if intersection:
  args = [i for i in text if i in move_args]
  #выполнение команды с использованием аргументов
