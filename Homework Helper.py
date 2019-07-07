from tkinter import *
import wikipedia
import pyttsx3
root = Tk()



engine = pyttsx3.init()
voices = engine.getProperty('voices') 
print(voices[0].id)   #getting details of current voice
print(voices[1].id)   
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSSam')

 # =========== function aare here ============
def show_answer():
    input1 = query.get()
    asnwer = wikipedia.summary(input1, sentences=3)
    answer_shower.insert(END, asnwer)

def erase_text():
    answer_shower.delete(1.0, END)

def speak_answer():
    input1 = query.get()
    asnwer = wikipedia.summary(input1, sentences=3)
    engine.say(asnwer)
    engine.runAndWait()
    engine.stop()

input_help = Label(root, text="Ask Anything: ")
input_help.grid(row=1, column=0)

query = StringVar()
take_input = Entry(root, width=25, textvariable=query)
take_input.grid(row=1, column=1)

answer_shower = Text(root, width=100, height=20)
answer_shower.grid(row=2, columnspan=3, pady=20, padx=10)

button = Button(root, text="Find Answer", command=show_answer)
button.grid(row=2, column=3)

button2 = Button(root, text="Clear", command=erase_text)
button2.grid(row=2, column=4, padx=5)

button3 = Button(root, text="Speak", command=speak_answer)
button3.grid(columnspan=4)

root.geometry("1300x700")
root.resizable(0,0)
root.title("Find Everthing!")
root.mainloop()
