from tkinter import *
from tkinter.messagebox import askokcancel
from Bio import Entrez
Entrez.email = 'lw325911@163.com'
class BioTk(Frame):
    def __init__(self,parent = None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        self.lab = Label(self, width=1, text="ID")
        self.ent = Entry(self)
        self.lab.grid(row=0, column=1)
        self.ent.grid(row=0, column=2)
        self.var = StringVar()
        self.R1 = Radiobutton(self, text='nucleotide', command=self.onPress, variable=self.var, value='nucleotide')
        self.R2 = Radiobutton(self, text='protein', command=self.onPress, variable=self.var, value='protein')
        self.R1.grid(row=1, column=1)
        self.R2.grid(row=1, column=2)
        self.var.set("nucleotide")
        Button(self, text="Fetch", command=(lambda: self.download_seq(self.ent))).grid(row=2,column=1)
        Button(self,text="quit",command=self.quit).grid(row=2,column=2)
    def quit(self):
        ans = askokcancel('Verify exit',"Really quit?")
        if ans:
            Frame.quit(self)
    def download_seq(self,ent):
        db = ""
        if self.var.get() == "nucleotide":
            db = "nucleotide"
        elif self.var.get() == "protein":
            db = "protein"
        else:
            print("error")
        accs = list(set(ent.get().split(",")))
        fout = open("sequence.txt", 'w')
        try:
            for acc in accs:
                handle = Entrez.efetch(db=db, id=acc, rettype='fasta', retmode='txet')
                data = handle.read()
                fout.write(data)
        except Exception as e:
            print(e)
        fout.close()
    def onPress(self):
        pick = self.var.get()
        print('you pressed',pick)

if __name__ == "__main__":
    BioTk().mainloop()