from tkinter import *
from pytube import YouTube

def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    quality = quality_var.get()
    
    if quality == "high":
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.get_lowest_resolution()
        
    video.download()
    status_label.config(text="تم التحميل بنجاح!")

# إعداد نافذة التطبيق
window = Tk()
window.title("YouTube Video Downloader")
window.geometry("400x250")

# حقل إدخال الرابط
Label(window, text="أضف رابط يوتيوب هنا:").pack(pady=10)
url_entry = Entry(window, width=50)
url_entry.pack(pady=10)

# خيارات الجودة
quality_var = StringVar(value="high")
Label(window, text="اختر الجودة:").pack(pady=10)
Radiobutton(window, text="عالي الجودة", variable=quality_var, value="high").pack()
Radiobutton(window, text="منخفض الجودة", variable=quality_var, value="low").pack()

# زر التحميل
download_button = Button(window, text="تحميل الفيديو", command=download_video)
download_button.pack(pady=20)

# حالة التحميل
status_label = Label(window, text="")
status_label.pack()

# بدء حلقة التطبيق
window.mainloop()