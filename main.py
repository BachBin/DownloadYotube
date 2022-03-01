import _thread
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from plyer import notification
from pytube import YouTube

direct = ""


def toast(title):
    notification.notify(
        title="Video đã được tải xuống",
        message="Video: "+title+" đã được tải xuống",
        timeout=10,
        app_icon="ytb.ico"
    )


def show_progress_bar(stream, chunk, bytes_remaining):
    progress = int(((stream.filesize - bytes_remaining) / stream.filesize) * 100)
    bar['value'] = progress


def open_path():
    global direct
    direct = filedialog.askdirectory()
    entry_path.set(direct)
    if len(direct) == 0:
        msb_path = messagebox.showwarning('Cảnh báo', 'Chọn đường dẫn lưu video.')
    else:
        pass


def Download():
    url = link_entry.get()
    if len(url) == 0:
        msb_url = messagebox.showwarning('Cảnh báo', 'Nhập đường dẫn video youtube.')
        return
    else:
        pass
    select = cb_types.get()
    Yt = YouTube(url, on_progress_callback=show_progress_bar)
    if (select == options[0]):
        typ = Yt.streams.get_highest_resolution()
    elif (select == options[1]):
        typ = Yt.streams.filter(progressive=True, file_extension="mp4").first()
    elif (select == options[2]):
        typ = Yt.streams.filter(only_audio=True).first()

    typ.download(direct)
    toast(typ.title)


window = Tk()
window.title("Youtube Download")
windowWidth = 470
windowHeight = 220

global screen_height, screen_width, x_cordinate, y_cordinate

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x_cordinate = int((screen_width / 2) - (windowWidth / 2))
y_cordinate = int((screen_height / 2) - (windowHeight / 2))

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x_cordinate, y_cordinate))

window.resizable(False, False)
window.config(bg='white')

# label URL
link = Label(window, text="URL Youtube:", background='white', foreground='black', font='arial 10')
link.place(x=20, y=10)

# textbox url
entry_url = StringVar()
link_entry = Entry(window, width=52, textvariable=entry_url)
link_entry.place(x=130, y=10)

# label path save
path = Label(window, text="Output Directory:", background='white', foreground='black', font='arial 10')
path.place(x=20, y=40)

# textbox directory output
entry_path = StringVar()
link_path = Entry(window, width=40, textvariable=entry_path)
link_path.place(x=130, y=40)

# button choose path
btn_brower = Button(window, width=10, text="Chọn", command=open_path)
btn_brower.place(x=380, y=38)

# label chế độ tải
download_type = Label(window, text="Download Type:", background='white', foreground='black', font='arial 10')
download_type.place(x=20, y=70)

# combobox chất lượng video
options = ["Video chất lượng cao", "Video chất lượng thấp", "Chỉ âm thanh"]
cb_types = ttk.Combobox(window, value=options, width=49)
cb_types.current(0)
cb_types.place(x=130, y=70)

# thanh tiến trình
bar = ttk.Progressbar(window, length=320)
bar.place(x=130, y=110)

# button tải
btn_download = Button(window, width=26, text="Tải Video", command=lambda: _thread.start_new_thread(Download, ()))
btn_download.place(x=200, y=145)

# label copyright
copyright = Label(window, text="© Copyright Bạch Bin", background='white', foreground='black', font='arial 8')
copyright.place(x=240, y=190)
window.mainloop()
