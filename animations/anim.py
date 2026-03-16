from manim import *

GLOBAL_SHIFT_UP = UP*0.5

class AIHeaderGeneratorDemo(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- текстовое поле ---
        input_box = RoundedRectangle(
            width=10,
            height=4,
            corner_radius=0.2
        ).set_stroke(WHITE, width=3)
        input_box.shift(UP*1.5 + GLOBAL_SHIFT_UP)
        self.play(Create(input_box))

        # --- текст поста ---
        post_text = (
            "in recent years, neural networks have revolutionized many fields. "
            "from image recognition to natural language processing, "
            "these models are capable of learning complex patterns..."
        )

        # --- разбиваем на строки ---
        max_chars_per_line = 60
        words = post_text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            if len(current_line + " " + word) <= max_chars_per_line:
                current_line += " " + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        # --- создаём текстовые объекты для каждой строки ---
        text_objects = []
        top_left = input_box.get_top() + LEFT*input_box.width/2 + RIGHT*0.2 + DOWN*0.2
        for i, line in enumerate(lines):
            txt = Text("", font_size=28, color=WHITE, font="Arial")
            txt.move_to(top_left + DOWN*0.7*i)  # вертикальный сдвиг по строкам
            self.add(txt)
            text_objects.append(txt)

        # --- курсор ---
        cursor = Rectangle(width=0.05, height=0.6)\
            .set_fill(WHITE, opacity=1)\
            .set_stroke(width=0)
        self.add(cursor)

        # --- печать текста по буквам ---
        for i, line in enumerate(lines):
            current_line_text = ""
            for char in line:
                current_line_text += char
                text_objects[i].become(
                    Text(current_line_text, font_size=28, color=WHITE, font="Arial")
                        .move_to(text_objects[i].get_center())
                )
                cursor.next_to(text_objects[i], RIGHT, buff=0.05)
                self.wait(1.0 / len(post_text))  # весь текст ~1 сек

        self.wait(0.3)

        # --- кнопка ---
        button = RoundedRectangle(width=4, height=1, corner_radius=0.2)\
            .set_fill(GRAY, opacity=1)\
            .set_stroke(WHITE, width=2)
        button_text = Text("Generate Header", font_size=32, color=BLACK)
        button_group = VGroup(button, button_text)
        button_group.next_to(input_box, DOWN, buff=1)
        self.play(FadeIn(button_group))
        self.wait(0.3)

        # --- курсор на кнопке для клика ---
        button_cursor = Rectangle(width=0.05, height=0.6)\
            .set_fill(WHITE, opacity=1)\
            .set_stroke(width=0)
        button_cursor.move_to(button.get_left() + RIGHT*0.3 + UP*0.05)
        self.add(button_cursor)
        self.play(button_cursor.animate.move_to(button.get_center()), run_time=0.3)
        self.play(button.animate.set_fill(DARK_GRAY, opacity=1), run_time=0.2)
        self.play(button.animate.set_fill(GRAY, opacity=1), run_time=0.2)
        self.wait(0.3)
        self.remove(button_cursor)

        # --- заголовок ---
        header_text = "Neural Networks: Learning Complex Patterns"
        header = Text(header_text, font_size=40, color=YELLOW, font="Arial")
        header.next_to(button_group, DOWN, buff=1)
        self.play(FadeIn(header, shift=UP*0.3))
        self.wait(2)