# Magic 8 ball project
import random, time, tkinter as tk


responses = ["Most definitely", 
             "Likely", 
             "Never", 
             "Always", 
             "You are crazy for even asking this question", 
             "Over my dead body", 
             "I'm too lazy to finish this list"]

def question():
    if answer_disp["text"]:
        return
    answer_disp["text"] = "Thinking..."
    time.sleep(1)
    random_response = responses[random.randint(0, len(responses) - 1)]
    answer_disp["text"] = random_response

def clear():
    question_entry.delete(0,"end")
def restart():
    answer_disp["text"] = ""

root = tk.Tk()
root.geometry('600x200')
root.resizable(False, False)
root.title('Magic 8-Ball')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=2)
root.grid_rowconfigure(3, weight=2)


q = tk.StringVar()

message1 = tk.Label(root, text="Please enter your question: ")
message1.grid(row = 0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

question_entry = tk.Entry(root, textvariable=q)
question_entry.grid(row = 0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
question_entry.focus()

message2 = tk.Label(root, text="Answer: ")
message2.grid(row = 1, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

answer_disp = tk.Label(root, text="")
answer_disp.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

button1 = tk.Button(root, text="Ask question", command=question)
button1.grid(column=0, row = 2, sticky=(tk.N, tk.S, tk.E, tk.W))

button2 = tk.Button(root, text="Clear question", command=clear)
button2.grid(column=1, row = 2, sticky=(tk.N, tk.S, tk.E, tk.W))

button3 = tk.Button(root, text="Play again", command=restart)
button3.grid(column=0, row = 3, sticky=(tk.N, tk.S, tk.E, tk.W))

button4 = tk.Button(root, text="Quit", command=lambda: root.quit())
button4.grid(column=1, row = 3, sticky=(tk.N, tk.S, tk.E, tk.W))

root.mainloop()

