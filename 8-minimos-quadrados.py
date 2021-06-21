#!/usr/bin/env python

#python3 -m manim template-animacao.py Fechamento -l

# template para animacoes dentro do Projeto Explora
# composição cenas 1...n
# 1) Cena de abertura
# 2) cenas intermediárias
# ...
# n) Cena de fechamento

# os objetos, textos, etc devem seguir 
# cores que estejam em harmonia com 
# as cores da sala:
#
# Apatita (verde)   : código Hex "#43bfca"
# Papoula (laranja) : código Hex "#dc6a40"

apatita = "#43bfca"
papoula = "#dc6a40"
azul="#0000ff"

# cores Manim
# https://www.reddit.com/r/manim/comments/dzxoen/predefined_color_scheme/


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

      tt1=TextMobject("Método dos Mínimos Quadrados")
      tt2=TextMobject("Ajuste Linear")
      titulo = VGroup(tt1,tt2)
      titulo.arrange_submobjects(DOWN,buff=0.3)
      titulo.set_color(papoula).scale(1.6)
         
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
     "x_max": 1,
     "x_axis_width": 6,
     "x_tick_frequency": 1,
     "x_leftmost_tick": None, # Change if different from x_min
     "x_labeled_nums": None,#[0,1,2,3,4,5,6,7,8,9,10],
     "x_axis_label": "$x$",
     "y_min": 0.0,
     "y_max": 1.0,
     "y_axis_height": 6,
     "y_tick_frequency": 1,
     "y_bottom_tick": None, # Change if different from y_min
     "y_label_decimals": 1,
     "y_labeled_nums": None,
     "y_axis_label": "$y$",
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
     "rate1": TAU/4, # 2Pi/(tempo que dura a animação selt.wait(4)
     "theta01": 0,
     "rate2": TAU/4, # 2Pi/(tempo que dura a animação selt.wait(4)
     "theta02": 0,
     "rate3": TAU/4, # 2Pi/(tempo que dura a animação selt.wait(4)
     "theta03": 0,
     "rate4": TAU/4, # 2Pi/(tempo que dura a animação selt.wait(4)
     "theta04": 0,
     "rate": TAU/4, # 2Pi/(tempo que dura a animação selt.wait(4)
     "theta0": 0,
      "reta_config":{
            "x_min": -7,
            "x_max": 1,
            "color": YELLOW,
            },
     } 

    def get_reta(self, theta):
        c = FunctionGraph(
                lambda x: (1 + 0.5 * np.sin(theta))*(3 + x), # reta y = (1 + 0.5 * sin(theta(t)))(a+bx)
                **self.reta_config
                )
        return c


    #def get_yp(self, x, theta):
    #    return (1 + 0.5 * np.sin(theta))*(3 + x)

    def get_quad(self, x0, y0,theta):
        lado = np.abs((1 + 0.5 * np.sin(theta))*(3 + x0)-y0)
        
        r=Square(side_length=lado, fill_color=YELLOW_E, fill_opacity=0.7, color=YELLOW_E)
         
        if (1 + 0.5 * np.sin(theta))*(3 + x0)>y0: 
             r.move_to(np.array([x0+lado/2,y0+lado/2,0]))
        else:
             r.move_to(np.array([x0+lado/2,y0-lado/2,0]))

        return r


    def construct(self):
       #grid=ScreenGrid()
       #self.add(grid)

       def get_yp(x, theta):
        return (1 + 0.5 * np.sin(theta))*(3 + x)

       # função update para mudar reta
       # dt = 1 / fps = tempo de cada frame = 1/15 
       def update_curve(c, dt):
            rate = self.rate * dt # taxa em ( 2 PI / tempo total da animacao )* (tempo de cada frame)
            c.become(self.get_reta(self.theta0 + rate))
            self.theta0 += rate


       def update_quad1(c,dt):
            rate = self.rate1 * dt # taxa em ( 2 PI / tempo total da animacao )* (tempo de cada frame)
#[-4.8, -3.5999999999999996, -2.4000000000000004, -1.1999999999999993]
#[-1.2000000000000002, -0.9000000000000004, 1.5, 1.62] 
            x0=-4.8
            y0=-1.5
            yr = (1 + 0.5 * np.sin(self.theta01 + rate))*(3 + x0)
            
            lado = np.abs(yr-y0)
           
            c2=Square(side_length=lado, fill_color=YELLOW_E, fill_opacity=0.7, color=YELLOW_E)
            
            if yr>y0: 
             c2.move_to(np.array([x0+lado/2,y0+lado/2,0]))
            else:
             c2.move_to(np.array([x0+lado/2,y0-lado/2,0]))
            
          
            c.become(c2)
            self.theta01 += rate

            
       def update_quad2(c,dt):
            rate = self.rate2 * dt # taxa em ( 2 PI / tempo total da animacao )* (tempo de cada frame)
#[-4.8, -3.5999999999999996, -2.4000000000000004, -1.1999999999999993]
#[-1.2000000000000002, -0.9000000000000004, 1.5, 1.62] 
            x0=-3.6
            y0=-0.6
            yr = (1 + 0.5 * np.sin(self.theta02 + rate))*(3 + x0)
            
            lado = np.abs(yr-y0)
           
            c2=Square(side_length=lado, fill_color=YELLOW_E, fill_opacity=0.7, color=YELLOW_E)
            
            if yr>y0: 
             c2.move_to(np.array([x0+lado/2,y0+lado/2,0]))
            else:
             c2.move_to(np.array([x0+lado/2,y0-lado/2,0]))
            
          
            c.become(c2)
            self.theta02 += rate
            
       def update_quad3(c,dt):
            rate = self.rate3 * dt # taxa em ( 2 PI / tempo total da animacao )* (tempo de cada frame)
            x0=-2.4
            y0=0.9
            yr = (1 + 0.5 * np.sin(self.theta03 + rate))*(3 + x0)
            
            lado = np.abs(yr-y0)
           
            c2=Square(side_length=lado, fill_color=YELLOW_E, fill_opacity=0.7, color=YELLOW_E)
            
            if yr>y0: 
             c2.move_to(np.array([x0+lado/2,y0+lado/2,0]))
            else:
             c2.move_to(np.array([x0+lado/2,y0-lado/2,0]))
            
          
            c.become(c2)
            self.theta03 += rate
        
       def update_quad4(c,dt):
            rate = self.rate4 * dt # taxa em ( 2 PI / tempo total da animacao )* (tempo de cada frame)
            x0=-1.2
            y0=1.62
            yr = (1 + 0.5 * np.sin(self.theta04 + rate))*(3 + x0)
            
            lado = np.abs(yr-y0)
           
            c2=Square(side_length=lado, fill_color=YELLOW_E, fill_opacity=0.7, color=YELLOW_E)
            
            if yr>y0: 
             c2.move_to(np.array([x0+lado/2,y0+lado/2,0]))
            else:
             c2.move_to(np.array([x0+lado/2,y0-lado/2,0]))
            
          
            c.become(c2)
            self.theta04 += rate
 
       # para criar pontos com diferentes opacidades
       def cria(x0,y0,n,cor,ox,oy,sx,sy,sigma,r):
       
         if n>20: 
             dx = 0.05
         else:
             dx = 0.2

         for i in range(n):
               
              k= i - n + (n+1)/2
              x = 1-np.abs(k)*dx
              r.append(Dot(point=(x0,y0 + (sigma*k/((n+1)/2 -1))*sy,0),
                           color=cor,
                           radius=0.1,
                           fill_opacity=x))
         
         return r

       # cria barra de erros
       def berro(x0,y0,sigma,r):
         
         r.append(Line(np.array([x0,y0+sigma,0]),np.array([x0,y0-sigma,0])))
         r.append(Line(np.array([x0-0.2,y0+sigma,0]),np.array([x0+0.2,y0+sigma,0])))
         r.append(Line(np.array([x0-0.2,y0-sigma,0]),np.array([x0+0.2,y0-sigma,0])))

         
         return r

       # cria quadrados
       def quad(x0,y0,xr,yr):
         lado = np.abs(yr-y0)
         
         r=Square(side_length=lado, fill_color=YELLOW_E, fill_opacity=0.7, color=YELLOW_E)
         
         if yr>y0: 
             r.move_to(np.array([x0+lado/2,y0+lado/2,0]))
         else:
             r.move_to(np.array([x0+lado/2,y0-lado/2,0]))

         return r

       
       # configuracoes
       #origem 
       ox = -6 
       oy = -3

       #escala
       sx = 6
       sy = 6
      
       #parametros da reta a + bx na tela do Manim
       a=3
       b=1
      
       #dados
       xp=[0.2,0.4,0.6,0.8]
       yp=[0.25,0.4,0.65,0.77]
       sigmap=[0.05, 0.1, 0.08, 0.06]
       
       #valores em escala
       x=[ox+xp[0]*sx, ox+xp[1]*sx,  ox+xp[2]*sx,  ox+xp[3]*sx]
       y=[oy+yp[0]*sy, oy+yp[1]*sy,  oy+yp[2]*sy,  oy+yp[3]*sy]
       sigma = [sigmap[0]*sy,sigmap[1]*sy,sigmap[2]*sy,sigmap[3]*sy]
       
       dot1 = Dot(point=(x[0], y[0], 0),color=GREEN_SCREEN, radius=0.1)
       dot2 = Dot(point=(x[1], y[1], 0),color=GREEN_SCREEN, radius=0.1)
       dot3 = Dot(point=(x[2], y[2], 0),color=GREEN_SCREEN, radius=0.1)
       dot4 = Dot(point=(x[3], y[3], 0),color=GREEN_SCREEN, radius=0.1)

       xy1=TexMobject("(x_1,y_1)").set_color(WHITE).move_to(dot1.get_center()+0.5*RIGHT+0.5*DOWN).scale(0.7)
       xy2=TexMobject("(x_2,y_2)").set_color(WHITE).move_to(dot2.get_center()+0.5*RIGHT+0.5*DOWN).scale(0.7)
       xy3=TexMobject("(x_3,y_3)").set_color(WHITE).move_to(dot3.get_center()+0.5*RIGHT+0.5*DOWN).scale(0.7)
       xy4=TexMobject("(x_4,y_4)").set_color(WHITE).move_to(dot4.get_center()+0.5*RIGHT+0.5*DOWN).scale(0.7)

       #xys1=TexMobject("(x_1,y_1\pm\sigma_1)").set_color(BLUE).move_to(dot1.get_center()+UP).scale(0.7)
       #xys2=TexMobject("(x_2,y_2\pm\sigma_2)").set_color(BLUE).move_to(dot2.get_center()+UP).scale(0.7)
       #xys3=TexMobject("(x_3,y_3\pm\sigma_3)").set_color(BLUE).move_to(dot3.get_center()+UP).scale(0.7)
       #xys4=TexMobject("(x_4,y_4\pm\sigma_4)").set_color(BLUE).move_to(dot4.get_center()+UP).scale(0.7)
    
            

       # texto inicial
       
       tt0 = TextMobject("Considere o conjunto de")
       tt1 = TextMobject("pontos experimentais $(x_i,y_i)$")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(3.4*RIGHT+2.7*UP)

       self.play(FadeIn(tt))
       self.wait()

       self.setup_axes(animate=False)
       self.wait()
       self.play(FadeIn(dot1),FadeIn(dot2),FadeIn(dot3),FadeIn(dot4))
       
       self.wait()
       
       # mostrar pontos sem barras de erros
       # mostrar (x1,y1), etc para cada ponto
       self.play(FadeIn(xy1),FadeIn(xy2),FadeIn(xy3),FadeIn(xy4))
       self.wait()

       self.play(FadeOut(tt))
       self.play(FadeOut(xy1),FadeOut(xy2),FadeOut(xy3),FadeOut(xy4))
       

       # escolher um ponto e mostrar que ele tem incerteza
       # a incerteza pode ser pequena ou grande
       # mostrar os varios dots para o caso de pequena e grande

       tt0 = TextMobject("Todo ponto experimental")
       tt1 = TextMobject("tem uma incerteza associada a ele.")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(2.7*RIGHT+2.7*UP)

       self.play(FadeIn(tt))
       self.wait()

       n=11
       r=[]       
       cria(x[1],y[1],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[1],r)
       d2 = VGroup(*[ r[i] for i in range(n) ])

       self.play(FadeIn(d2))
       self.wait()

       t0 = TextMobject("Essa incerteza pode")
       t1 = TextMobject("ser grande")
       ttt = VGroup(t0,t1)
       ttt.arrange_submobjects(DOWN,buff=0.3)
       ttt.set_color(YELLOW).scale(1.0).move_to(3.4*RIGHT)

       self.play(FadeIn(ttt))
       self.wait()
       self.play(FadeOut(d2))

       n=41
       r=[]       
       cria(x[1],y[1],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[1]*4,r)
       d2 = VGroup(*[ r[i] for i in range(n) ])
       
       self.play(FadeIn(d2))
       self.wait()
       self.play(FadeOut(ttt))


       t0 = TextMobject("ou pode")
       t1 = TextMobject("ser pequena")
       ttt = VGroup(t0,t1)
       ttt.arrange_submobjects(DOWN,buff=0.3)
       ttt.set_color(YELLOW).scale(1.0).move_to(3.4*RIGHT)

       self.play(FadeIn(ttt))
       self.wait()
       self.play(FadeOut(d2))

       n=15
       r=[]       
       cria(x[1],y[1],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[1]*0.3,r)
       d2 = VGroup(*[ r[i] for i in range(n) ])
       
       self.play(FadeIn(d2))
       self.wait()
       self.play(FadeOut(ttt), FadeOut(tt),FadeOut(d2))


       # colocar os dots para todos os pontos

       n=11
       r=[]       
       cria(x[0],y[0],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[0],r)
       d1 = VGroup(*[ r[i] for i in range(n) ])

       r=[]       
       cria(x[1],y[1],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[1],r)
       d2 = VGroup(*[ r[i] for i in range(n) ])

       r=[]       
       cria(x[2],y[2],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[2],r)
       d3 = VGroup(*[ r[i] for i in range(n) ])

       r=[]       
       cria(x[3],y[3],n,GREEN_SCREEN,ox,oy,sx,sy,sigmap[3],r)
       d4 = VGroup(*[ r[i] for i in range(n) ])

       self.play(FadeIn(d1),FadeIn(d2),FadeIn(d3),FadeIn(d4))
       self.wait()
       

       # indicar as barras de erros
       # mostrar (x1,y1,sigma1), etc para cada ponto

       tt0 = TextMobject("Essas incertezas podem ser")
       tt1 = TextMobject("representadas com barras de erro")
       tt2 = TexMobject("(x_i,y_i\pm\sigma_i)")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(3.4*RIGHT+2.7*UP)

       self.play(FadeIn(tt))
       self.wait()

       r=[] 
       berro(x[0],y[0],sigma[0],r)
       bar1=VGroup(*[ r[i] for i in range(3) ])
       
       r=[] 
       berro(x[1],y[1],sigma[1],r)
       bar2=VGroup(*[ r[i] for i in range(3) ])

       r=[] 
       berro(x[2],y[2],sigma[2],r)
       bar3=VGroup(*[ r[i] for i in range(3) ])

       r=[] 
       berro(x[3],y[3],sigma[3],r)
       bar4=VGroup(*[ r[i] for i in range(3) ])

       self.play(FadeIn(bar1),FadeIn(bar2),FadeIn(bar3),FadeIn(bar4))
       self.wait()
       

       self.remove(d1,d2,d3,d4)
       
       self.wait()
       self.play(FadeOut(tt))
      
       # metodo dos minimos quadrados
       # obter a melhor descrição dos dados de acordo com alguma função
       # matemática (teoria), no nosso caso, um reta.
       # essa teoria previria o valor de y para o ponto x (y_teo)
       # esse y_teo seria dado por uma funçao (reta, no nosso caso) y_teo=y_teo(a,b)=a+bx
       tt0 = TextMobject("Como obter a melhor descrição")
       tt1 = TextMobject("dos dados,")
       tt2 = TextMobject("de acordo com")
       tt3 = TextMobject("uma função matemática (teoria)?")
       tt = VGroup(tt0,tt1,tt2,tt3)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(3.2*RIGHT+2.5*UP)

       self.play(FadeIn(tt))
       self.wait(3)
       self.play(FadeOut(tt))

       tt0 = TextMobject("Essa teoria pode prever $y_{\\text{teo}}$:")
       tt1 = TextMobject("o valor de $y$ para cada $x$.")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(3.4*RIGHT+2.7*UP)

       self.play(FadeIn(tt))
       self.wait(3)
       
       stt0 = TextMobject("Veremos aqui o caso")
       stt1 = TextMobject("de uma reta: $y_{\\text{teo}}=a + bx$")
       stt = VGroup(stt0,stt1)
       stt.arrange_submobjects(DOWN,buff=0.3)
       stt.set_color(YELLOW).scale(1.0).move_to(3.4*RIGHT+0*UP)

       self.play(FadeIn(stt))
       self.wait(1)
       f = self.get_reta(0)
       self.play(ShowCreation(f))
       self.wait(2)
       self.play(FadeOut(tt))
       self.wait(2)
       self.play(FadeOut(bar1),FadeOut(bar2),FadeOut(bar3),FadeOut(bar4),FadeOut(f))
       self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4))
       self.play(FadeOut(self.axes),FadeOut(stt))
       self.wait()

       # se f é a função que fornece o valor verdadeiro y para cada x_i

       # probabilidade de obter o valor (x_i,y_i,\sigma_i)
       #P_i \propto \frac{1}\{\sigma_i} e^{-\frac{1}{2}(\frac{y_i-y_teo(a,b)}{\sigma_i})^2}

       tt0 = TextMobject("A probabilidade de")
       tt1 = TextMobject("obter o ponto $(x_i,y_i,\\sigma_i)$ é:")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(0*RIGHT+2.7*UP)

       t1 = TexMobject(r"P_i \propto \frac{1}{\sigma_i} e^{-\frac{1}{2}(\frac{y_i-y_{\text{teo}}(a,b)}{\sigma_i})^2}").scale(1.8)
      
       self.play(FadeIn(tt))
       self.wait()
       self.play(Write(t1))
       self.wait(2)

       self.play(FadeOut(tt), FadeOut(t1))
       # a probalilidade P de ocorre o conjunto dos resultados é
       # P = P_1P_2\ldots P_n \propto \frac{1}\{\sigma_1\sigma_2\ldots \sigma_n} e^{-\frac{1}{2}\sum (\frac{y_i-y_teo(a,b)}{\sigma_i})^2}

       tt0 = TextMobject("A probabilidade de obter")
       tt1 = TextMobject("TODOS os pontos do CONJUNTO é:")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(2.7*UP)

       self.play(FadeIn(tt))
       self.wait()
       tc = TexMobject(r"P =","P_1","P_2","P_3","\ldots P_n").scale(1.8)
       self.play(FadeIn(tc[0]),run_time=0.5)
       self.play(FadeIn(tc[1]),run_time=0.5)
       self.play(FadeIn(tc[2]),run_time=0.5)
       self.play(FadeIn(tc[3]),run_time=0.5)
       self.play(FadeIn(tc[4]),run_time=0.5)
       self.wait(2)
       self.play(FadeOut(tc),run_time=1)
       
       tc1 = TexMobject(r"P  \propto \frac{1}{\sigma_1\sigma_2\ldots \sigma_n} e^{-\frac{1}{2}\sum (\frac{y_i-y_{\text{teo}}(a,b)}{\sigma_i})^2}").scale(1.4)
       self.play(FadeIn(tc1))
       self.wait(2)

       tc2 = TexMobject(r"P  \propto \frac{1}{\sigma_1\sigma_2\ldots \sigma_n} e^{-\frac{1}{2}S^2}").scale(1.3)

       self.play(Transform(tc1,tc2),run_time=2)
       self.wait()

       s = TexMobject(r"S^2=\sum_{i=1}^N (\frac{y_i-y_{\text{teo}}(a,b)}{\sigma_i})^2").scale(1.7).move_to(2.5*DOWN)
       self.play(FadeIn(s),run_time=1)

       self.wait()
       self.play(FadeOut(tt))
       # P = \propto \frac{1}\{\sigma_1\sigma_2\ldots \sigma_n} e^{-\frac{1}{2}S^2}
       # S^2=\sum_i^N (\frac{y_i-y_teo(a,b)}{\sigma_i})^2

       # o método da máxima verossimilhança indica que as melhores aproximações para os parâmetros a e b
       # são aquelas que levam a um máximo de P
       tt0 = TextMobject("O método da máxima verossimilhança indica")
       tt1 = TextMobject("que as melhores aproximações para os parâmetros $a$ e $b$")
       tt2 = TextMobject("são aquelas que levam a um máximo de $P$")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.0).move_to(2.7*UP)

       self.wait()
       self.play(FadeIn(tt))
       self.wait(2)
       self.play(FadeOut(tc1))
       self.wait()

       # o máximo ocorre quando S^2 é minímo

       stt0 = TextMobject("Isso ocorre quando $S^2$ é mínimo")
       stt0.set_color(YELLOW).scale(1.0).move_to(0.5*UP)
       self.play(FadeIn(stt0))
       self.wait(3)
       self.play(FadeOut(stt0),FadeOut(tt))
       self.play(ApplyMethod(s.scale,0.6))
       self.play(ApplyMethod(s.move_to,3.5*RIGHT+2.5*UP))
       self.wait(2)
       #(y_i-y_teo(a,b))^2 é a área do quadrado de lado que corresponde a distância vertical entre 
       # o ponto experimental e a previsão teórica y_i-y_teo(a,b)

       self.setup_axes(animate=False)
       self.wait()
       self.play(FadeIn(dot1),FadeIn(dot2),FadeIn(dot3),FadeIn(dot4))
       self.play(FadeIn(bar1),FadeIn(bar2),FadeIn(bar3),FadeIn(bar4))
       self.wait()
       
       f = self.get_reta(0)
       self.play(ShowCreation(f))
       self.wait(2)

       # e S^2 é a soma das áreas ponderadas pela incerteza de cada ponto experimental

       # pontos mais precisos tem peso menor

       tt0 = TextMobject("$(y_i-y_{\\text{teo}(a,b)})^2$ ") 
       tt1 = TextMobject("é a área do quadrado de lado igual")
       tt2 = TextMobject("à distância vertical entre")
       tt3 = TextMobject("o ponto experimental $(y_i)$")
       tt4 = TextMobject("e a previsão teórica $y_{\\text{teo}}(a,b)$")
       tt = VGroup(tt0,tt1,tt2,tt3,tt4)
       tt.arrange_submobjects(DOWN,buff=0.25)
       tt.set_color(YELLOW_E).scale(0.9).move_to(0.5*DOWN+2.6*RIGHT)
       self.play(FadeIn(tt))
       self.wait(3)
       
       circle = Circle(radius=1,color=GREEN_SCREEN).move_to(4.8*LEFT+1.5*DOWN)
       aa = TextMobject("Pontos mais precisos") 
       bb = TextMobject("tem peso maior !")
       ta = VGroup(aa,bb)
       ta.arrange_submobjects(DOWN,buff=0.25)
       ta.set_color(GREEN_SCREEN).scale(0.8).move_to(0.5*UP+4.5*LEFT)
       self.play(FadeIn(ta), run_time = 2)
       self.play(FadeIn(circle), run_time = 2)      
       self.play(FadeOut(ta), run_time = 2)
       self.play(FadeOut(circle), run_time = 2) 

       quad1=self.get_quad(x[0],y[0],0)
       quad2=self.get_quad(x[1],y[1],0)
       quad3=self.get_quad(x[2],y[2],0)
       quad4=self.get_quad(x[3],y[3],0)
       self.play(FadeIn(quad1),FadeIn(quad2),FadeIn(quad3),FadeIn(quad4))
       self.wait(2)
       f.add_updater(update_curve)
       quad1.add_updater(update_quad1)
       quad2.add_updater(update_quad2)
       quad3.add_updater(update_quad3)
       quad4.add_updater(update_quad4)
       
       self.wait(4)
 
       f.remove_updater(update_curve)
       quad1.remove_updater(update_quad1)
       quad2.remove_updater(update_quad2)
       quad3.remove_updater(update_quad3)
       quad4.remove_updater(update_quad4)

       self.wait(2)
       
       self.play(FadeOut(tt))
       self.wait()
       mmq = TextMobject("Método do Mínimos Quadrados").set_color(YELLOW).scale(1.2).move_to(0.5*DOWN+2.5*RIGHT)
       self.play(Write(mmq))
       self.wait(2)

       self.play(FadeOut(quad1),FadeOut(quad2),FadeOut(quad3),FadeOut(quad4))
       self.play(FadeOut(bar1),FadeOut(bar2),FadeOut(bar3),FadeOut(bar4),FadeOut(f))
       self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4))
       self.play(FadeOut(self.axes),FadeOut(mmq))
       self.wait()

       # mostrar o update indicando a reta, os pontos, os quadrados no grafico, a pilha de quadrados,
       # o valor de S^2: a media que muda a inclinação da reta a+b(sin(dt))*x vai se alterando todas essas
       # quantidades

       # a determinação dos melhores parâmetros
       # \frac{\partial S^2}{\partial a}=0
       # \frac{\partial S^2}{\partial b}=0

       tt0 = TextMobject("A determinação ") 
       tt1 = TextMobject("dos melhores parâmetros")
       tt2 = TextMobject("é feita minimizando $S^2$")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(WHITE).scale(1.0).move_to(2.5*UP+3*LEFT)
       self.play(FadeIn(tt))
       self.wait(2)
 
       s1 = TexMobject(r"\frac{\partial S^2}{\partial a}=0") 
       s2 = TexMobject(r"\frac{\partial S^2}{\partial b}=0") 
       ss = VGroup(s1,s2)
       ss.arrange_submobjects(DOWN,buff=0.3)
       ss.scale(1.2).move_to(DOWN)
       self.play(FadeIn(ss))
       self.wait(2)

       # \sum (\frac{y_i-a+bx_i}{\sigma_i^2})=0
       # \sum (\frac{(y_i-a+bx_i)x_i}{\sigma_i^2})=0

       sa = TexMobject("\\sum (\\frac{y_i-a+bx_i}{\\sigma_i^2})=0") 
       sb = TexMobject("\\sum (\\frac{(y_i-a+bx_i)x_i}{\\sigma_i^2})=0") 
       sss = VGroup(sa,sb)
       sss.arrange_submobjects(DOWN,buff=0.3)
       sss.scale(1.2).move_to(DOWN)
       self.play(Transform(ss,sss),run_time=2)

       # 2 equações, 2 incógnitas
       qt0 = TextMobject("2 equações, 2 incógnitas") 
       qt0.set_color(YELLOW).scale(1.0).move_to(3.5*DOWN)
       self.play(FadeIn(qt0))
       self.wait(2)

       self.play(FadeOut(qt0))
       self.wait()
       self.play(FadeOut(ss),FadeOut(s),FadeOut(tt))

       a0 = TextMobject("Melhores parâmetros").set_color(YELLOW_E).scale(1.5).move_to(3*UP)
       self.play(FadeIn(a0))
       self.wait(2)
       # solução

       # b = \frac{\sum(1/sigma_i^2)\sum(x_iy_i/sigma_i^2)-\sum(x_i/sigma_i^2)\sum(y_i/sigma_i^2)}{\sum(1/sigma_i^2)\sum(x_i^2/sigma_i^2)-(\sum(x_i/sigma_i^2))^2)}
      # a = \frac{\sum(y_i/sigma_i^2)-b\sum(x_i/sigma_i^2)}{\sum(1/sigma_i^2)}

       solb = TexMobject(r"b = \frac{\sum(1/\sigma_i^2)\sum(x_iy_i/\sigma_i^2)-\sum(x_i/\sigma_i^2)\sum(y_i/\sigma_i^2)}{\sum(1/\sigma_i^2)\sum(x_i^2/\sigma_i^2)-(\sum(x_i/\sigma_i^2))^2)}").scale(1.2).move_to(0.5*UP) 
       sola = TexMobject(r"a = \frac{\sum(y_i/\sigma_i^2)-b\sum(x_i/\sigma_i^2)}{\sum(1/\sigma_i^2)}").scale(1.2).move_to(2*DOWN) 
       self.play(FadeIn(solb),FadeIn(sola))
       self.wait(3)
       self.play(FadeOut(a0))

       self.play(ApplyMethod(solb.scale,0.4))
       self.play(ApplyMethod(solb.move_to,3.0*RIGHT+2.5*UP))
       self.play(ApplyMethod(sola.scale,0.4))
       self.play(ApplyMethod(sola.move_to,3.0*RIGHT+1*UP))

       self.wait(2)

       tt0 = TextMobject("Usando a notação").set_color(WHITE).scale(1.0).move_to(2.5*UP+4*LEFT)
       self.play(FadeIn(tt0))
       self.wait(2)
 
       # [f] = \sum\frac{f_i}{\sigma_i^2}
       # <f> = frac{[f]}{[1]}

       not1=TexMobject(r"[f] = \sum\frac{f_i}{\sigma_i^2}").set_color(WHITE).scale(1.0).move_to(4*LEFT)
       not2=TexMobject(r"<f> = \frac{[f]}{[1]}").set_color(WHITE).scale(1.0).move_to(4*LEFT+2*DOWN)
       self.play(FadeIn(not1), FadeIn(not2))
       self.wait(2)
       self.play(FadeOut(not1), FadeOut(not2),FadeOut(tt0))
       
       notb=TexMobject(r"b = \frac{[1][xy]-[x][y]}{[1][x^2]-[x][x]}").scale(1.3).move_to(0.0*UP)
       nota=TexMobject(r"a = <y> - b<x>").scale(1.3).move_to(2*DOWN)
     
       self.wait()
       mmq = TextMobject("Método do Mínimos Quadrados").set_color(YELLOW_E).scale(1.2).move_to(3*UP)
       mmq1 = TextMobject("Caso linear: $y=a+bx$").set_color(YELLOW_E).scale(1.2).move_to(1.5*UP)
       self.play(Transform(solb,notb),Transform(sola,nota))
       self.wait(3)
       self.play(Write(mmq),Write(mmq1))
       self.wait(5)
       # b = \frac{[1][xy]-[x][y]}{[1][x^2]-[x][x]}
       # a = <y> - b<x>
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
       

