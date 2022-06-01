import cv2



class MotionDetector:

    def __init__(self, video_width = 300, video_height = 300):
        self.video_width = video_width
        self.video_height = video_height
        self.detectors = {"MOG":cv2.bgsegm.createBackgroundSubtractorMOG(),
                          "MOG2":cv2.createBackgroundSubtractorMOG2(),
                          "KNN":cv2.createBackgroundSubtractorKNN(detectShadows=False)}

    def detect(self, input_file, output_file, detector="MOG2"):
        capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(input_file))
        out = cv2.VideoWriter(output_file, -1, 10, (self.video_width, self.video_height))
        if not capture.isOpened():
            print('Unable to open file')
            exit(0)
        while True:
            ret, frame = capture.read()
            if frame is None:
                break

            resize = cv2.resize(frame, (self.video_width, self.video_height))
            fgMask = self.detectors[detector].apply(resize)
            out.write(fgMask)