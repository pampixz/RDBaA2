import unittest
from refpaint2 import PaintLogic  # Импортируем логику из рефакторинга


class TestPaintLogic(unittest.TestCase):
    def setUp(self):
        """Создает новый экземпляр логики перед каждым тестом."""
        self.paint_logic = PaintLogic()

    def test_initial_values(self):
        """Проверяет начальные параметры."""
        self.assertEqual(self.paint_logic.color, 'black')
        self.assertEqual(self.paint_logic.line_width, 5.0)
        self.assertFalse(self.paint_logic.eraser_on)

    def test_set_color(self):
        """Проверяет изменение цвета."""
        self.paint_logic.set_color('red')
        self.assertEqual(self.paint_logic.color, 'red')

    def test_set_eraser(self):
        """Проверяет включение и выключение ластика."""
        self.paint_logic.set_eraser(True)
        self.assertTrue(self.paint_logic.eraser_on)

        self.paint_logic.set_eraser(False)
        self.assertFalse(self.paint_logic.eraser_on)

    def test_set_line_width(self):
        """Проверяет изменение толщины кисти."""
        self.paint_logic.set_line_width(8)
        self.assertEqual(self.paint_logic.line_width, 8)

    def test_reset_position(self):
        """Проверяет сброс координат."""
        self.paint_logic.old_x = 10
        self.paint_logic.old_y = 20
        self.paint_logic.reset_position()
        self.assertIsNone(self.paint_logic.old_x)
        self.assertIsNone(self.paint_logic.old_y)


if __name__ == '__main__':
    unittest.main()