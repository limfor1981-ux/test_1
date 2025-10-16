import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:  # 클래스 생성
    def __init__(self, root):
        self.root = root
        self.root.title("제목 없음 - 메모장")
        self.root.geometry("800x600")

        # 현재 파일 경로 저장 변수
        self.current_file_path = None

        # 텍스트 입력 영역 생성
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill="both")

        # 메뉴바 생성
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # 파일 메뉴
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="파일", menu=file_menu)
        file_menu.add_command(label="새로 만들기", command=self.new_file)
        file_menu.add_command(label="열기", command=self.open_file)
        file_menu.add_command(label="저장", command=self.save_file)
        file_menu.add_command(label="다른 이름으로 저장", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.exit_app)

        # 편집 메뉴
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="편집", menu=edit_menu)
        edit_menu.add_command(label="실행 취소", command=self.text_area.edit_undo)
        edit_menu.add_command(label="다시 실행", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="잘라내기", command=self.cut_text)
        edit_menu.add_command(label="복사", command=self.copy_text)
        edit_menu.add_command(label="붙여넣기", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="모두 선택", command=self.select_all)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file_path = None
        self.root.title("제목 없음 - 메모장")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file_path = file_path
                self.root.title(f"{file_path} - 메모장")
            except Exception as e:
                messagebox.showerror("오류", f"파일을 여는 중 오류가 발생했습니다: {e}")

    def save_file(self):
        if self.current_file_path:
            try:
                with open(self.current_file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.root.title(f"{self.current_file_path} - 메모장")
            except Exception as e:
                messagebox.showerror("오류", f"파일을 저장하는 중 오류가 발생했습니다: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.current_file_path = file_path
            self.save_file() # 저장 로직 재사용

    def exit_app(self):
        self.root.quit()

    def cut_text(self): self.text_area.event_generate("<<Cut>>")
    def copy_text(self): self.text_area.event_generate("<<Copy>>")
    def paste_text(self): self.text_area.event_generate("<<Paste>>")
    def select_all(self): self.text_area.tag_add("sel", "1.0", "end")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = Notepad(main_window)
    main_window.mainloop()