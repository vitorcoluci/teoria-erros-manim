#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim histograma.py Fechamento -l

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
      tt2=TextMobject("de")
      tt3=TextMobject("Medições")
      tt1.shift(0.8*UP)
      tt3.shift(0.8*DOWN)

      titulo=VGroup(tt1,tt2,tt3)
      titulo.scale(3.0)
      titulo.set_color(papoula)
         
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
     "x_labeled_nums": [0,1,2,3,4,5,6,7,8,9,10],
     "x_axis_label": None,
     "y_min": 0.0,
     "y_max": 100,
     "y_axis_height": 5,
     "y_tick_frequency": 20,
     "y_bottom_tick": None, # Change if different from y_min
     "y_labeled_nums": [0,20,40,60,80,100],
     "y_axis_label": None,
     "y_label_decimals": 1,
     "axes_color": WHITE,
     "graph_origin": 3 * DOWN + 6 * LEFT,
     "exclude_zero_label": False,
     "num_graph_anchor_points": 25,
     "default_graph_colors": [BLUE, GREEN, YELLOW],
     "default_derivative_color": GREEN,
     "default_input_color": YELLOW,
     "default_riemann_start_color": BLUE,
     "default_riemann_end_color": GREEN,
     "area_opacity": 0.8,
     "num_rects": 50,
     } 
     #definição da função gaussiana a ser usada no final da animação
     def f1(self,x):
         return (250.0/(1.00364*np.sqrt(2.0*np.pi)))*np.exp(-np.square(x-5.0)/(2.0*np.square(1.00364)))

     def construct(self):
       # criar valores em x com distribuição gaussiana e 
       # as linhas verticais que representam as medidas
       def cria(n,p,q,media,sigma,x0,y0):
          for i in range(n):
              x = media + sigma* np.random.randn()
              q.append(x)
              x=x-media
              p.append(Line(np.array([x-x0,-0.2-y0,0]),np.array([x-x0,0.2-y0,0]),width=1,color=apatita))
              
          return p,q
       
       # numero maximo de medidas
       nmax=500
   
       # origem do grafico
       oo = 3 * DOWN + 6 * LEFT
       # centro da reta horizontal
       x0=1
       y0=-3.5
       

       # reta horizontal para representar os valores das medições
       line=Line(np.array([-5,0-y0,0]),np.array([5,0-y0,0]),width=3,color=WHITE)
       self.add(line)
       self.wait(2)

       # introdução 
       l1 = Line(np.array([0-x0,-0.2-y0,0]),np.array([0-x0,0.2-y0,0]),width=1,color=apatita)
  
       t0 = TexMobject("5.2")
       
       t0.shift(2.7*UP+2*LEFT)
       t0.set_color(apatita)
       t0.scale(1.5)
     
       t1 = TextMobject("Valor da medição")
       t2 = TextMobject("de uma grandeza física experimental")
       t2.shift(DOWN)
       t1.set_color(YELLOW)
       t1.scale(1.5)
       t2.set_color(YELLOW)
       t2.scale(1.5)
      
       arrow1 = Arrow(l1.get_center(),t1.get_center())

       self.add(l1)
       self.wait(0.5)
       self.play(FadeIn(t0))
       self.wait()
       self.play(GrowArrow(arrow1),FadeIn(t1),FadeIn(t2))
       self.wait(2)
       self.play(FadeOut(arrow1),FadeOut(t1),FadeOut(t2),FadeOut(t0))
       self.wait()

       t1 = TextMobject("Por exemplo,")
       t2 = TextMobject("o tempo de queda de um objeto")
       t3 = TextMobject("de uma certa altura")
       t2.shift(DOWN)
       t3.shift(2*DOWN)
       t1.set_color(YELLOW)
       t1.scale(1.5)
       t2.set_color(YELLOW)
       t2.scale(1.5)
       t3.set_color(YELLOW)
       t3.scale(1.5)

       self.play(FadeIn(t1),FadeIn(t2),FadeIn(t3))
       self.wait(2)
       self.play(FadeOut(t1),FadeOut(t2),FadeOut(t3))
       self.wait()


       l2 = Line(np.array([1-x0,-0.2-y0,0]),np.array([1-x0,0.2-y0,0]),width=1,color=apatita)
       l3 = Line(np.array([-0.5-x0,-0.2-y0,0]),np.array([-0.5-x0,0.2-y0,0]),width=1,color=apatita)
       l4 = Line(np.array([-1.2-x0,-0.2-y0,0]),np.array([-1.2-x0,0.2-y0,0]),width=1,color=apatita)
  
       t1 = TextMobject("Realização de $N$ medições")
       t2 = TextMobject("sob as mesmas condições")
       t2.shift(DOWN)
       t1.set_color(YELLOW)
       t1.scale(1.5)
       t2.set_color(YELLOW)
       t2.scale(1.5)

       self.play(FadeIn(t1),FadeIn(t2))
       self.wait()
       self.play(FadeIn(l2))
       self.wait()
       self.play(FadeIn(l3))
       self.wait()
       self.play(FadeIn(l4))
       self.wait()
       self.play(FadeOut(line),FadeOut(l1),FadeOut(l2),FadeOut(l3),FadeOut(l4),FadeOut(t1),FadeOut(t2))
       self.wait()

       # apresntação do histograma para cada conjunto de valores    
       line=Line(np.array([-5-x0,0-y0,0]),np.array([5-x0,0-y0,0]),width=3,color=WHITE)
       self.add(line)
       self.wait(2)

       self.setup_axes(animate=False)
       
       # nome do eixos do gráfico
       s1 = TextMobject("Medições")
       s1.shift(oo+5.6*UP)
       s1.set_color(WHITE)
       s1.scale(1.0)
       self.add(s1)

       s2 = TextMobject("Valor da medição")
       s2.shift(oo+10*RIGHT+0.7*DOWN)
       s2.set_color(WHITE)
       s2.scale(1.0)
       self.add(s2)

       self.wait(2)

       p=[]
       q=[]
       dn = 50

       #loop para criar os histogramas
       for n in range(0,nmax,dn):
         media=5
         sigma=1
         
         # adiciona pontos nas listas
         cria(dn,p,q,media,sigma,x0,y0)
         hist, bin_edges = np.histogram(q,bins=20,density=False,range=(0,10))
         
         r=[]
         
         # cria os retangulos do histograma
         for i in range(len(hist)):
           # a altura do retangulo foi ajustada de acordo com a altura do 
           # eixo y: depende do valor "y_max" e "y_axis_height",
           # o fator de escala fica : y_axis_height/y_max = 5/100 = 0.05
           r.append(Rectangle(height=0.05*hist[i], 
                              width=0.5,
                              color=WHITE,
                              fill_color=papoula,
                              fill_opacity=0.8
                              )
                    )  
           # move o retangulo para a posição correta no grafico
           r[i].shift(oo + bin_edges[i]*RIGHT + 0.5*0.05*hist[i]*UP + 0.25*RIGHT)
                        
         t_1 = TexMobject(f'N={n+50}')
         t_1.shift(2*UP+5*RIGHT)
         t_1.set_color(papoula)
         t_1.scale(1.5)
         self.add(t_1) 

         for i in range(len(p)):
                self.add(p[i])
                
     
         # exibe o histograma
         self.add(*[ r[i] for i in range(len(hist)) ] ) 
         self.wait(2)  
         # remove o histograma
         self.remove(*[ r[i] for i in range(len(hist)) ] ) 
         self.remove(t_1) 
       #final do loop dos histogramas
       
       self.remove(line)
       self.remove(*[ p[i] for i in range(len(p)) ] )
       self.add(*[ r[i] for i in range(len(hist)) ] ) 

       
       #faz grafico da gausiana
       func1 = self.get_graph(self.f1,color=YELLOW)
       self.play(FadeIn(func1))
       self.wait(3)

       g1 = TextMobject("Gaussiana")
       g1.set_color(YELLOW)
       g1.scale(1.5)
       g1.shift(4.5*RIGHT)
       
       arrow1 = Arrow(0*RIGHT,3*RIGHT)
       arrow1.set_color(YELLOW)
       self.play(GrowArrow(arrow1),FadeIn(g1))
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
