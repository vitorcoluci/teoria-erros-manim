#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim media-apresentação.py Fechamento -l

############################################
############################################


# Apatita (verde)   : código Hex "#43bfca"
# Papoula (laranja) : código Hex "#dc6a40"

apatita = "#43bfca"
papoula = "#dc6a40"
azul="#0000ff"

from manimlib.imports import *
####################
# GRID from theoremofbeethoven
class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

import random
import numpy as np
####################

############################################
# Cena de abertura
############################################
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color(apatita)

      tt1=TextMobject("Representação de")
      tt2=TextMobject("uma grandeza experimental")
      titulo = VGroup(tt1,tt2)
      titulo.arrange_submobjects(DOWN,buff=0.3)
      titulo.set_color(papoula).scale(2)
         
      self.play(FadeIn(explora))
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(2)

############################################
# Cena intermediárias
############################################
class metodo(GraphScene):
    def construct(self):
       #grid=ScreenGrid()
       #self.add(grid)
      
       # texto inicial
       tt0 = TextMobject("Suponha que você tenha ")
       tt1 = TextMobject("realizado $N$ medições,")
       tt2 = TextMobject("sob as mesmas condições,")
       tt3 = TextMobject("de uma grandeza física")
       tt = VGroup(tt0,tt1,tt2,tt3)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(3.5*RIGHT)

       self.play(FadeIn(tt))
       self.wait(2)
       # cria lista de medicoes na tela
       np.random.seed(1)
       q=[]
       for x in range(-6, 0):
            for y in range(4, -4,-1):
                m =  5.0 + 0.3* np.random.randn()
                a = TexMobject("{:.2f}".format(m), height=0.3, fill_opacity=.7).shift(x*RIGHT+y*UP)
                q.append(a)
                self.add(a)
                self.wait(.2)
                
       self.wait(2)
       r = VGroup(*[ q[i] for i in range(len(q)) ])
       self.play(FadeOut(r))
       #for i in range(len(q)):
       #   self.remove(q[i])
      
       self.wait(2)
       self.play(FadeOut(tt))

       # texto
       tt0 = TextMobject("No caso de haver apenas erros aleatórios,")
       tt1 = TextMobject("o valor da grandeza experimental")
       tt2 = TextMobject("$y$ é expresso como")
      
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(WHITE).scale(1.0).shift(2.5*UP)

       self.play(FadeIn(tt))
       self.wait(2)

       f1 = TexMobject(r"y=(\bar{y}\pm\sigma_m)\; u").scale(1.8)
       self.play(FadeIn(f1))

       arrow1 = Arrow(-0.5*RIGHT-0.2*UP,-0.5*RIGHT-1.4*UP)
       arrow1.set_color(YELLOW)
       g1=TextMobject("Média").set_color(YELLOW).shift(-0.5*RIGHT-1.5*UP)
       self.play(GrowArrow(arrow1),FadeIn(g1))
       self.wait(2)

       arrow2 = Arrow(RIGHT-0.2*UP,RIGHT-3*UP)
       arrow2.set_color(RED)
       g2=TextMobject("Desvio padrão da média").set_color(RED).shift(RIGHT-3.2*UP)
       self.play(GrowArrow(arrow2),FadeIn(g2))
       self.wait(2)

       arrow3 = Arrow(2.5*RIGHT-0.2*UP,2.5*RIGHT-2.1*UP)
       arrow3.set_color(GREEN)
       g3=TextMobject("Unidade").set_color(GREEN).shift(2.5*RIGHT-2.2*UP)
       self.play(GrowArrow(arrow3),FadeIn(g3))
       self.wait(2)

       self.play(FadeOut(arrow1),FadeOut(g1), \
                 FadeOut(arrow2),FadeOut(g2),FadeOut(arrow3),FadeOut(g3))


       ff1= TexMobject(r"\bar{y}=\frac{1}{N}\sum_{i=1}^N y_i").scale(1.5).shift(2*DOWN+4*LEFT).set_color(YELLOW)
       self.play(FadeIn(ff1))
       self.wait()

       ff3= TexMobject(r"\sigma^2=\frac{1}{N-1}\sum_{i=1}^N (y_i-\bar{y})^2").scale(1.2).shift(2*DOWN+3.5*RIGHT).set_color(RED)
       self.play(FadeIn(ff3))
       self.wait()

       ff2= TexMobject(r"\sigma_m=\frac{\sigma}{\sqrt{N}").scale(1.5).shift(2*DOWN+3*RIGHT).set_color(RED)
       self.play(FadeOut(ff3),FadeIn(ff2))
       self.wait()
    
       self.play(FadeOut(ff1),FadeOut(ff2),FadeOut(tt),FadeOut(f1))

       # texto
       tt0 = TextMobject("Considere, por exemplo, ")
       tt1 = TextMobject("11 medições do alcance (em m)")
       tt2 = TextMobject("de um projétil")
      
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(WHITE).scale(1.0).shift(-2.5*UP)

       self.play(FadeIn(tt))
       self.wait(2)

       q=[]
       v=[]
       j=1
       for x in range(-5, 6):
                m =  5.0 + 0.3* np.random.randn()
                v.append(m)
                a1 = TexMobject("{:.2f}".format(m),  height=0.3, fill_opacity=1).shift(x*RIGHT+2*UP)
                a2 = TexMobject(r"y_{","{}".format(j),r"}", height=0.3, fill_opacity=1).shift(x*RIGHT+2.5*UP)
                j=j+1
                a = VGroup(a1,a2)
                q.append(a)
                self.add(a)
                self.wait(.2)
                
       self.wait(2)
       self.play(FadeOut(tt))
              
       
       soma=np.sum(v)
       media=np.mean(v)
       std=np.std(v,ddof=1)

       stdm= std/np.sqrt(11)

       #print(media,std,stdm)
       
       ff1=  TexMobject(r"\bar{y}=",r"\frac{1}{N}",r"\sum_{i=1}^N y_i").scale(1.5).set_color(YELLOW)
       self.play(FadeIn(ff1))
       self.wait()
       fa=TexMobject(r"\frac{1}{11}").next_to(ff1[0], RIGHT, buff = 0.3).scale(1.5).set_color(YELLOW)
       
       
       x0=0
       for i in range(len(v)):
                x0=x0+(v[i]-media)*(v[i]-media)
                
       
       fb=TexMobject("({:.4f})".format(soma)).next_to(ff1[1], RIGHT, buff = 0.5).scale(1.5).set_color(YELLOW)
       self.play(Transform(ff1[1],fa))
       self.wait(2) 
       self.play(Transform(ff1[2],fb))
       self.wait(2)
       self.play(FadeOut(ff1),FadeOut(fa),FadeOut(fb))
       self.wait()

       ff1= TexMobject(r"\bar{y}=","{:.4f}".format(media)).scale(1.5).shift(0*LEFT).set_color(YELLOW)
       self.play(FadeIn(ff1))
       self.wait()
   
       ff3= TexMobject(r"\sigma^2=",r"\frac{1}{N-1}",r"\sum_{i=1}^N (y_i-",r"\bar{y})^2").scale(1.5).shift(2*DOWN).set_color(RED)
       self.play(FadeIn(ff3))
       fa=TexMobject(r"\frac{1}{10}").next_to(ff3[0], RIGHT, buff = 0.9).scale(1.5).set_color(RED)
       fb=TexMobject("{:.4f}".format(media),r")^2").next_to(ff3[2], RIGHT, buff = 0.9).scale(1.5).set_color(RED)
       self.play(Transform(ff3[1],fa))
       self.wait(2) 
       self.play(Transform(ff3[3],fb))
       self.wait(2)

       fc=TexMobject("{:.4f}".format(x0)).next_to(ff3[1], RIGHT, buff = 0.7).scale(1.5).set_color(RED)
       self.play(Transform(ff3[2],fc),Transform(ff3[3],fc),Transform(fb,fc),FadeOut(fb))
       self.wait(2)
       self.play(FadeOut(ff3),FadeOut(fa),FadeOut(fc))

       ff2= TexMobject(r"\sigma=","{:.4f}".format(std)).scale(1.5).shift(2*DOWN).set_color(RED)
       self.play(FadeIn(ff2))
       self.wait()
       self.play(ApplyMethod(ff2.scale,0.7))
       self.wait()
       self.play(ApplyMethod(ff2.move_to,4*LEFT+2*DOWN))
       self.wait()

       ff4=  TexMobject(r"\sigma_m=",r"\frac{\sigma}{\sqrt{N}}").scale(1.5).shift(2*DOWN).set_color(RED)
       ff4c= TexMobject(r"\sigma_m=",r"\frac{0.1858}{\sqrt{11}").scale(1.5).shift(2*DOWN).set_color(RED)
       ff4d= TexMobject(r"\sigma_m=",r"\hspace{0.8cm}0.05602652").scale(1.5).shift(2*DOWN).set_color(RED)

       self.play(FadeIn(ff4))
       self.wait()
       self.play(Transform(ff4[1],ff4c[1]))
       self.wait(2)
       self.play(Transform(ff4[1],ff4d[1]))
       self.wait(2)

       r = VGroup(*[ q[i] for i in range(len(q)) ])
       self.play(FadeOut(r),FadeOut(ff1),FadeOut(ff2),FadeOut(ff4[0]),FadeOut(ff4[1])) 
       self.wait(2)

       f1 = TexMobject(r"y=(\bar{y}\pm\sigma_m)\; u").scale(1.8).shift(2*UP)
       self.play(FadeIn(f1))
       self.wait()
       f2 = TexMobject(r"y=(","5.04","436791",r"\pm","0.0","5","602652",r")\; m").scale(1.8).shift(0*UP)
       f2c = TexMobject(r"y=(","5.04","436791",r"\pm","0.0","6","602652",r")\; m").scale(1.8).shift(0*UP)
       self.play(FadeIn(f2))
       self.wait()
       self.play(ApplyMethod(f2[6].set_color,RED))
       self.wait()
       
       l1 = Line(2.5*RIGHT,5.4*RIGHT)
       l1.set_color(YELLOW)
       self.play(GrowArrow(l1))


       self.wait()
       self.play(Transform(f2[5],f2c[5]))
       self.wait()


       self.play(ApplyMethod(f2[2].set_color,RED))
       self.wait()

       l2 = Line(-2.7*RIGHT,-0.2*RIGHT)
       l2.set_color(YELLOW)
       self.play(GrowArrow(l2))
       
       
       self.wait()
       self.play(FadeOut(f2),FadeOut(l1),FadeOut(l2))
       f3 = TexMobject(r"y=(5.04\pm0.06)\; m").scale(1.8)
       self.play(FadeIn(f3))

       self.wait(3)
       

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
       
