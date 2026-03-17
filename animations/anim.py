from manim import *

# ===== НАСТРОЙКИ =====

# позиция текстового блока
BOX_SHIFT = UP * 1.5

# размер рамки
BOX_WIDTH = 10
BOX_HEIGHT = 4

# отступ текста внутри рамки
TEXT_LEFT_PADDING = 0.5
TEXT_TOP_PADDING = 0.4

class HeaderGeneratorDemo(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- рамка (фиксированная) ---
        box = RoundedRectangle(
            width=BOX_WIDTH,
            height=BOX_HEIGHT,
            corner_radius=0.2
        ).set_stroke(WHITE, width=2)

        box.move_to(BOX_SHIFT)
        self.add(box)

        # --- стартовая позиция текста (внутри рамки) ---
        text_start = (
            box.get_top()
            + DOWN * TEXT_TOP_PADDING
            + RIGHT * (-BOX_WIDTH/2 + TEXT_LEFT_PADDING)
        )

        # --- текст поста ---
        post_text = """neural networks are changing the way we
build software. they can learn patterns from
data instead of explicit rules. this opens new
possibilities in automation and creativity."""

        text_obj = Text(
            "",
            font_size=34,
            color=WHITE,
            font="Arial",
            line_spacing=0.8
        )

        text_obj.move_to(text_start, aligned_edge=UL)
        self.add(text_obj)

        # --- печать текста ---
        typed = ""
        for letter in post_text:
            typed += letter

            new_text = Text(
                typed,
                font_size=34,
                color=WHITE,
                font="Arial",
                line_spacing=0.8
            )

            new_text.move_to(text_start, aligned_edge=UL)

            self.remove(text_obj)
            text_obj = new_text
            self.add(text_obj)

            self.wait(0.02)

        self.wait(0.5)

        # --- кнопка ---
        button = RoundedRectangle(
            width=4,
            height=1,
            corner_radius=0.3
        ).set_fill(BLUE, opacity=1).set_stroke(width=0)

        button_text = Text(
            "Generate Header",
            font_size=30,
            color=WHITE,
            font="Arial"
        ).move_to(button.get_center())

        button_group = VGroup(button, button_text)
        button_group.next_to(box, DOWN, buff=1.2)

        self.play(FadeIn(button_group, shift=UP*0.2))

        # --- клик ---
        self.play(button.animate.scale(0.93), run_time=0.1)
        self.play(button.animate.scale(1/0.93), run_time=0.1)

        self.wait(0.3)

        # --- loading ---
        loading = Text("...", font_size=40, color=GRAY, font="Arial")
        loading.next_to(button_group, DOWN, buff=0.6)

        self.play(FadeIn(loading))
        self.wait(0.6)
        self.play(FadeOut(loading))

        # --- результат ---
        header = Text(
            "How Neural Networks Are Transforming Software",
            font_size=40,
            color=BLUE,
            font="Arial"
        ).next_to(button_group, DOWN, buff=0.8)

        self.play(FadeIn(header, shift=UP*0.3), run_time=0.8)

        self.wait(2)