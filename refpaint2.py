from tkinter import *
from tkinter.colorchooser import askcolor


class PaintLogic:
    """Логика работы приложения для рисования (без GUI)."""

    def __init__(self, default_color='black', default_size=5.0):
        self.color = default_color
        self.line_width = default_size
        self.eraser_on = False
        self.old_x = None
        self.old_y = None

    def set_color(self, new_color):
        """Устанавливает новый цвет кисти."""
        self.color = new_color

    def set_eraser(self, is_active):
        """Включает или выключает режим ластика."""
        self.eraser_on = is_active

    def set_line_width(self, width):
        """Устанавливает толщину линии."""
        self.line_width = width

    def reset_position(self):
        """Сбрасывает координаты."""
        self.old_x, self.old_y = None, None


class PaintApp:
    """Графический интерфейс для рисования на Tkinter."""

    def __init__(self):
        self.root = Tk()
        self.root.title("Paint App")

        self.logic = PaintLogic()  # Используем логику рисования

        self.pen_button = Button(self.root, text='Карандаш', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.eraser_button = Button(self.root, text='Ластик', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='Выбрать цвет', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.size_slider = Scale(self.root, from_=1, to=10, orient=HORIZONTAL, command=self.update_line_width)
        self.size_slider.grid(row=0, column=3)

        self.canvas = Canvas(self.root, bg='white', width=600, height=600)
        self.canvas.grid(row=1, columnspan=4)

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.root.mainloop()

    def choose_color(self):
        color = askcolor(color=self.logic.color)[1]
        if color:
            self.logic.set_color(color)

    def use_pen(self):
        self.logic.set_eraser(False)

    def use_eraser(self):
        self.logic.set_eraser(True)

    def update_line_width(self, value):
        self.logic.set_line_width(int(value))

    def paint(self, event):
        paint_color = 'white' if self.logic.eraser_on else self.logic.color
        if self.logic.old_x and self.logic.old_y:
            self.canvas.create_line(
                self.logic.old_x, self.logic.old_y, event.x, event.y,
                width=self.logic.line_width, fill=paint_color,
                capstyle=ROUND, smooth=TRUE, splinesteps=36
            )
        self.logic.old_x = event.x
        self.logic.old_y = event.y

    def reset(self, event):
        self.logic.reset_position()


if __name__ == '__main__':
    PaintApp()