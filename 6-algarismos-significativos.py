#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim algarismos-significativos.py Fechamento -l

############################################
############################################


# Apatita (verde)   : código Hex "#43bfca"
# Papoula (laranja) : código Hex "#dc6a40"

apatita = "#43bfca"
papoula = "#dc6a40"
azul="#0000ff"

from manimlib.imports import *
####################
# GRID auxiliar para posicionar os objetos na tela
# É removido para gerar o vídeo final da animação
# crédito: theoremofbeethoven
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

      tt1=TextMobject("Algarismos")
      tt2=TextMobject("significativos")
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
     "x_max": 1000,
     "x_axis_width": 7,
     "x_tick_frequency": 200,
     "x_leftmost_tick": None, # Change if different from x_min
     "x_labeled_nums": [0,200,400,600,800,1000],#[0,1,2,3,4,5,6,7,8,9,10],
     "x_axis_label": "$N$",
     "y_min": 0.0,
     "y_max": 1.0,
     "y_axis_height": 5,
     "y_tick_frequency": 1,
     "y_bottom_tick": None, # Change if different from y_min
     "y_label_decimals": 1,
     "y_labeled_nums": [0,0.2,0.4,0.6,0.8,1.0],
     "y_axis_label": "$\sigma_{\sigma^2}/\sigma$",
     "axes_color": WHITE,
     "graph_origin": 3 * DOWN + 5 * LEFT,
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



    def ff(self,x):
         return np.sqrt(np.sqrt(2.0/(x-1)))

    def construct(self):
       #grid=ScreenGrid()
       #self.add(grid)

       
       # texto inicial
       tt0 = TextMobject("O valor de uma grandeza experimental")
       tt1 = TextMobject("pode ter muitos algarismos")
       
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2.5*UP)

       self.play(FadeIn(tt))
       self.wait(2)

       a1 = TexMobject(r"0.0000","314159265359").scale(1.8)
       self.play(Write(a1))
       self.wait(2)
       self.play(FadeOut(tt))
       self.wait(2)

       
       stt0 = TextMobject("Como existe uma incerteza associada")
       stt1 = TextMobject("ao valor da grandeza experimental,")
       
       stt = VGroup(stt0,stt1)
       stt.arrange_submobjects(DOWN,buff=0.3)
       stt.set_color(YELLOW).scale(1.0).shift(2.5*UP)

       self.play(FadeIn(stt))
       self.wait(2)

       qtt0 = TextMobject("nem todos os algarismos")
       qtt1 = TextMobject("tem significado")
       
       qtt = VGroup(qtt0,qtt1)
       qtt.arrange_submobjects(DOWN,buff=0.3)
       qtt.set_color(YELLOW).scale(1.0).shift(2.5*DOWN)

       self.play(FadeIn(qtt))
       self.wait(2)
       self.play(FadeOut(qtt),FadeOut(stt))
       self.wait(2)


       arrow1 = Arrow(1.2*LEFT-0.2*UP,1.2*LEFT+2*DOWN)
       arrow1.set_color(YELLOW)

       t1=TextMobject("Primeiro algarismo")
       t2=TextMobject("não-nulo")
       t = VGroup(t1,t2)
       t.arrange_submobjects(DOWN,buff=0.3)
       t.set_color(BLUE_A).scale(1.0).shift(1.2*LEFT+2.5*DOWN)
       self.play(GrowArrow(arrow1),FadeIn(t))
   
       self.wait(2)
       
       self.play(ApplyMethod(a1[0].set_color,RED_E))
       self.wait()

       s1=TextMobject("Zeros à esquerda")
       s2=TextMobject("do primeiro não-nulo")
       s3=TextMobject("não são significativos")
       s = VGroup(s1,s2,s3)
       s.arrange_submobjects(DOWN,buff=0.3)
       s.set_color(RED_E).scale(1.0).shift(3*LEFT+1.5*UP)
       self.play(FadeIn(s))

       self.wait(2)
       self.play(FadeOut(t),FadeOut(arrow1))
       self.wait()
       tt0 = TextMobject("Podem ser removidos")
       tt1 = TextMobject("mudando a notação")
       
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2*DOWN)
       self.play(FadeIn(tt))
       self.wait(2)
       self.play(FadeOut(tt))
       
       self.wait()
       a2 = TexMobject(r"3.14159265359\times 10^{-5}").scale(1.8).shift(2*DOWN).set_color(GREEN_E)
       self.play(Write(a2))
       self.wait(2)
       self.play(FadeOut(a2),FadeOut(s),FadeOut(a1))
       self.wait()

       a1 = TexMobject("3.","1","4","1","5","9","2","6","5","5","9").scale(1.8)
       self.play(Write(a1))
       self.wait(2)

       # texto inicial
       tt0 = TextMobject("Alguns são significativos,")
       tt1 = TextMobject("outros não.")
       
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.scale(1.3).shift(2.5*UP)


       self.play(FadeIn(tt))

       t1=TextMobject("Significativos").set_color(GREEN_SCREEN).scale(1.0).shift(2*LEFT+2*DOWN)
       t2=TextMobject("Não-significativos").set_color("#eb344c").scale(1.0).shift(2*RIGHT+2*DOWN)
       self.play(FadeIn(t1),FadeIn(t2),\
                 ApplyMethod(a1[:5].set_color,GREEN_SCREEN),\
                 ApplyMethod(a1[5:].set_color,"#eb344c"))
   
       self.wait(2)
       self.play(FadeOut(tt),FadeOut(t1),FadeOut(t2),\
                 ApplyMethod(a1[:5].set_color,WHITE),\
                 ApplyMethod(a1[5:].set_color,WHITE))
       self.wait()
  
       tt0 = TextMobject("Mas como determinar")
       tt1 = TextMobject("quais são os significativos ?")
       
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.scale(1.3).shift(2.5*UP)


       self.play(FadeIn(tt))

       for i in range(len(a1)):
                self.play(ApplyMethod(a1[i].scale,2),run_time=0.1)
                self.wait(0.1)
                self.play(ApplyMethod(a1[i].scale,0.5),run_time=0.5)
                

       self.wait()
       s1=TextMobject("É a incerteza padrão")
       s2=TextMobject("que determina o último")
       s3=TextMobject("algarismo significativo à direita")
       s = VGroup(s1,s2,s3)
       s.arrange_submobjects(DOWN,buff=0.3)
       s.set_color(GREEN_SCREEN).scale(1.0).shift(2*DOWN)
       self.play(FadeIn(s))
       self.wait(3)
       self.play(FadeOut(s),FadeOut(tt),FadeOut(a1))
       self.wait(2)

       ##################
       
       tt0 = TextMobject("Considere, por exemplo:")
       tt0.set_color(YELLOW).scale(1.0).shift(2.5*UP)

       self.play(FadeIn(tt0))
       self.wait()

       a1 = TexMobject(r"\bar{y}=3.141592").scale(1.4).shift(UP+3*LEFT)
       a2 = TexMobject(r"\sigma=0.031473").scale(1.4).shift(UP+3*RIGHT)
       self.play(Write(a1),Write(a2))
       self.wait(2)
   
       # calculo das probabilidades

       q1=[0.141592,1.141592,2.141592,3.141592,4.141592,5.141592,6.141592,7.141592,8.141592,9.141592]
       pq1=[]
       for i in range(len(q1)):
           x=q1[i]
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           #print(q1[i],y)
           pq1.append(y)


       q2=[3.041592,3.141592,3.241592,3.341592,3.441592,3.541592,3.641592,3.741592,3.841592,3.941592]
       pq2=[]
       for i in range(len(q2)):
           x=q2[i]
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           #print(q2[i],y)
           pq2.append(y)

       q3=[3.101592,3.111592,3.121592,3.131592,3.141592,3.151592,3.161592,3.171592,3.181592,3.191592]
       pq3=[]

       for i in range(len(q3)):
           x=q3[i]
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           #print(q3[i],y)
           pq3.append(y)

       q4=[3.140592,3.141592,3.142592,3.143592,3.144592,3.145592,3.146592,3.147592,3.148592,3.149592]
       pq4=[]

       for i in range(len(q4)):
           x=q4[i]
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           #print(q4[i],y)
           pq4.append(y)

       q5=[3.141092,3.141192,3.141292,3.141392,3.141492,3.141592,3.141692,3.141792,3.141892,3.141992]
       pq5=[]

       for i in range(len(q5)):
           x=q5[i]
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           #print(q5[i],y)
           pq5.append(y)


       q6=[3.141502,3.141512,3.141522,3.141532,3.141542,3.141552,3.141562,3.141572,3.141582,3.141592]
       pq6=[]

       for i in range(len(q6)):
           x=q6[i]
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           #print(q6[i],y)
           pq6.append(y)


       num1 = [3.04,3.06,3.08,3.10,3.12,3.14,3.16,3.18,3.20,3.22,3.24]
       tamanho=[]
       num1_text = []
       for i in range(len(num1)):
           x=num1[i]
           num1_text.append(TexMobject("{:.2f}".format(x)).set_color(GREEN_SCREEN).scale(0.7).shift((i-5)*1.3*RIGHT +0.5*DOWN))
           y=np.exp(-np.square(3.141592-x)/(2.0*np.square(0.031473)))
           tamanho.append(2.1*y)
           #print(num1[i],y)

       self.play(FadeOut(tt0))
  
       tt0 = TextMobject("Há aproximadamente 99\% de chance")
       tt1 = TexMobject(r"\text{do valor verdadeiro }(y_v)\text{ estar entre } \bar{y}-3\sigma\text{ e }\bar{y}+3\sigma")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2.5*UP)

       self.play(FadeIn(tt))
       self.wait(2)

     # mostra numero possiveis dentro de \pm 3 sigma
       for i in range(len(num1_text)):
           self.add(num1_text[i])
           self.wait(0.5)

       stt0 = TextMobject("E a probablidade de ser um dos valores acima")
       stt1 = TextMobject("segue uma distribuição gaussiana")
       stt = VGroup(stt0,stt1)
       stt.arrange_submobjects(DOWN,buff=0.3)
       stt.set_color(YELLOW).scale(1.0).move_to(3*DOWN)

       self.play(FadeIn(stt))
       self.wait(2)

       # muda tamanho de acordo com probabilidade
       for i in range(len(num1_text)):
           self.play( ApplyMethod(num1_text[i].scale,tamanho[i]))
           

       self.wait(2)
       for i in range(len(num1_text)):
           self.remove(num1_text[i])

       
       self.play(FadeOut(a1),FadeOut(a2),FadeOut(stt),FadeOut(tt))
       # Explicacao usando o tamanho do numero

       a1 = TexMobject("3",".","1","4","1","5","9").scale(1.2).move_to(0.4*DOWN+3.5*LEFT)
       alg = [0,1,2,3,4,5,6,7,8,9]
       alg_text = []
    
       stt0 = TextMobject("Para cada um dos algarismos possíveis")
       stt1 = TextMobject("de um dígito do número,")
       stt2 = TextMobject("existe uma probabilidade proporcional à")
       
       pp = TexMobject(r"\displaystyle e^{-\frac{(y-y_v)^2}{2\sigma^2}}")
       
       stt = VGroup(stt0,stt1,stt2,pp)
       stt.arrange_submobjects(DOWN,buff=0.25)
       stt.set_color(YELLOW).scale(1.0).move_to(2.5*UP+2*RIGHT)

       self.play(FadeIn(stt))
       self.wait(2)

       self.play(Write(a1))
       self.wait(1)

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[3].get_center()+(i-4)*0.6*UP))


  
       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.add(alg_text[i])
           
       self.wait()


       tt0 = TextMobject("Se a probabilidade ")
       tt1 = TextMobject("para um algarismo")
       tt2 = TextMobject("for maior que a dos outros")
               
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.25)
       tt.set_color(WHITE).scale(1.0).move_to(0.5*DOWN+3*RIGHT)

       self.play(FadeIn(tt),run_time=2)
       
       # muda o tamanho de acordo com probabilidade
       prob=[0.1,0.2,0.4,0.7,1.0,0.7,0.4,0.2,0.1,0.05]
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,1.6*prob[i]),run_time=0.2)
           
       self.wait()
         
       tts = TextMobject("Ele é significativo").set_color(YELLOW).scale(1.0).shift(3*DOWN+3.5*RIGHT)
       
       self.play(FadeIn(tts))
            
       self.wait()

       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
       
       self.play( ApplyMethod(a1[3].set_color,GREEN_SCREEN) )     

       self.play(FadeOut(tts),FadeOut(tt)) 
       
       ###############
       alg_text=[]
       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[5].get_center()+(i-5)*0.6*UP))


  
       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.add(alg_text[i])
           
       self.wait()



       tt0 = TextMobject("Se a probabilidade ")
       tt1 = TextMobject("para um algarismo")
       tt2 = TextMobject("for aproximadamente ")
       tt3 = TextMobject("igual a dos outros")        
       tt = VGroup(tt0,tt1,tt2,tt3)
       tt.arrange_submobjects(DOWN,buff=0.25)
       tt.set_color(WHITE).scale(1.0).move_to(0.5*DOWN+3*RIGHT)

       self.play(FadeIn(tt),run_time=2)

       
       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,1.6),run_time=0.2)
           
       self.wait()
         
       tts = TextMobject("Ele NÃO é significativo").set_color(YELLOW).scale(1.0).shift(3*DOWN+3.5*RIGHT)
       
       self.play(FadeIn(tts))
       self.wait()

       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])

       self.play( ApplyMethod(a1[5].set_color,"#eb347d") )   

       self.play(FadeOut(a1),FadeOut(tts),FadeOut(tt),FadeOut(stt))       
       self.wait()
 
      
##############################################

       # agora mostrando as prob como tamanhos ao longo do numero
       a1 = TexMobject("3",".","1","4","1","5","9").scale(1.2)
       alg = [0,1,2,3,4,5,6,7,8,9]
       alg_text = []
    
       self.play(Write(a1))
       self.wait(2)
       
       #############
       # 1o algarismo
       #############
       # acerta posicao do numero para caber todos os algarismos na vertical
       self.play( ApplyMethod(a1.move_to,DOWN))

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[0].get_center()+(i-3)*0.6*UP))


  
       tt0 = TextMobject("Possíveis algarismos").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(FadeIn(tt0))
       self.wait()

       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.play(FadeIn(alg_text[i]),run_time=0.2)
           
       self.wait()

       # muda a cor do numero
       self.play( ApplyMethod(a1.set_color,DARKER_GREY))

       tt1 = TextMobject("Probabilidade").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt1))
       self.wait()

       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,3*pq1[i]),run_time=0.2)
           
       self.wait()
         
       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
        
       tt2 = TextMobject("Algarismo significativo").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt2))
       self.wait()

       # highlight alg. significativo com cor Verde
       self.play( ApplyMethod(a1.set_color,WHITE))
       self.play( ApplyMethod(a1[0].set_color,GREEN_SCREEN) )     
       self.wait()
       self.play(FadeOut(tt0))
      
       #############

       #############
       # 2o algarismo
       #############
       alg_text = []
    
       # acerta posicao do numero para caber todos os algarismos na vertical
       self.play( ApplyMethod(a1.move_to,2*DOWN))

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[2].get_center()+(i-1)*0.6*UP))


  
       tt0 = TextMobject("Possíveis algarismos").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(FadeIn(tt0))
       self.wait()

       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.play(FadeIn(alg_text[i]),run_time=0.2)
           
       self.wait()

       # muda a cor do numero
       self.play( ApplyMethod(a1.set_color,DARKER_GREY))

       tt1 = TextMobject("Probabilidade").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt1))
       self.wait()

       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,3*pq2[i]),run_time=0.2)
           
       self.wait()
         
       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
        
       tt2 = TextMobject("Algarismo significativo").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt2))
       self.wait()

       # highlight alg. significativo com cor Verde
       self.play( ApplyMethod(a1.set_color,WHITE))
       self.play( ApplyMethod(a1[:3].set_color,GREEN_SCREEN) )     
       self.wait()
       self.play(FadeOut(tt0))
      
       #############

       #############
       # 3o algarismo
       #############
       alg_text = []
    
       # acerta posicao do numero para caber todos os algarismos na vertical
       self.play( ApplyMethod(a1.move_to,DOWN))

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[3].get_center()+(i-4)*0.6*UP))


  
       tt0 = TextMobject("Possíveis algarismos").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(FadeIn(tt0))
       self.wait()

       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.play(FadeIn(alg_text[i]),run_time=0.2)
           
       self.wait()

       # muda a cor do numero
       self.play( ApplyMethod(a1.set_color,DARKER_GREY))

       tt1 = TextMobject("Probabilidade").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt1))
       self.wait()

       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,3*pq3[i]),run_time=0.2)
           
       self.wait()
         
       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
        
       tt2 = TextMobject("Algarismo significativo").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt2))
       self.wait()

       # highlight alg. significativo com cor Verde
       self.play( ApplyMethod(a1.set_color,WHITE))
       self.play( ApplyMethod(a1[:4].set_color,GREEN_SCREEN) )     
       self.wait()
       self.play(FadeOut(tt0))
      
       #############

       #############
       # 4o algarismo
       #############
       alg_text = []
    
       # acerta posicao do numero para caber todos os algarismos na vertical
       self.play( ApplyMethod(a1.move_to,1.5*DOWN))

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[4].get_center()+(i-1)*0.6*UP))


  
       tt0 = TextMobject("Possíveis algarismos").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(FadeIn(tt0))
       self.wait()

       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.play(FadeIn(alg_text[i]),run_time=0.2)
           
       self.wait()

       # muda a cor do numero
       self.play( ApplyMethod(a1.set_color,DARKER_GREY))

       tt1 = TextMobject("Probabilidade").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt1))
       self.wait()

       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,1.5*pq4[i]),run_time=0.2)
           
       self.wait()
         
       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
        
       tt2 = TextMobject("Algarismo NÃO significativo").set_color(YELLOW).scale(1.0).shift(2*UP+3.8*RIGHT)
       self.play(Transform(tt0,tt2))
       self.wait()

       # highlight alg. significativo com cor Verde
       self.play( ApplyMethod(a1.set_color,WHITE))
       self.play( ApplyMethod(a1[:5].set_color,GREEN_SCREEN), ApplyMethod(a1[4].set_color,"#eb347d") )     
       self.wait()
       self.play(FadeOut(tt0))
      
       #############

       #############
       # 5o algarismo
       #############
       alg_text = []
    
       # acerta posicao do numero para caber todos os algarismos na vertical
       self.play( ApplyMethod(a1.move_to,0*UP))

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[5].get_center()+(i-5)*0.6*UP))


  
       tt0 = TextMobject("Possíveis algarismos").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(FadeIn(tt0))
       self.wait()

       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.play(FadeIn(alg_text[i]),run_time=0.2)
           
       self.wait()

       # muda a cor do numero
       self.play( ApplyMethod(a1.set_color,DARKER_GREY))

       tt1 = TextMobject("Probabilidade").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt1))
       self.wait()

       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,1.5*pq5[i]),run_time=0.2)
           
       self.wait()
         
       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
        
       tt2 = TextMobject("Algarismo NÃO significativo").set_color(YELLOW).scale(1.0).shift(1*UP+3.8*RIGHT)
       self.play(Transform(tt0,tt2))
       self.wait()

       # highlight alg. significativo com cor Verde
       self.play( ApplyMethod(a1.set_color,WHITE))
       self.play(  ApplyMethod(a1[:4].set_color,GREEN_SCREEN), ApplyMethod(a1[4:6].set_color,"#eb347d") )     
       self.wait()
       self.play(FadeOut(tt0))

       #############
       # 6o algarismo
       #############
       alg_text = []
    
       # acerta posicao do numero para caber todos os algarismos na vertical
       self.play( ApplyMethod(a1.move_to,2*UP))

       # cria numeros da vertical
       for i in range(len(alg)):
           x=alg[i]
           alg_text.append(TexMobject("{}".format(x)).set_color("#eb347d").\
                           scale(1.2).move_to(a1[6].get_center()+(i-9)*0.6*UP))


  
       tt0 = TextMobject("Possíveis algarismos").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(FadeIn(tt0))
       self.wait()

       # exibe numeros da vertical
       for i in range(len(alg_text)):
           self.play(FadeIn(alg_text[i]),run_time=0.2)
           
       self.wait()

       # muda a cor do numero
       self.play( ApplyMethod(a1.set_color,DARKER_GREY))

       tt1 = TextMobject("Probabilidade").set_color(YELLOW).scale(1.0).shift(2*UP+4*RIGHT)
       self.play(Transform(tt0,tt1))
       self.wait()

       # muda o tamanho de acordo com probabilidade
       for i in range(len(alg_text)):
           self.play( ApplyMethod(alg_text[i].scale,1.5*pq6[i]),run_time=0.2)
           
       self.wait()
         
       # remove numeros na vertical
       for i in range(len(alg_text)):
           self.remove(alg_text[i])
        
       tt2 = TextMobject("Algarismo NÃO significativo").set_color(YELLOW).scale(1.0).shift(1*UP+3.8*RIGHT)
       self.play(Transform(tt0,tt2))
       self.wait()

       # highlight alg. significativo com cor Verde
       self.play( ApplyMethod(a1.set_color,WHITE))
       self.play( ApplyMethod(a1[:4].set_color,GREEN_SCREEN),  ApplyMethod(a1[4:7].set_color,"#eb347d") )     
       self.wait()
       self.play(FadeOut(tt0))
       self.play(ApplyMethod(a1.move_to,0))

       b1 = TexMobject(r"\bar{y}=","3.14","1592").scale(1.4).shift(UP+3*LEFT)
       b2 = TexMobject(r"\sigma=0.031473").scale(1.4).shift(UP+3*RIGHT)
       self.play(FadeIn(b1),FadeIn(b2))
       self.wait(1)
       self.play( ApplyMethod(b1[1].set_color,GREEN_SCREEN), ApplyMethod(b1[2].set_color,BLACK))     
       self.wait(1)

       tt0 = TextMobject("E quanto aos algarismos significativos")
       tt1 = TexMobject(r"\text{de }\sigma\text{ ?}")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.scale(1.3).shift(2.8*UP)
       self.play(FadeIn(tt),FadeOut(b1),FadeOut(a1))
       self.wait()



       ## Algarismos siginificativos para o desvio padrão
       # usando formula da apostila do Prof. Brito Cruz disponível em
       # https://www.ifi.unicamp.br/~brito/graferr.pdf
       # e de discussão mostrada em  https://groups.google.com/g/sci.stat.math/c/dsgmWBLJoHc
       s0 = TextMobject("Para uma distribuição gaussiana,")
       s1 = TextMobject("o desvio padrão do desvio padrão é")
       st = VGroup(s0,s1)
       st.arrange_submobjects(DOWN,buff=0.3)
       st.scale(1.0).move_to(3*LEFT+DOWN)
       self.play(FadeIn(st))
       self.wait()

       f1=TexMobject(r"\displaystyle \sigma_{\sigma^2}=\sigma\left[\frac{2}{N-1}\right]^{\frac{1}{4}}")
       f1.move_to(1*DOWN+4*RIGHT)
       self.play(FadeIn(f1))
       self.wait()

       self.play(FadeOut(st))
       self.setup_axes(animate=False)
       
       func1 = self.get_graph(self.ff,color=YELLOW,width=1,x_min = 1, x_max = 1000)
       self.play(Write(func1))
       self.wait(2)
       #print(np.sqrt(np.sqrt(2.0/(201-1))))
       self.wait(2)

       self.play(FadeOut(self.axes),FadeOut(func1))
       s0 = TextMobject("Para termos $\\sigma_{\\sigma^2}=$ 0.001 (3\%):")
       s0.scale(1.0).move_to(3*LEFT)
       self.play(FadeIn(s0))
       self.wait(2)


       f2=TexMobject(r"\displaystyle N=1+\frac{2}{\sigma^4_{\sigma^2}/\sigma^4}")
       f2.move_to(2*DOWN+3.5*LEFT).scale(1.3).set_color(YELLOW)

       f3=TexMobject(r"\displaystyle N \simeq 2.5\text{ milhões !}")
       f3.move_to(2*DOWN+3.5*LEFT).scale(1.3).set_color(YELLOW)
       self.play(FadeIn(f2))
       self.wait(2)
       self.play(Transform(f2,f3))
       # N para 0,03
       #print(1+ 2/(0.03**4) )
       self.wait()

       self.play(FadeOut(tt),FadeOut(f2),FadeOut(s0),FadeOut(f1),FadeOut(b2))
       self.wait()

       tt0 = TextMobject("Portanto, geralmente considera-se")
       tt1 = TextMobject("apenas UM algarismo significativo em $\\sigma$")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.scale(1.3).shift(2.5*UP)
       self.play(FadeIn(tt))
       self.wait()
       
       b2 = TexMobject(r"\sigma=","0.03","1473").scale(1.4)
       self.play(FadeIn(b2))
       self.wait()
       self.play( ApplyMethod(b2[1].set_color,GREEN_SCREEN), ApplyMethod(b2[2].set_color,BLACK))     
       self.wait()

       self.play(FadeOut(b2),FadeOut(tt))
       self.wait()
       a1 = TexMobject(r"\bar{y}=3.141592").scale(1.2).shift(UP+3*LEFT)
       a2 = TexMobject(r"\sigma=0.031473").scale(1.2).shift(UP+3*RIGHT)
       self.play(Write(a1),Write(a2))
       self.wait(2)

       b1 = TexMobject(r"\bar{y}=","3.14").scale(1.8).shift(DOWN+3*LEFT)
       b2 = TexMobject(r"\sigma=","0.03").scale(1.8).shift(DOWN+3*RIGHT)
       b1[1].set_color(GREEN_SCREEN)
       b2[1].set_color(GREEN_SCREEN)
       self.play(FadeIn(b1),FadeIn(b2))
       self.wait(2)
       self.play(FadeOut(a1),FadeOut(a2))
       self.wait(2)
       self.play(FadeOut(b1),FadeOut(b2))
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
       
