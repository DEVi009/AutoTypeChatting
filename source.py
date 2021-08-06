import keyboard as k
import time as t


x = input("enter the phrase you want to be at the start (default is Chatting): ") or "Chatting "

xkey = input('Add custom key or leave empty for default (F2)') or 'F2'

def WritePhrase():
    k.write(x)



def MoveCursorAndWrite():
    k.send('ctrl+a')
    k.send('left arrow')
    WritePhrase()
    k.send('enter')


while True:
    if(k.is_pressed(xkey)):
        MoveCursorAndWrite()
        t.sleep(0.5)
        