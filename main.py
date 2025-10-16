import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:  # 클래스 생성
    def __init__(self, root):
        self.root = root
        self.root.title("간단한 메모장")
        self.root.geometry("800x600")

        # 텍스트 입력 영역 생성
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill="both")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = Notepad(main_window)
    main_window.mainloop()
