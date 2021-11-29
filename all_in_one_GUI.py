import platform
import sys
from threading import Thread
import tkinter as tk
import tkinter.ttk as ttk
import all_in_one_GUI_support
import threading
import os

py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    all_in_one_GUI_support.set_Tk_var()
    top = Toplevel1(root)
    all_in_one_GUI_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    all_in_one_GUI_support.set_Tk_var()
    top = Toplevel1(w)
    all_in_one_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        if hasattr(sys, "_MEIPASS"):
            work_dir = sys._MEIPASS
        else:
            work_dir = os.getcwd()

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.iconbitmap(os.path.normpath(os.path.join(work_dir, "car.ico")))
        top.geometry("1116x664+125+34")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("@for Suiken")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.018, rely=0.06, height=20, relwidth=0.165)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(textvariable=all_in_one_GUI_support.input_i)
        self.Entry1.bind('<Return>', lambda v: threading.Thread(target=all_in_one_GUI_support.main, daemon=True).start())

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.215, rely=0.06, height=24, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=lambda: threading.Thread(target=all_in_one_GUI_support.main, daemon=True).start())
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Искать''')

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(top)
        self.Scrolledtreeview1.place(
            relx=0.081, rely=0.136, relheight=0.795, relwidth=0.911)
        self.Scrolledtreeview1.configure(columns="Col1 Col2 Col3 Col4 Col5")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0", text="Tree")
        self.Scrolledtreeview1.heading("#0", anchor="center")
        self.Scrolledtreeview1.column("#0", width="1")
        self.Scrolledtreeview1.column("#0", minwidth="1")
        self.Scrolledtreeview1.column("#0", stretch="0")
        self.Scrolledtreeview1.column("#0", anchor="center")
        self.Scrolledtreeview1.heading("Col1", text="Сайт")
        self.Scrolledtreeview1.heading("Col1", anchor="center")
        self.Scrolledtreeview1.column("Col1", width="117")
        self.Scrolledtreeview1.column("Col1", minwidth="80")
        self.Scrolledtreeview1.column("Col1", stretch="1")
        self.Scrolledtreeview1.column("Col1", anchor="e")
        self.Scrolledtreeview1.heading("Col2", text="Артикул")
        self.Scrolledtreeview1.heading("Col2", anchor="center")
        self.Scrolledtreeview1.column("Col2", width="118")
        self.Scrolledtreeview1.column("Col2", minwidth="80")
        self.Scrolledtreeview1.column("Col2", stretch="1")
        self.Scrolledtreeview1.column("Col2", anchor="e")
        self.Scrolledtreeview1.heading("Col3", text="Цена")
        self.Scrolledtreeview1.heading("Col3", anchor="center")
        self.Scrolledtreeview1.column("Col3", width="117")
        self.Scrolledtreeview1.column("Col3", minwidth="80")
        self.Scrolledtreeview1.column("Col3", stretch="1")
        self.Scrolledtreeview1.column("Col3", anchor="e")
        self.Scrolledtreeview1.heading("Col4", text="Бренд")
        self.Scrolledtreeview1.heading("Col4", anchor="center")
        self.Scrolledtreeview1.column("Col4", width="117")
        self.Scrolledtreeview1.column("Col4", minwidth="80")
        self.Scrolledtreeview1.column("Col4", stretch="1")
        self.Scrolledtreeview1.column("Col4", anchor="e")
        self.Scrolledtreeview1.heading("Col5", text="Описание")
        self.Scrolledtreeview1.heading("Col5", anchor="center")
        self.Scrolledtreeview1.column("Col5", width="528")
        self.Scrolledtreeview1.column("Col5", minwidth="200")
        self.Scrolledtreeview1.column("Col5", stretch="1")
        self.Scrolledtreeview1.column("Col5", anchor="w")
############################
        def popup(event):
            try:
                self.menu.tk_popup(event.x_root,event.y_root) # Pop the menu up in the given coordinates
            finally:
                self.menu.grab_release() # Release it once an option is selected

        def paste():
            clipboard = top.clipboard_get() # Get the copied item from system clipboard
            self.Entry1.insert('end',clipboard) # Insert the item into the entry widget

        def copy():
            inp = self.Entry1.get() # Get the text inside entry widget
            top.clipboard_clear() # Clear the tkinter clipboard
            top.clipboard_append(inp) # Append to system clipboard

        self.menu = tk.Menu(top,tearoff=0) # Create a menu
        self.menu.add_command(label='Копировать',command=copy) # Create labels and commands
        self.menu.add_command(label='Вставить',command=paste)

        self.Entry1.bind('<Button-3>',popup) # Bind a func to right click

    ############################
        rev = {"#%d"%x:False for x in range(1,5)}
        def treeview_sort_column(tv, col):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            try:
                l.sort(key=lambda t: int(t[0]), reverse=rev[col])
            except ValueError:
                l.sort(reverse=rev[col])
            for k in rev.keys():
                tv.heading(k,text=tv.heading(k,"text").replace("v","").replace("^",""))
            tv.heading(col,text=["^","v"][rev[col]]+tv.heading(col,"text"))
            rev[col]=not rev[col]
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

        self.Scrolledtreeview1.heading("Col1", command=lambda:treeview_sort_column(self.Scrolledtreeview1,"#1"))
        self.Scrolledtreeview1.heading("Col2", command=lambda:treeview_sort_column(self.Scrolledtreeview1,"#2"))
        self.Scrolledtreeview1.heading("Col3", command=lambda:treeview_sort_column(self.Scrolledtreeview1,"#3"))
        self.Scrolledtreeview1.heading("Col4", command=lambda:treeview_sort_column(self.Scrolledtreeview1,"#4"))
        self.Scrolledtreeview1.heading("Col5", command=lambda:treeview_sort_column(self.Scrolledtreeview1,"#4"))
############################
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.636, rely=0.045, height=32, width=384)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.305, rely=0.0, height=31, width=333)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        # self.Label2.configure(text='''Label''')



        # self.menubar = tk.Menu(top, font="TkMenuFont",
        #                        bg=_bgcolor, fg=_fgcolor)
        # top.configure(menu=self.menubar)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.009, rely=0.377, height=24, width=77)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''autoeuro''')
        self.Button2.configure(command=all_in_one_GUI_support.autoeuro_link)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.009, rely=0.422, height=24, width=77)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''pasker''')
        self.Button3.configure(command=all_in_one_GUI_support.pasker_link)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.009, rely=0.467, height=24, width=77)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''ixora''')
        self.Button4.configure(command=all_in_one_GUI_support.ixora_auto_link)

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.009, rely=0.512, height=24, width=77)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''autorus''')
        self.Button5.configure(command=all_in_one_GUI_support.autorus_link)

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.009, rely=0.557, height=24, width=77)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''rossko''')
        self.Button6.configure(command=all_in_one_GUI_support.rossko_link)

        self.Button7 = tk.Button(top)
        self.Button7.place(relx=0.009, rely=0.602, height=24, width=77)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''autopiter''')
        self.Button7.configure(command=all_in_one_GUI_support.autopiter_link)

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(
            relx=0.305, rely=0.06, relwidth=0.299, relheight=0.0, height=22)
        self.TProgressbar1.configure(length="334")

        self.Label2 = tk.Label(top)
        self.Label1.place(relx=0.636, rely=0.015, height=42, width=384)
        # self.Label2.place(relx=0.018, rely=0.015, height=21, width=184)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Введите артикул:''')
        self.Label2.configure(anchor=w)

# The following code is added to facilitate the Scrolled widgets you specified.


class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind(
            '<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>',
                       lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
