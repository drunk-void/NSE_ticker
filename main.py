import tkinter as tk
from nsetools import Nse
nse = Nse()


class stock(tk.Frame):
    def __init__(self, stockCode, parent):
        self.code = stockCode.get()
        self.stockData = nse.get_quote(self.code)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Market data of " +
                         self.code)
        label.grid(column=2, row=1, sticky="n")
        label = tk.Label(self, text="Market depth ")
        label.grid(column=1, row=2, sticky="n")
        label = tk.Label(self, text="LTP")
        label.grid(column=2, row=2, sticky="n")
        button = tk.Button(self, text="Exit", command=root.destroy)
        button.grid(column=3, row=2, sticky="n")
        label = tk.Label(self, text=self.stockData['lastPrice'])
        label.grid(column=2, row=3, sticky="n")


def show_frame(a):
    a.grid(row=0, column=0, sticky="nsew")
    a.tkraise()


def showStock(code, parent):
    a = stock(code, parent)
    show_frame(a)


class homePage(tk.Frame):
    def __init__(self, parent):
        self.code = tk.StringVar()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.grid(column=1, row=1, sticky="e")
        search = tk.Entry(self, width=7, textvariable=self.code)
        search.grid(column=2, row=1, sticky="we")
        b = tk.Button(self, text="Start",
                      command=lambda: showStock(self.code, parent))
        b.grid(column=2, row=2, sticky="s")


root = tk.Tk()
root.title("NSE Tracker")
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky="nwes")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
home = homePage(mainframe)
show_frame(home)
root.mainloop()
