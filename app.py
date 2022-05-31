import tkinter as tk
from tkinter import filedialog

from tkvideo import tkvideo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('OCMotDetVal')

        self._set_frame('Original Video', 0, 0)
        self._set_frame('KNN', 1, 0)
        self._set_frame('MOG', 1, 1)
        self._set_frame('MOG2', 1, 2)

        self.upload_button = tk.Button(self, text='Open',
                                       command=lambda: self._upload_action())
        self.upload_button.grid(row=0, column=2)

        # create labels for videos
        self.upload_label = tk.Label(self)
        self.knn_label = tk.Label(self)
        self.mog_label = tk.Label(self)
        self.mog2_label = tk.Label(self)

    def _set_frame(self, text, row, column):
        row *= 2
        self.frame = tk.Frame(self, width=350, height=250, background='darkgrey')
        self.frame.grid(row=row, column=column)
        self.label = tk.Label(self, text=text)
        self.label.grid(row=row+1, column=column)

    def _upload_action(self, event=None):
        self.filename = filedialog.askopenfilename()

        if self.filename == '':
            return

        self._play_video(self.filename, self.upload_label, 0, 0)
        self._play_video(self.filename, self.knn_label, 1, 0)
        self._play_video(self.filename, self.mog_label, 1, 1)
        self._play_video(self.filename, self.mog2_label, 1, 2)

    def _play_video(self, filename, label, row, column):
        try:
            label.destroy()
        except AttributeError:
            pass

        row *= 2

        label = tk.Label(self)
        label.grid(row=row, column=column)
        player = tkvideo(filename, label, loop=1, size=(350, 250))
        player.play()


if __name__ == "__main__":
    app = App()
    app.mainloop()
