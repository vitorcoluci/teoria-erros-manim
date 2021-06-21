#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim gaussiana.py Fechamento -l

############################################
############################################

#
#Definição de Cores
#
# Apatita (verde)   : código Hex "#43bfca"
# Papoula (laranja) : código Hex "#dc6a40"

apatita = "#43bfca"
papoula = "#dc6a40"


from manimlib.imports import *
import random
import numpy as np
############################################
# Cena de abertura
############################################
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color(apatita)

      tt1=TextMobject("Distribuição")
      tt2=TextMobject("Gaussiana")
      titulo = VGroup(tt1,tt2)
      titulo.arrange_submobjects(DOWN,buff=0.3)
      titulo.set_color(papoula).scale(3)
      

      self.play(FadeIn(explora))
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(2)

############################################
# Cena intermediárias
############################################
class metodo(GraphScene):
     CONFIG = {
     "x_min": 0,
     "x_max": 10,
     "x_axis_width": 10,
     "x_tick_frequency": 1,
     "x_leftmost_tick": None, # Change if different from x_min
     "x_labeled_nums": None, #[0,1,2,3,4,5,6,7,8,9,10],
     "x_axis_label": "$x$",
     "y_min": 0.0,
     "y_max": 1.0,
     "y_axis_height": 6,
     "y_tick_frequency": 1,
     "y_bottom_tick": None, # Change if different from y_min
     "y_labeled_nums": None,
     "y_label_decimals": 1,
     "y_axis_label": "$G(x)$",
     "axes_color": WHITE,
     "graph_origin": 3 * DOWN + 6 * LEFT,
     "exclude_zero_label": False,
     "num_graph_anchor_points": 25,
     "default_graph_colors": [BLUE, GREEN, YELLOW],
     "default_derivative_color": GREEN,
     "default_input_color": YELLOW,
     "default_riemann_start_color": papoula,
     "default_riemann_end_color": papoula,
     "area_opacity": 0.8,
     "num_rects": 120,
     } 
     def f1(self,x):
         return (2*1/(1.0*np.sqrt(2.0*np.pi)))*np.exp(-np.square(x-5.0)/(2.0*np.square(1.0)))

     def construct(self):
              
       #informação introdutória
       tt0 = TextMobject("A maioria dos erros e medições de").set_color(YELLOW).scale(1.5)
       tt1 = TextMobject("grandezas físicas obedecem a").set_color(YELLOW).scale(1.5)
       tt2 = TextMobject("distribuição gaussiana").set_color(YELLOW).scale(1.5) 
       tt0.shift(UP)
       tt2.shift(DOWN)

       self.play(FadeIn(tt0),FadeIn(tt1),FadeIn(tt2))
       self.wait(2)
       self.play(FadeOut(tt0),FadeOut(tt1),FadeOut(tt2))
       self.wait()

       self.setup_axes(animate=False)
       #faz grafico da gaussiana
       func1 = self.get_graph(self.f1,color=YELLOW)
       self.play(FadeIn(func1))
       self.wait(2)

       g1 = TextMobject("Gaussiana")
       g1.set_color(YELLOW)
       g1.scale(1.5)
       g1.shift(4.5*RIGHT)
       
       arrow1 = Arrow(0*RIGHT,3*RIGHT)
       arrow1.set_color(YELLOW)
       self.play(GrowArrow(arrow1),FadeIn(g1))
       self.wait(2)
       self.play(FadeOut(arrow1),FadeOut(g1))

       # formula de G(x)
       g = TexMobject(r"\displaystyle G(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{\displaystyle -\frac{(x-\mu)^2}{2\sigma^2}").set_color(WHITE).scale(1.2).shift(2.5*UP+3.5*RIGHT) 
       self.play(FadeIn(g))
       self.wait(2)
       self.play(ApplyMethod(g.scale,0.7))
       self.wait()

       # simetria
       props3  = TextMobject("$G(x)$ é simétrica").set_color(YELLOW).scale(1.2).shift(3.5*RIGHT) 
       self.play(FadeIn(props3))
       self.wait(1)
       self.play(FadeOut(props3))
       self.wait()

       # integral de G(x)
       props3  = TexMobject(r"\displaystyle \int_{-\infty}^{\infty} G(x) dx = 1").set_color(YELLOW).scale(1.2).shift(3.5*RIGHT) 
       self.play(FadeIn(props3))
       self.wait(1)
       self.play(FadeOut(props3))
       self.wait()

       # media
       media  = TextMobject("$\mu =$ média").set_color(WHITE).scale(1.5).shift(3.5*RIGHT) 
       mu0  = TexMobject(r"\mu").set_color(WHITE).scale(1.2).shift(LEFT+3.5*DOWN)
       arrow2 = Arrow(LEFT,3*DOWN+LEFT)
       arrow2.set_color(WHITE)


       self.play(FadeIn(media),GrowArrow(arrow2),FadeIn(mu0))
       self.wait()
       self.play(FadeOut(media),FadeOut(arrow2))
      
       # máximo de G(x)
       g1 = TextMobject("Para $x=\mu$,")
       g2 = TextMobject("$G(x)$ é máxima.")
       g3 = TexMobject(r"G_{max}= \frac{1}{ \sigma\sqrt{2\pi} }")
       vg = VGroup(g1,g2,g3)
       vg.arrange_submobjects(DOWN,buff=0.3)
       vg.set_color(YELLOW).scale(1.2).shift(0.5*DOWN+3.5*RIGHT)
       arrow2 = Arrow(3.5*UP+LEFT,1.7*UP+LEFT)
       arrow2.set_color(WHITE)
       self.play(FadeIn(vg),GrowArrow(arrow2))
       self.wait(3)
       self.play(FadeOut(vg),FadeOut(arrow2))
       self.wait()

       # sigma
       sigma   = TextMobject("$\sigma =$ desvio padrão").set_color(WHITE).scale(1.5).shift(3.5*RIGHT)
       props4  = TexMobject(r"\displaystyle \int_{\mu-\sigma}^{\mu+\sigma} G(x) dx = 0.6827").set_color(YELLOW).scale(1).shift(3.5*RIGHT)
       sigma_dir  = TexMobject(r"\mu +\sigma").set_color(WHITE).scale(0.8).shift(RIGHT+LEFT+3.5*DOWN)
       sigma_esq  = TexMobject(r"\mu -\sigma").set_color(WHITE).scale(0.8).shift(2*LEFT+3.5*DOWN)

       
       line1 = self.get_vertical_line_to_graph(6,func1,DashedLine,color=YELLOW)
       line2 = self.get_vertical_line_to_graph(4,func1,DashedLine,color=YELLOW)

       self.play(FadeIn(sigma))
       self.wait()
       self.play(FadeOut(sigma), FadeIn(sigma_dir),FadeIn(sigma_esq))
       self.wait()
       self.play(ShowCreation(line1),ShowCreation(line2))
       self.wait()

       area = self.get_area(func1, 4, 6)
       self.play(ShowCreation(area))
       self.wait()
       self.play(FadeIn(props4))
       self.wait(2)
       self.play(FadeOut(props4),FadeOut(area))
       self.play(FadeOut(sigma_dir),FadeOut(sigma_esq),FadeOut(line1),FadeOut(line2))
       self.wait()

       # 2 sigma
       props4  = TexMobject(r"\displaystyle \int_{\mu-2\sigma}^{\mu+2\sigma} G(x) dx = 0.9545").set_color(YELLOW).scale(1).shift(3.5*RIGHT)
       sigma_dir  = TexMobject(r"\mu +2\sigma").set_color(WHITE).scale(0.8).shift(2*RIGHT+LEFT+3.5*DOWN)
       sigma_esq  = TexMobject(r"\mu -2\sigma").set_color(WHITE).scale(0.8).shift(3*LEFT+3.5*DOWN)

       line1 = self.get_vertical_line_to_graph(7,func1,DashedLine,color=YELLOW)
       line2 = self.get_vertical_line_to_graph(3,func1,DashedLine,color=YELLOW)

       self.play(FadeIn(sigma_dir),FadeIn(sigma_esq))
       self.wait()
       self.play(ShowCreation(line1),ShowCreation(line2))
       self.wait()

       area = self.get_area(func1, 3, 7)
       self.play(ShowCreation(area))
       self.wait()
       self.play(FadeIn(props4))
       self.wait(2)
       self.play(FadeOut(props4),FadeOut(area))
       self.play(FadeOut(sigma_dir),FadeOut(sigma_esq),FadeOut(line1),FadeOut(line2))
       self.wait()

       # 3 sigma
       props4  = TexMobject(r"\displaystyle \int_{\mu-3\sigma}^{\mu+3\sigma} G(x) dx = 0.9973").set_color(YELLOW).scale(1).shift(3.5*RIGHT)
       sigma_dir  = TexMobject(r"\mu +3\sigma").set_color(WHITE).scale(0.8).shift(3*RIGHT+LEFT+3.5*DOWN)
       sigma_esq  = TexMobject(r"\mu -3\sigma").set_color(WHITE).scale(0.8).shift(4*LEFT+3.5*DOWN)

       line1 = self.get_vertical_line_to_graph(8,func1,DashedLine,color=YELLOW)
       line2 = self.get_vertical_line_to_graph(2,func1,DashedLine,color=YELLOW)

       self.play(FadeIn(sigma_dir),FadeIn(sigma_esq))
       self.wait()
       self.play(ShowCreation(line1),ShowCreation(line2))
       self.wait()

       area = self.get_area(func1, 2, 8)
       self.play(ShowCreation(area))
       self.wait()
       self.play(FadeIn(props4))
       self.wait(2)
       self.play(FadeOut(props4),FadeOut(area))
       self.play(FadeOut(sigma_dir),FadeOut(sigma_esq),FadeOut(line1),FadeOut(line2))
       self.wait()
     

       
############################################
# Cena de fechamento
############################################
class Fechamento(Scene):
    def construct(self):
      explora=TexMobject(
           "\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")
      explora.shift(2.5*UP)

      site=TextMobject("https://wordpress.ft.unicamp.br/explora/")
      site.scale(1.0)
      site.set_color(WHITE)
      site.shift(0.8*UP)

      autor=TextMobject("Animações: Vitor R. Coluci")
      autor.scale(1.2)
      autor.set_color("#dc6a40")
      autor.shift(0.3*DOWN)

      ft = ImageMobject("logo-FT.jpg")
      ft.scale(1.5)
      ft.shift(2.3*DOWN+3*RIGHT)

      unicamp = ImageMobject("logo-unicamp.jpg")
      unicamp.scale(1.5)
      unicamp.shift(2.3*DOWN+3*LEFT)
      
      self.play(FadeIn(explora),FadeIn(site))
      self.wait(1)
      self.play(FadeIn(unicamp),FadeIn(ft))
      self.wait(1)
      self.play(FadeOut(unicamp),FadeOut(ft))
      self.wait(0.8)
      self.play(FadeIn(autor))
      self.wait(2)

############################################
############################################
