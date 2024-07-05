import time
import subprocess
from tkinter import Tk, Label

def show_popup():
    root = Tk()
    window_width = 400
    window_height = 200
    root.title("리마인더")
    label = Label(root, font=("Helvetica", 40),text="TURN OFF THE SHORTS!!!", padx=20, pady=20)
    label.pack(anchor='center')
    root.mainloop()

def check_youtube_shorts():
    while True:
        try:
            # 열려 있는 Window 의 리스트를 확보
            result = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE)
            windows = result.stdout.decode('utf-8').split('\n')
            
            # window 중에 "Youtube" 와 "shorts" 타이틀이 있는지 확인 

            for window in windows:
                if 'youtube' in window and 'shorts' in window.lower():
                    print("오 ㅋㅋ 유튭 쇼츠 켰네")
                    time.sleep(10) # 알람 뜨기까지 3분 기다려줄게~
                    show_popup()
                    return
        except Exception as e:
            print("Error : {e}")


def check_chrome_open():
    while True:
        try:
            # Check if Chrome is running
            result = subprocess.run(['pgrep', 'chrome'], stdout=subprocess.PIPE)
            if result.stdout:
                check_youtube_shorts()

        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(10)  # Check every 10 seconds


if __name__ == "__main__":
    check_youtube_shorts ()