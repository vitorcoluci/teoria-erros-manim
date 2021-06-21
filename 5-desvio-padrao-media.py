#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim desvio-padrao-media.py Fechamento -l

############################################
############################################


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

      tt1=TextMobject("Desvio padrão")
      tt2=TextMobject("do valor médio")
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
     "x_max": 100,
     "x_axis_width": 10,
     "x_tick_frequency": 20,
     "x_leftmost_tick": None, # Change if different from x_min
     "x_labeled_nums": [0,20,40,60,80,100],
     "x_axis_label": "$N$",
     "y_min": 0.0,
     "y_max": 1.0,
     "y_axis_height": 5,
     "y_tick_frequency": 0.2,
     "y_bottom_tick": None, # Change if different from y_min
     "y_label_decimals": 1,
     "y_labeled_nums": [0,0.2,0.4,0.6,0.8,1.0],
     "y_axis_label": "$\sigma_m/\sigma$",
     "axes_color": WHITE,
     "graph_origin": 3 * DOWN + 5 * LEFT,
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
     def ff1(self,x):
         return (1.0/(np.sqrt(x)))

     def construct(self):
       # criar valores em x com distribuição gaussiana
       def cria(n,q,media,sigma):
          for i in range(n):
              x = media + sigma* np.random.randn()
              q.append(x)
          return q

       
       # texto inicial
       tt0 = TextMobject("Considere $N$ medições,")
       tt1 = TextMobject("sob as mesmas condições,")
       tt2 = TextMobject("de uma grandeza física")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.5)

       self.play(FadeIn(tt))
       self.wait(2)
       self.play(FadeOut(tt))
       self.wait()
   
       # exemplo 
       tt0 = TextMobject("Por exemplo,")
       tt1 = TextMobject("50 medições do tempo de queda")
       tt2 = TextMobject("de um objeto de uma certa altura")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.5)

       self.play(FadeIn(tt))
       self.wait(3)
       self.play(FadeOut(tt))
       self.wait()
      
       # limites para setas que representaram os eixos
       xl=5
       yl=4
       x0=-3
       y0=-3
       
       # setas que representam os eixos
       eixox = Arrow(np.array([-xl+1,y0,0]),np.array([xl,y0,0]),width=1,color=WHITE)
       eixoy = Arrow(np.array([x0,-yl,0]),np.array([x0,yl-1,0]),width=1,color=WHITE)
       ttx = TextMobject("Tempo (s)").set_color(WHITE).scale(1.0).shift(5*RIGHT+3.5*DOWN)
       tty = TextMobject("Medidas").set_color(WHITE).scale(1.0).shift(4.5*LEFT+3*UP)
       self.play(FadeIn(eixox),FadeIn(eixoy),FadeIn(ttx),FadeIn(tty))
       self.wait(2)

       
       # media, sigma e N para o histograma
       media=0.5*(x0+xl)
       sigma=1
       n=1000
       # origem para os eixos
       oo=x0*RIGHT + y0*UP

       # adiciona pontos nas listas
      
       q=[]
       cria(n,q,media,sigma)
       hist, bin_edges = np.histogram(q,bins=15,density=True,range=(-2,4))

       # r vai guardar os retangulos do histograma
       r=[] 
       # largura dos bins do histograma
       w = bin_edges[1]-  bin_edges[0]
       
       # cria os retangulos do histograma
       for i in range(len(hist)):
          r.append(Rectangle(height=12*hist[i], 
                              width=w,
                              color=WHITE,
                              fill_color=papoula,
                              fill_opacity=0.8
                              )
                    )  
          # move o retangulo para a posição correta no grafico
          r[i].shift(y0*UP+ bin_edges[i]*RIGHT + 0.5*12*hist[i]*UP + w*RIGHT/2)
                        
       #self.add(*[ r[i] for i in range(len(hist)) ] ) 
       rrr = VGroup(*[ r[i] for i in range(len(hist)) ])
       self.play(FadeIn(rrr))

       self.wait(2)
       
       tt0 = TextMobject("Para esse conjunto,")
       tt1 = TextMobject(r"você terá um valor médio $\bar{t}$")
       tt2 = TextMobject("e um desvio padrão $\sigma$.")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(3*UP+4*RIGHT)

       self.play(FadeIn(tt))
       self.wait(3)
       self.play(FadeOut(tt))
       self.wait()
       self.remove(eixox,eixoy,ttx,tty)
       self.remove(rrr) 
       
       # comeca a descriçao das amostras
       tt0 = TextMobject("Considere agora que você")
       tt1 = TextMobject("repita, sob as mesmas condições,")
       tt2 = TextMobject("esse conjunto de $N$ medições $k$ vezes.")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.5)

       self.play(FadeIn(tt))
       self.wait(4)
       self.play(FadeOut(tt))
       self.wait()

       # cria 16 histogramas, mostra, reduz o tamanho e move para canto
       h=[]
       h_copy=[]
       k=0
       b=2
       tempo=[]
       tm=[]
       sm=[]

       for k1 in range(4):
         for k2 in range(4):
           
           # cria os eixos
           eixox = Arrow(np.array([b-xl+1,y0,0]),np.array([b+xl,y0,0]),width=1,color=WHITE)
           eixoy = Arrow(np.array([b+x0,-yl,0]),np.array([b+x0,yl-1,0]),width=1,color=WHITE)
           
       
           #gera distribuição gaussiana
           q=[]
           cria(n,q,media,sigma)
           hist, bin_edges = np.histogram(q,bins=15,density=True,range=(-2,4))
           r=[]
           w = bin_edges[1]-  bin_edges[0]
           
           # gera valores seguindo gaussiana para mostrar acima de cada histograma
           
           tempo.append(5 + 0.1* np.random.randn())
           
           # cria os retangulos do histograma
           for i in range(len(hist)):
                  r.append(Rectangle(height=12*hist[i], 
                              width=w,
                              color=WHITE,
                              fill_color=papoula,
                              fill_opacity=0.8
                              )
                    )  
                  # move o retangulo para a posição correta no grafico
                  r[i].shift(b*RIGHT+y0*UP+ bin_edges[i]*RIGHT + 0.5*12*hist[i]*UP + w*RIGHT/2)
                        
           
           h1 = VGroup(*[ r[i] for i in range(len(hist)) ])
           h2 = VGroup(h1,eixox,eixoy)
           # h é a lista com os 16 histogramas
           h.append(h2)
                    
           # exibe o histograma no tamanho original
           self.play(FadeIn(h[k]))
           self.wait()
           # faz uma copia para movê-la depois para o canto
           h_copy.append(h[k].copy())
           # h_copy contem lista com 16 histrogramas reduzidos e deslocados
           h_copy[k].scale(0.15).shift(2*DOWN + (3+b)*LEFT + 1.6*k1*UP + 1.3*k2*LEFT)
           
           ss=2*DOWN + (3+b)*LEFT + 1.6*k1*UP + 1.3*k2*LEFT

           # gera texto para ficar acima de cada histograma representando o valor medio 
           # de cada um
           ttt0= TexMobject("{:.2f}".format(tempo[k])).scale(0.6).shift(0.3*UP+2.7*RIGHT +ss)
           ttt1= TexMobject(r"\bar{t}=").scale(0.6).shift(0.3*UP+2.1*RIGHT +ss)
           ttt = VGroup(ttt0,ttt1)
           
           # tm eh a lista dos tempos para ficar acima de cada histograma
           tm.append(ttt)

           # gera texto para ficar em cada histograma representando o sigma 
           # de cada um
           ttt0=TexMobject(r"\sigma_{{}}".format(16-k)).set_color(YELLOW).scale(0.5).shift(0.6*DOWN+0.8*RIGHT+0.3*UP+2.1*RIGHT +ss)
           ttt1=TexMobject("{}".format(16-k)).set_color(YELLOW).scale(0.3).shift(0.7*DOWN+0.9*RIGHT+0.3*UP+2.1*RIGHT +ss)
           # sm contem os 16 simbolos sigma_1, sigma_2 ....
           sm.append(VGroup(ttt0,ttt1))

           self.play(Transform(h[k],h_copy[k]),FadeIn(tm[k]),FadeIn(sm[k]))       
           self.wait(0.5)   
           k = k+1



       ###
       # cria agora o histograma para os valores medios usando sigma menor (desvio padrão da media)
       eixox = Arrow(np.array([b-xl+1,y0,0]),np.array([b+xl,y0,0]),width=1,color=WHITE)
       eixoy = Arrow(np.array([b+x0,-yl,0]),np.array([b+x0,yl-1,0]),width=1,color=WHITE)
       ttx = TexMobject(r"\bar{t}").set_color(WHITE).scale(1.0).shift(6*RIGHT+3.5*DOWN)
       sigma=0.3
       
       # cria distribuição gaussiana
       q=[]
       cria(n,q,media,sigma)
       hist, bin_edges = np.histogram(q,bins=15,density=True,range=(-2,4))
       r=[]
       
       w = bin_edges[1]-  bin_edges[0]
       # cria os retangulos do histograma
       for i in range(len(hist)):
                  r.append(Rectangle(height=4*hist[i], 
                              width=w,
                              color=WHITE,
                              fill_color=papoula,
                              fill_opacity=0.8
                              )
                    )  
                  # move o retangulo para a posição correta no grafico
                  r[i].shift(b*RIGHT+y0*UP+ bin_edges[i]*RIGHT + 0.5*4*hist[i]*UP + w*RIGHT/2)
                        
           
       # h1 grupos dos retangulos do histograma
       h1 = VGroup(*[ r[i] for i in range(len(hist)) ])
       # h2 grupo do retangulos + eixos + titulo do eixo
       h2 = VGroup(h1,eixox,eixoy,ttx)
       # h0 grupo dos valores de tmedio
       h0 = VGroup(*[ tm[i] for i in range(len(tm)) ])
       # sigmas grupo dos sigmas sigma_1 , sigma_2, ....
       sigmas = VGroup(*[ sm[i] for i in range(len(sm)) ])
 
       # transforma textos dos tempos no histograma
       self.wait(2)
       
       tt0 = TextMobject("Obtém-se agora a distribuição")
       tt1 = TextMobject("dos $k$ valores médios")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2.8*RIGHT+2*UP)
       self.play(FadeIn(tt))
       self.wait(2)
       self.play(FadeOut(tt))
       self.wait(2)

       self.play(Transform(h0,h2))
       self.wait(2)
       # remove o histograma
       self.play(FadeOut(h0),FadeOut(h2),FadeOut(h1),FadeOut(eixox),FadeOut(eixoy),FadeOut(ttx))

       # começa a dedução da formula do desvio padrao da media (seguindo Vuolo pag. 99-100)
       f1 = TexMobject(r"\sigma_1^2=\displaystyle \frac{1}{N}[\sum_{i=1}^{N}(t_{i1}-t_{mv})^2]").move_to(2*RIGHT).scale(1.2)
       self.play(FadeIn(f1))
       self.wait()

       f2 = TexMobject(r"\sigma_j^2=\displaystyle \frac{1}{N}[\sum_{i=1}^{N}(t_{ij}-t_{mv})^2]").move_to(2*RIGHT).scale(1.2)

       f2a = TexMobject(r"\sigma_j^2=\displaystyle \frac{1}{N}[\sum_{i=1}^{N}(t_{ij}-t_{mv})^2]").move_to(3*RIGHT+3*UP).scale(0.7)

       f3 = TextMobject("$t_{mv}$ é o valor médio verdadeiro").next_to(f2, DOWN, buff = 0.2)
       self.play(Transform(f1,f2))
       self.wait()
       self.play(FadeIn(f3))
       self.wait()
       self.play(FadeOut(f3))
       self.wait(2)
       self.play(FadeOut(f1),FadeOut(f2))
       self.wait()
        
       f4 = TexMobject(r"\bar{t_j}=\displaystyle \frac{1}{N}[\sum_{i=1}^{N}t_{ij}").move_to(2*RIGHT).scale(1.2)
       f5 = TexMobject(r"\sigma^2_m",
                       " = ",
                       r"\displaystyle \frac{1}{k}\sum_{j=1}^{k}(\bar{t_j}-t_{mv})^2").move_to(2*RIGHT).scale(1.2)
       

       tt0 = TextMobject("Desvio padrão da média $\sigma_m$")
       tt0.set_color(YELLOW).scale(1.2).shift(2.8*RIGHT+2*UP)
       self.play(FadeIn(tt0))
       self.wait(2)
       

       self.play(FadeIn(f5))
       self.wait(2)
       
                
       f6 = TexMobject(r"\displaystyle \frac{1}{k}\sum_{j=1}^{k}[(\frac{1}{N}\sum_{i=1}^{N}t_{ij}-t_{mv})^2]").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f6))
       self.play(FadeOut(tt0))
       self.wait(3)

       f7 = TexMobject(r"\displaystyle \frac{1}{k}\sum_{j=1}^{k}\frac{1}{N^2}[\sum_{i=1}^{N}t_{ij}-Nt_{mv}]^2").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f7))
       self.wait(3)

       f7a = TexMobject(r"\displaystyle \frac{1}{k}\sum_{j=1}^{k}\frac{1}{N^2}[\sum_{i=1}^{N}t_{ij}-\sum_{i=1}^{N}t_{mv}]^2").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f7a))
       self.wait(3)

       f7b = TexMobject(r"\displaystyle \frac{1}{k}\sum_{j=1}^{k}\frac{1}{N^2}[\sum_{i=1}^{N}(t_{ij}-t_{mv})]^2").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f7b))
       self.wait(3)


       f8 = TexMobject(r"\displaystyle \frac{1}{kN^2}\sum_{j=1}^{k}\sum_{i=1}^{N}(t_{ij}-t_{mv})^2 +").next_to(f5[1], RIGHT, buff = 0.2)
  
       f9 = TexMobject(r"\displaystyle + \frac{2}{kN^2}\sum_{j=1}^{k}\sum_{i=1}^{N}\sum_{l=1,l\neq i}^{N}(t_{ij}-t_{mv})(t_{lj}-t_{mv})").scale(0.7).next_to(f5[2], DOWN, buff = 0.2)
       

       self.play(Transform(f5[2], f8),FadeIn(f9))
       self.wait(3)


       tt0 = TextMobject("Para $N$ grande e $(t_{ij}-t_{mv})$ e $(t_{lj}-t_{mv})$")
       tt1 = TextMobject("independentes entre si e ")
       tt2 = TextMobject("distribuídos aleatoriamente em torno de zero")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.2)
       tt.set_color(YELLOW).scale(0.8).shift(3*DOWN+2*RIGHT)

       self.play(FadeIn(tt))
       self.wait(4)

       f10 = TexMobject(r"+ 0").next_to(f5[2], DOWN, buff = 0.2)
       f11 = TexMobject(r"\simeq").next_to(f5[1], 0*RIGHT, buff = 0.2)
       self.play(Transform(f9,f10),Transform(f5[1],f11))
       self.wait(3)
       self.play(FadeOut(tt),FadeOut(f9),FadeOut(f10))
       self.wait(2)

       f12 = TexMobject(r"\displaystyle \frac{1}{kN^2}\sum_{j=1}^{k}\sum_{i=1}^{N}(t_{ij}-t_{mv})^2").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f12))
       self.wait(3)

       f13 = TexMobject(r"\displaystyle \frac{1}{kN}\sum_{j=1}^{k}[\frac{1}{N}\sum_{i=1}^{N}(t_{ij}-t_{mv})^2]").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f13))
       self.wait(3)

       self.play(FadeIn(f2a))
       self.wait(3)
       self.play(FadeOut(f2a))
       self.wait()

       f14 = TexMobject(r"\displaystyle \frac{1}{kN}\sum_{j=1}^{k}\sigma^2_j").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f14))
       self.wait(3)

       tt0 = TextMobject("Como os $k$ conjuntos de medições")
       tt1 = TextMobject("são similares, então os desvios padrões")
       tt2 = TextMobject("devem ser aproximadamente iguais.")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2.7*RIGHT+3*DOWN)
       self.play(FadeIn(tt))
       self.wait(3)
       self.play(FadeOut(tt))


       tt3 = TexMobject(r"\sigma_1\simeq\sigma_2\simeq\ldots\sigma_k=\sigma").set_color(WHITE).scale(1.2).shift(1.4*RIGHT+3*DOWN)
       self.play(Transform(sigmas,tt3))
       self.wait()
       
       rrr1 = VGroup(*[ h_copy[i] for i in range(len(h_copy)) ])
       rrr2 = VGroup(*[ h[i] for i in range(len(h)) ])

       self.play(FadeOut(rrr1),FadeOut(rrr2))
       
       self.wait(2)

       f15 = TexMobject(r"\displaystyle \frac{1}{N}[\frac{1}{k}\sum_{j=1}^{k}\sigma^2_j]").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f15))
       self.wait(2)

       f15a = TexMobject(r"\displaystyle \frac{1}{N}[\frac{k\sigma^2}{k} ]").next_to(f5[1], RIGHT, buff = 0.2)
       self.remove(sigmas)
       self.play(Transform(f5[2], f15a))
       self.wait(2)

       f16 = TexMobject(r"\displaystyle \frac{\sigma^2}{N}").next_to(f5[1], RIGHT, buff = 0.2)
       self.play(Transform(f5[2], f16))
       ###
       self.wait(2)
       self.play(FadeOut(f5[0]),FadeOut(f5[1]),FadeOut(f5[2]),FadeOut(f16))

       f17 = TexMobject(r"\sigma^2_m\simeq \displaystyle \frac{\sigma^2}{N}").move_to(2*RIGHT).scale(1.2)
       self.play(FadeIn(f17))
       self.wait(2)
       self.play(FadeOut(f17))

       f18 = TexMobject(r"\sigma_m\simeq \displaystyle \frac{\sigma}{\sqrt{N}}").move_to(2*RIGHT).scale(1.2)
       self.play(FadeIn(f18))
       self.wait(2)
       
       self.setup_axes(animate=False)
       self.wait()
       
       func1 = self.get_graph(self.ff1,color=YELLOW,width=1,x_min = 1, x_max = 100)
       self.play(Write(func1))
       self.wait(4)
       
       tt0 = TextMobject("O desvio padrão da média $\sigma_m$")
       tt1 = TextMobject("é a incerteza final correspondente")
       tt2 = TextMobject("aos erros estatísticos nas medições")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2.8*RIGHT+2*UP)
       self.play(FadeIn(tt))
       self.wait(4)
       self.play(FadeOut(tt))
       

       tt0 = TextMobject("Na ausência de erros sistemáticos,")
       tt1 = TextMobject("o desvio padrão da média")
       tt2 = TextMobject("é a incerteza padrão no resultado final.")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).shift(2.8*RIGHT+2*UP)
       self.play(FadeIn(tt))
       self.wait(5)
        
     
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
