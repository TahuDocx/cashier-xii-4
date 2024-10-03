import datetime
import pyglet

MONTH = [
   "Januari","Februari","Maret","Äpril","Mei","Juni",
   "Juli","Agustus","September","October","November","Desember",
        ]

DAY = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

class Clock:
    def __init__(self, x, y, batch, font_size=30):
        self.label = pyglet.text.Label("hai", font_size=font_size, x=x-40, y=y, anchor_x="right", anchor_y="top", height=60, align="right", width=400, batch=batch)

    def update(self):
        current_time = datetime.datetime.now()
        # time_tuple = time.timetuple()
        day = current_time.strftime("%w")
        str_day = DAY[int(day)]
        date = current_time.date()
        date_arr = str(date).split("-")
        date_arr[1] = int(date_arr[1])
        str_date = f"{date_arr[2]} {MONTH[date_arr[1]]} {date_arr[0]}"
        # print(str_date)
        # print(current_time)
        # print(time_tuple)
        # date_str = f"{date[2]} {MONTH[date[1]]} {date[0]}"
        time_str = current_time.strftime("%H:%M:%S")
        datetime_str = f"{str_day}, {str_date} - {time_str}"
        # print(datetime_str)
        self.label.text = datetime_str

class Title:
  def __init__(self, width, height, batch):
    self.title = "Warung Teknik XII-4"
    self.clock = Clock(x=width-40, y=height-20, batch=batch)
    self.container = pyglet.shapes.BorderedRectangle(x=0, y=height-100, height=100, width=width, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=batch)
    self.title_label = pyglet.text.Label(self.title, x=40, y=height-20, height=60, font_size=30, align="center", anchor_y="top", batch=batch)
