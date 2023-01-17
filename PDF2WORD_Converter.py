# READMEE
# Baca panduan ini dulu ya 
# Sebelum Menjalankan projectnya membutuhkan beberapa yang harus di install
# Seperti:
# pip install pdf2docx
# dan bagian initialdir di ganti dulu dengan default folder yang ingin
# kalian jadikan tempat import dan export

from tkinter import *
from tkinter import messagebox, filedialog
from pdf2docx import parse

root = Tk()
root.resizable(False, False)
root.config(bg='black')
root.geometry("300x190")
root.title("PDF to WORD Converter by Mee")


def file():
    global pdf
    pdf = filedialog.askopenfilename(initialdir="D:\Kuliah", title='Select File', filetype=(("PDF", "*.pdf"),("All Files", "*.*")))
    path.insert(0, str(pdf))


Label(root, text='Meee', font=('sans-serif', 20, 'bold', 'italic', 'underline'), bg='black', fg='#06beb6').pack(pady=10)
path=Entry(root,width=28, bd=0, font=('times', 15, 'italic'), bg='black', fg='gray')
path.pack()
Button(root, text='Pilih File PDFnya', command=file, bg='black', fg='white', activebackground='black', activeforeground="#ee9ca7", font=("rosemary", 15, "italic"), bd=0).pack()

def export():
    if len(path.get()) != 0 :
        word = filedialog.asksaveasfilename(initialdir="D:\Kuliah", title='Save As', defaultextension=".docx",
                                      filetype=(("Word", "*.docx"), ("All Files", "*.*")))
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