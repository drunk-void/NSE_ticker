import tkinter as tk
from nsetools import Nse
nse = Nse()


class driver(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        mainframe = tk.Frame(self)
        mainframe.grid(column=0, row=0, sticky="nwes")
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        home = homePage(mainframe, self)
        show_frame(home)


class stock(tk.Frame):
    def __init__(self, stockCode, parent):
        self.code = stockCode.get()
        self.stockData = nse.get_quote(self.code)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Market data of " +
                         self.stockData['companyName'])
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
    def __init__(self, parent, driver):
        self.code = tk.StringVar()
        self.par=parent
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.grid(column=1, row=1, sticky="e")
        search = tk.Entry(self, width=7, textvariable=self.code)
        search.grid(column=2, row=1, sticky="we")
        b = tk.Button(self, text="Start",
                      command=lambda: showStock(self.code, parent))
        b.grid(column=2, row=2, sticky="s")
        search.focus()
        # driver.bind('<Return>', lambda : self.s)

    """ def s(self):
        cc = self.code
        parent = self.par
        showStock(cc, parent) """

root = driver()
root.title("NSE Tracker")
root.mainloop()
