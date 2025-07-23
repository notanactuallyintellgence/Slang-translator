import tkinter as tk

my_word = {
    "ts": "this",
    "brb": "be right back",
    "idk": "i don't know",
    "fr": "for real",
    "lol": "laugh out loud"
}

window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("300x200")

lab = tk.Label(window, text="Slang Translator!")
lab.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

# Define label first
result_label = tk.Label(window, text="", wraplength=280, font=("Arial", 12))
result_label.pack(pady=10)

def on_click():
    user_in = entry.get()
    words = user_in.split()

    translated = []
    for word in words:
        if word in my_word:
            translated.append(my_word[word])
        else:
            translated.append(word)

    new = " ".join(translated)
    result_label.config(text=new)

translate_btn = tk.Button(window, text="Translate", command=on_click)
translate_btn.pack(pady=5)

window.mainloop()