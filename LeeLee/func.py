from posixpath import dirname
from pynput.mouse import Listener
import keyboard
import win32clipboard
import time
import os
import gtts
import speech_recognition as sr
from playsound import playsound
import tkinter as tk
from googletrans import Translator, constants
from random import randint
import speech_recognition as sr

global data

def get_audio():
    r = sr.Recognizer()
    global said
    
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            data = r.recognize_google(audio,language="fr-FR")
            data2 = r.recognize_google(audio,language="es-ES")
            tts = gtts.gTTS(data)
            tts = gtts.gTTS(data2)
            translator = Translator()
            detection = translator.detect(data)
            detection2 = translator.detect(data2)
            if "fr" in detection.lang:
             print(f"{detection}")
             print(data)
            if "es" in detection2.lang:
             print(f"{detection2}")
             print(data2)
             data=data2

        except Exception as e:
            print("Exception: " + str(e))
    return data

def translate(data):
    tts = gtts.gTTS(data)
    translator = Translator()
    detection = translator.detect(data)
    print("Language code:", detection.lang)
    print("Confidence:", detection.confidence)
    
    if "fr" in detection.lang:
        translation=translator.translate(data,src="fr",dest="es")
        print(f"{translation.text}")
        tts = gtts.gTTS(text=translation.text, lang='es-ES',tld="com.mx")
    if "es" in detection.lang:
        translation=translator.translate(data,src="es",dest="fr")
        tts = gtts.gTTS(text=translation.text, lang='FR-fr')
        print(f"{translation.text}")
    if "en" in detection.lang:
        translation=translator.translate(data,src="en",dest="fr")
        tts = gtts.gTTS(text=translation.text, lang='FR-fr')
        print(f"{translation.text}")
    value = randint(0,100)
      
    tts.save("Read" + str(value) + ".mp3")                       
    playsound("Read" + str(value) + ".mp3")

def translate_text(data):
    global tts
    tts = gtts.gTTS(data)
    translator = Translator()
    detection = translator.detect(data)
    print("Language code:", detection.lang)
    print("Confidence:", detection.confidence)
    
    if "fr" in detection.lang:
        tts = gtts.gTTS(text=data, lang='fr-FR')
        print(data)
        
    if "en" in detection.lang:
        tts = gtts.gTTS(text=data, lang='en-US')
        print(data)
    if "es" in detection.lang:
        tts = gtts.gTTS(text=data, lang='es-ES', tld='com.mx')
        print(data)        
    value = randint(0,100)
      
    tts.save("Read" + str(value) + ".mp3")                       
    playsound("Read" + str(value) + ".mp3")
    
def ChangeName():
    window = tk.Tk()

    window.title("Save As")
    window.minsize(150,100)
    window.attributes('-topmost', True)
    window.eval('tk::PlaceWindow . center')
    window.update()

    def clickMe():
        label.configure(text= 'Hello ' + name.get())
        
        global name2
        global weburl
        name2 = name.get()
        weburl = url.get()
        window.destroy()

    label = tk.Label(window, text = "Enter Name of file to save")

    url = tk.StringVar()
    name = tk.StringVar()
    name_label = tk.Label(window, text = 'Name', font=('calibre',10, 'bold'))
    name_entry = tk.Entry(window,textvariable = name, font=('calibre',10,'normal'))
    
    
    url_label = tk.Label(window, text = 'URL', font=('calibre',10, 'bold'))
    url_entry = tk.Entry(window,textvariable = url, font=('calibre',10,'normal'))
    button = tk.Button(window, text = "Save", command = clickMe)
    
    
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    url_label.grid(row=1,column=0)
    url_entry.grid(row=1,column=1)
    button.grid(row=2,column=1)
    
    window.mainloop()
  
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:

        copy = keyboard.press_and_release('ctrl+c')
        time.sleep(0.1)
        win32clipboard.OpenClipboard()
        global data 
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        print(data)
        return False

def WriteFile(text,weburl,name2):

    with open('KB/Write'+str(name2)+'.txt', 'a') as f:
        if weburl:
            if 'KB/Write'+str(name2)+'.txt':
                f = open('KB/Write'+str(name2)+'.txt','r+')
                lines = f.readlines() # read old content
                f.seek(0) # go back to the beginning of the file
                f.write(weburl+"\n") # write new content at the beginning
                for line in lines: # write old content after new
                    f.write(line)
                f.write(text)    
                f.close()
            else:
                f.write(weburl+"\n")
                f.write(text+"\n")
        else:
             f.write(text+"\n")


def main():
    
    while True:  

        try:
                
                if keyboard.is_pressed('alt+q'):  
                    with Listener(
                        on_click=on_click
                        ) as listener:
                            listener.join()                                               
                            translate_text(data)


                            
                   
                if keyboard.is_pressed('alt+t'): 
                        with Listener(
                            on_click=on_click
                            
                        ) as listener:                           
                            listener.join() 
                            print(listener)
                            translate(data)
        
                            
                                  
                if keyboard.is_pressed('ctrl+p'):
                        print('quitting')
                        break
                if keyboard.is_pressed('alt+s'):
                        win32clipboard.OpenClipboard()
                        text = win32clipboard.GetClipboardData()
                        win32clipboard.CloseClipboard()
                        ChangeName()
                        WriteFile(text,weburl,name2)

                if keyboard.is_pressed('alt+m'):
                    
                        cwd = os.getcwd() 
                        path = os.path.realpath(cwd)
                        os.startfile(path+"\KB")
                if keyboard.is_pressed('alt+i'):
                        print("listening")
                        voice = get_audio()
                        translate(voice)
                        print(voice)
                        
        except:
            break 
