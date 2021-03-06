import tkinter as tk
from tkinter import filedialog

from tkvideo import tkvideo

from motion_detection import MotionDetector


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('OCMotDetVal')

        self.mog_file = "mog.mp4"
        self.mog2_file = "mog2.mp4"
        self.knn_file = "knn.mp4"

        self._set_frame('Original Video', 0, 0)
        self._set_frame('KNN', 1, 0)
        self._set_frame('MOG', 1, 1)
        self._set_frame('MOG2', 1, 2)

        self.filename = filedialog.askopenfilename()

        if not self.filename:
            self.destroy()
            return

        motion_detector = MotionDetector()

        motion_detector.detect(self.filename, self.knn_file, detector="KNN")
        motion_detector.detect(self.filename, self.mog_file, detector="MOG")
        motion_detector.detect(self.filename, self.mog2_file, detector="MOG2")

        self._play_video(self.filename, 0, 0)
        self._play_video(self.knn_file, 1, 0)

        self._play_video(self.mog_file, 1, 1)
        self._play_video(self.mog2_file, 1, 2)

    def _set_frame(self, text, row, column):
        row *= 2

        self.frame = tk.Frame(self, width=350, height=250, background='darkgrey')
        self.frame.grid(row=row, column=column)
        self.label = tk.Label(self, text=text)
        self.label.grid(row=row+1, column=column)

    def _play_video(self, filename, row, column):
        row *= 2

        label = tk.Label(self)
        label.grid(row=row, column=column)
        player = tkvideo(filename, label, loop=1, size=(350, 250))
        player.play()


if __name__ == "__main__":
    app = App()
    app.mainloop()
