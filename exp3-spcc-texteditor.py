import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def save(text):

    saveLoc = filedialog.asksaveasfilename()

    txt = text.get("1.0", tk.END)

    with open(saveLoc, 'w+') as f:

        f.write(txt)



def openF(text):

    openLoc = filedialog.askopenfilename()

    text.delete("1.0", tk.END)

    with open(openLoc, 'r+') as F:

        for i,f in enumerate(F):

            text.insert(str(i+1) + ".0", f)

def select_all(textbox):
    textbox.tag_add(tk.SEL, "1.0", tk.END)
    textbox.mark_set(tk.INSERT, "1.0")
    textbox.see(tk.INSERT)
    return 'break'

def make_bold(text):

    text.tag_add("BOLD",  tk.SEL_FIRST, tk.SEL_LAST)

def close(root):
    root.destroy()

def counter(x, wc, cc, text):

    txt = text.get("1.0", tk.END)

    txt = txt.strip(" ")
    w = len(txt.split())
    txt = txt.replace(" ", "")
    c = len(txt)-1

    wc.config(text="Word Count = "+str(w))
    cc.config(text="Char Count = " + str(c))

    # print(w , c)



top = tk.Tk()

top.geometry("750x600")





text = tk.Text(top)
text.grid( row=3, column=2 , ipadx=10, ipady=10 )



saveL = tk.Button(top , text="Save", command = lambda : save(text))
saveL.grid(  )

openL = tk.Button(top , text="Open", command = lambda : openF(text))
openL.grid(  )

Close = tk.Button(top , text="Close", command = lambda : close(top))
Close.grid(  )

wc = tk.Label(top, text="Word Count = 0")
wc.grid( column=2  )

cc = tk.Label(top, text="Char Count = 0")
cc.grid( column=2  )

tk.Label(top, text="Ctrl+S = Save").grid( column=2  , ipady = 5 )
tk.Label(top, text="Ctrl+O = Open").grid( column=2 , ipady = 5)
tk.Label(top, text="Ctrl+Q = Close").grid( column=2 , ipady = 5)

text.bind('<Control-s>' , lambda x: save(text))
text.bind('<Control-o>' , lambda x: openF(text))
text.bind('<Control-b>' , lambda x: make_bold(text))
text.bind('<Control-q>' , lambda x: close(top))
text.bind('<Control-a>' , lambda x: select_all(text))




text.bind('<KeyPress>', lambda x: counter(x, wc, cc, text))
text.bind('<KeyRelease>', lambda x: counter(x, wc, cc, text))


text.tag_configure("BOLD", font="bold")


top.mainloop()
