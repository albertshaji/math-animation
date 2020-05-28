from manimlib.imports import *
import numpy as np
from sympy import *

class Title(Scene):
    def construct(self):
        title = TextMobject("Taylor Series of Bessel Function")
        title.scale(1.5)
        symbol = TexMobject("\\{ J_0 \\}")
        symbol.scale(2)
        symbol.set_color(BLUE)

        self.wait()
        self.play(Write(title, run_time=1.5))
        self.play(
            ApplyMethod(title.shift, 1.5*UP),
            FadeIn(symbol)
            )
        self.wait()
        self.remove(title, symbol)
        self.add(TextMobject("What is Bessel Function !"))
        self.wait()

class Define(Scene):
    def construct(self):
        define = TextMobject("Bessel function is a solution of the differential equation:")
        define.shift(2.5*UP)
        define.set_color(BLUE)

        eq = TexMobject("x", "^2 \\cdot \\frac{d^2}{d", "x" , "^2} +", "x", "\\cdot \\frac{d}{d", "x", "} + ", "x", "^2", "\\cdot", "y"," = 0")
        eq.set_color_by_tex("x", ORANGE)
        eq.set_color_by_tex("y", GREEN)
        eq.next_to(define, 2*DOWN)
        eq.scale(1.3)

        side_text = TextMobject("Derived  by the German astronomer \\\ ", "Friedrich Wilhelm Bessel", "around 1817 \\\ during an investigation of solutions \\\ of one of  Kepler’s equations of \\\ planetary motion.")
        side_text.set_color_by_tex("Friedrich Wilhelm Bessel", YELLOW)
        side_text.shift(1.5*DOWN+1.5*RIGHT)
        side_text.scale(.8)

        img = ImageMobject("bessel-portrait.png")
        img.scale(1.5)
        img.shift(1.5*DOWN+3.5*LEFT)

        self.play(Write(define, run_time=2))
        self.play(Write(eq, run_time=3))
        self.wait()
        self.play(FadeIn(img), Write(side_text, run_time=5))
        self.wait()

class Equation(Scene):
    def construct(self):
        eq = TexMobject("J_0 = \\sum_{k=0}^{\infty} (-1)^k \\frac{x^{2k}}{2^{2k}(k!)^2}")
        eq.set_color(BLUE)
        eq.scale(2)

        var = TexMobject("J_0 = ")
        var.shift(2.7*DOWN+6*LEFT)
        var.set_color(GREEN)

        self.play(Write(eq, run_time=4))
        self.wait()
        self.play(Transform(eq, var))

class Plotting(GraphScene):
    CONFIG = {
        "x_min": -15,
        "x_max": 15,
        "x_axis_width": 12,
        "x_tick_frequency": 3,
        "x_axis_label": "$x$",
        "x_labeled_nums": range(-15, 15, 3),

        "y_min": 0,
        "y_max": 1.2,
        "y_axis_height": 3,
        "y_tick_frequency": 0.2,
        "y_axis_label": "$J_0$",
        "y_labeled_nums": range(0, 1),

        "graph_origin": ORIGIN,
         "axes_color" : BLUE,
        }

    def construct(self):
        var = TexMobject("J_0 = ")
        var.shift(2.7*DOWN+6*LEFT)
        var.set_color(GREEN)
        self.add(var)

        self.setup_axes(animate = True)
        self.wait()
        parts = [
            "1",
            "- \\frac{x^2}{2^2}",
            "+ \\frac{x^4}{2^4\\: 2!^2}",
            "- \\frac{x^6}{2^6\\: 3!^2}",
            "+ \\frac{x^8}{2^8\\: 4!^2}",
            "- \\frac{x^{10}}{2^{10}\\: 5!^2}",
            "+ \\frac{x^{12}}{2^{12}\\: 6!^2}",
            "+ ..."
            ]

        dog = TexMobject(parts[0])
        dog.next_to(var, RIGHT)
        dog.set_color(BLUE)
        self.add(dog)

        x = symbols('x')
        g = 1
        for i in range (1,20):

            f = g + (((-1)**i)*x**(2*i))/((2**(2*i))*(math.factorial(i)**2))
            self.one = lambdify(x, g)
            self.two = lambdify(x, f)

            p = self.get_graph(self.one)
            q = self.get_graph(self.two)
            if(i%2 == 0):
                q.set_color(BLUE)
                p.set_color(YELLOW)
            else:
                q.set_color(YELLOW)
                p.set_color(BLUE)
            g = f

            if(i < 8):
                cat = TexMobject(parts[i])
                cat.next_to(dog, RIGHT)
                dog = cat

            if(i%2 == 0):
                cat.set_color(BLUE)
            else:
                cat.set_color(YELLOW)

            if(i < 8):
                self.play(Transform(p, q , run_time=2), Write(cat , run_time=1.5) )
                self.wait(.5)
            else:
                self.play(Transform(p, q , run_time=1), Write(cat , run_time=.5) )
                self.wait(0.2)

            self.remove(p)

        self.add(p)
        self.wait(2)


class Ripple(Scene):
    def construct(self):
        que = TextMobject("Looks like a ripple in water ?")
        que.scale(1.5)
        que.set_color(BLUE_A)

        know = TextMobject("Now you know Why,")
        know.shift(UP)

        use = TextMobject("Bessel function is used to model physical phenomena, \\\ like the flow of heat or electricity in a solid cylinder, \\\ propagation of electromagnetic waves \\\ and diffraction of light.")
        use.set_color(BLUE_B)
        use.next_to(know, 4*DOWN)

        self.play(ShowCreation(que))
        self.wait()
        self.play(ApplyMethod(que.shift, 2.5*UP, run_time=.5), FadeIn(know))
        self.play(Write(use, run_time=5))
        self.wait()
        self.play(FadeOut(use), FadeOut(know), FadeOut(que))
