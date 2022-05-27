import tkinter as tk
from tkvideo import tkvideo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # set window title
        self.title('Video Player')
        # create label
        self.video_label = tk.Label(self)
        self.video_label.pack()
        # read video to display on label
        self.player = tkvideo("path/to/video.mp4", self.video_label,
                              loop=1, size=(700, 500))
        self.player.play()


if __name__ == "__main__":
    app = App()
    app.mainloop()
