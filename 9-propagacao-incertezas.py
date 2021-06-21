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


from manimlib.imports import *
#import numpy as np
############################################
# Cena de abertura
############################################
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color(apatita)

      tt1=TextMobject("Propagação")
      tt2=TextMobject("de incertezas")
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
class metodo(Scene):
      def construct(self): 
       tt0 = TextMobject("Uma grandeza física $w$ geralmente")
       tt1 = TextMobject("é função de outras grandezas $x$, $y$, $z$, ...")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.5).shift(2*UP)

       self.play(FadeIn(tt))
       self.wait(2)
       
       f0 = TexMobject(r"w=f(x,y,z,...)")
       f0.set_color(YELLOW).scale(1.5).shift(0*UP)
       self.play(FadeIn(f0))
       self.wait(2)

       f1 = TexMobject(r"P=mg")
       f1.set_color(YELLOW).scale(1.7).shift(2*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       self.play(FadeOut(f1))

       f1 = TexMobject(r"\displaystyle \rho=\frac{m}{V}")
       f1.set_color(YELLOW).scale(1.7).shift(2*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       self.play(FadeOut(f1))

       f1 = TexMobject(r"\displaystyle R=\frac{V}{I}")
       f1.set_color(YELLOW).scale(1.7).shift(2*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       self.play(FadeOut(f1))

       f1 = TexMobject(r"v= v_0+at")
       f1.set_color(YELLOW).scale(1.7).shift(2*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       self.play(FadeOut(f1))

       f1 = TexMobject(r"\displaystyle P=\frac{nRT}{V}")
       f1.set_color(YELLOW).scale(1.7).shift(2*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       self.play(FadeOut(f1))

       f1 = TexMobject(r"\displaystyle G=\frac{Fd^2}{m_1 m_2}")
       f1.set_color(YELLOW).scale(1.7).shift(2*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       self.play(FadeOut(f1))

       self.play(FadeOut(tt),FadeOut(f0))
       self.wait(2)
   
       
       tt0 = TextMobject("Se cada grandeza $x$, $y$, $z$, ...")
       tt1 = TextMobject("tiver uma incerteza padrão $\sigma_x$, $\sigma_y$, $\sigma_z$, ...")
       tt2 = TextMobject("e essas incertezas")
       tt3 = TextMobject(" forem completamente independentes, ")
       tt = VGroup(tt0,tt1,tt2,tt3)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.5).shift(1.5*UP)

       self.play(FadeIn(tt))
       self.wait(2)
       self.play(FadeOut(tt))


       tt0 = TextMobject("então a incerteza padrão em $w$")
       tt1 = TextMobject("pode ser obtida,")
       tt2 = TextMobject(" em primeira aproximação, por")
       tt = VGroup(tt0,tt1,tt2)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.5).shift(2*UP)

       self.play(FadeIn(tt))
       self.wait(2)
       
       f1 = TexMobject(r"\displaystyle \sigma^2_w=\left(\frac{\partial w}{\partial x}\right)^2\sigma^2_x+\left(\frac{\partial w}{\partial y}\right)^2\sigma^2_y+\left(\frac{\partial w}{\partial z}\right)^2\sigma^2_z+...")
       f1.set_color(WHITE).scale(1.2).shift(1.5*DOWN)
       self.play(Write(f1))
       self.wait(4) 
       self.play(FadeOut(tt),FadeOut(f1))

       tt0 = TextMobject("Alguns casos:")
       tt0.set_color(YELLOW).scale(1.5).shift(2*UP)
       self.play(FadeIn(tt0))
       self.wait(2)

       f1 = TexMobject(r"\displaystyle w=x+y+z")
       f1.set_color(GREEN_SCREEN).scale(1.5).shift(1*UP)
       self.play(FadeIn(f1))
       self.wait(2)


       ft = TexMobject(r"\sigma^2_w", #0
                       " = ", #1
                       r"\displaystyle \left(\frac{\partial w}{\partial x}\right)^2", #2
                       r"\sigma^2_x + ", #3
                       r"\displaystyle \left(\frac{\partial w}{\partial y}\right)^2", #4
                       r"\sigma^2_y + ", #5
                       r"\displaystyle \left(\frac{\partial w}{\partial z}\right)^2", #6
                       r"\sigma^2_z", #7
           ).set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.play(FadeIn(ft))
       self.wait(2)

       ftx = TexMobject(r"\displaystyle (1)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[1], RIGHT, buff = 1.0)
       fty = TexMobject(r"\displaystyle (1)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[3], RIGHT, buff = 1.0)
       ftz = TexMobject(r"\displaystyle (1)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[5], RIGHT, buff = 1.0)
       
   
       self.play(Transform(ft[2], ftx))
       self.play(Transform(ft[4], fty))
       self.play(Transform(ft[6], ftz))

       ftfinal = TexMobject(r"\sigma^2_w = \sigma^2_x + \sigma^2_y + \sigma^2_z").set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.wait()
       self.play(Transform(ft, ftfinal))
       self.wait(2)
        
       self.play(FadeOut(ft))
       self.play(FadeOut(f1))
       self.wait(2)
        
# soma

       f1 = TexMobject(r"\displaystyle w=ax+by+cz")
       f1.set_color(GREEN_SCREEN).scale(1.5).shift(1*UP)
       self.play(FadeIn(f1))
       self.wait(2)


       ft = TexMobject(r"\sigma^2_w", #0
                       " = ", #1
                       r"\displaystyle \left(\frac{\partial w}{\partial x}\right)^2", #2
                       r"\sigma^2_x + ", #3
                       r"\displaystyle \left(\frac{\partial w}{\partial y}\right)^2", #4
                       r"\sigma^2_y + ", #5
                       r"\displaystyle \left(\frac{\partial w}{\partial z}\right)^2", #6
                       r"\sigma^2_z", #7
           ).set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.play(FadeIn(ft))
       self.wait(2)

       ftx = TexMobject(r"\displaystyle (a)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[1], RIGHT, buff = 1.0)
       fty = TexMobject(r"\displaystyle (b)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[3], RIGHT, buff = 1.0)
       ftz = TexMobject(r"\displaystyle (c)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[5], RIGHT, buff = 1.0)
       
   
       self.play(Transform(ft[2], ftx))
       self.play(Transform(ft[4], fty))
       self.play(Transform(ft[6], ftz))

       ftfinal = TexMobject(r"\sigma^2_w = a^2\sigma^2_x + b^2\sigma^2_y + c^2\sigma^2_z").set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.wait()
       self.play(Transform(ft, ftfinal))
       self.wait(2)
        

       self.play(FadeOut(ft))
       self.play(FadeOut(f1))
       self.wait(2)

# multiplicacao

       f1 = TexMobject(r"\displaystyle w=xyz")
       f1.set_color(GREEN_SCREEN).scale(1.5).shift(1*UP)
       self.play(FadeIn(f1))
       self.wait(2)


       ft = TexMobject(r"\sigma^2_w", #0
                       " = ", #1
                       r"\displaystyle \left(\frac{\partial w}{\partial x}\right)^2", #2
                       r"\sigma^2_x + ", #3
                       r"\displaystyle \left(\frac{\partial w}{\partial y}\right)^2", #4
                       r"\sigma^2_y + ", #5
                       r"\displaystyle \left(\frac{\partial w}{\partial z}\right)^2", #6
                       r"\sigma^2_z", #7
           ).set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.play(FadeIn(ft))
       self.wait(2)

       ftx = TexMobject(r"\displaystyle (yz)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[1], RIGHT, buff = 1.0)
       fty = TexMobject(r"\displaystyle (xz)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[3], RIGHT, buff = 1.0)
       ftz = TexMobject(r"\displaystyle (xy)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[5], RIGHT, buff = 1.0)
       
   
       self.play(Transform(ft[2], ftx))
       self.play(Transform(ft[4], fty))
       self.play(Transform(ft[6], ftz))

       ftfinal1 = TexMobject(r"\displaystyle \frac{\sigma^2_w}{(xyz)^2} = (yz)^2\frac{\sigma^2_x}{(xyz)^2} + (xz)^2\frac{\sigma^2_y}{(xyz)^2} + (xy)^2\frac{\sigma^2_z}{(xyz)^2}").set_color(WHITE).scale(1.2).shift(1*DOWN)
       ftfinal2 = TexMobject(r"\displaystyle \frac{\sigma^2_w}{w^2} = \frac{\sigma^2_x}{x^2} + \frac{\sigma^2_y}{y^2} + \frac{\sigma^2_z}{z^2}").set_color(WHITE).scale(1.2).shift(1*DOWN)
       ftfinal = TexMobject(r"\displaystyle \left(\frac{\sigma_w}{w}\right)^2 = \left(\frac{\sigma_x}{x}\right)^2 + \left(\frac{\sigma_y}{y}\right)^2 + \left(\frac{\sigma_z}{z}\right)^2").set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.wait()
       self.play(Transform(ft, ftfinal1))
       self.wait(2)
       self.play(Transform(ft, ftfinal2))
       self.wait(2)
       self.play(Transform(ft, ftfinal))
       self.wait(2) 

       self.play(FadeOut(ft))
       self.play(FadeOut(f1))

       self.wait(2)
       
# potencia

       f1 = TexMobject(r"\displaystyle w=x^py^qz^r")
       f1.set_color(GREEN_SCREEN).scale(1.5).shift(1*UP)
       self.play(FadeIn(f1))
       self.wait(2)


       ft = TexMobject(r"\sigma^2_w", #0
                       " = ", #1
                       r"\displaystyle \left(\frac{\partial w}{\partial x}\right)^2", #2
                       r"\sigma^2_x + ", #3
                       r"\displaystyle \left(\frac{\partial w}{\partial y}\right)^2", #4
                       r"\sigma^2_y + ", #5
                       r"\displaystyle \left(\frac{\partial w}{\partial z}\right)^2", #6
                       r"\sigma^2_z", #7
           ).set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.play(FadeIn(ft))
       self.wait(2)

       ftx = TexMobject(r"\displaystyle (px^{p-1}y^qz^r)^2").set_color(GREEN_SCREEN).scale(0.8).next_to(ft[1], RIGHT, buff = 0.1)
       fty = TexMobject(r"\displaystyle (qx^py^{q-1}z^r)^2").set_color(GREEN_SCREEN).scale(0.8).next_to(ft[3], RIGHT, buff = 0.1)
       ftz = TexMobject(r"\displaystyle (rx^py^qz^{r-1})^2").set_color(GREEN_SCREEN).scale(0.8).next_to(ft[5], RIGHT, buff = 0.1)
       
   
       self.play(Transform(ft[2], ftx))
       self.play(Transform(ft[4], fty))
       self.play(Transform(ft[6], ftz))

       ftfinal1 = TexMobject(r"\displaystyle \frac{\sigma^2_w}{(x^py^qz^r)^2} = (px^{p-1}y^qz^r)^2\frac{\sigma^2_x}{(x^py^qz^r)^2} + (qx^py^{q-1}z^r)^2\frac{\sigma^2_y}{(x^py^qz^r)^2} + (rx^py^qz^{r-1})^2\frac{\sigma^2_z}{(x^py^qz^r)^2}").set_color(WHITE).scale(0.7).shift(1*DOWN)
       ftfinal2 = TexMobject(r"\displaystyle \frac{\sigma^2_w}{w^2} = \frac{p^2\sigma^2_x}{x^2} + \frac{q^2\sigma^2_y}{y^2} + \frac{r^2\sigma^2_z}{z^2}").set_color(WHITE).scale(1.2).shift(1*DOWN)
       ftfinal = TexMobject(r"\displaystyle \left(\frac{\sigma_w}{w}\right)^2 = \left(p\frac{\sigma_x}{x}\right)^2 + \left(q\frac{\sigma_y}{y}\right)^2 + \left(r\frac{\sigma_z}{z}\right)^2").set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.wait()
       self.play(Transform(ft, ftfinal1))
       self.wait(4)
       self.play(Transform(ft, ftfinal2))
       self.wait(2)
       self.play(Transform(ft, ftfinal))
       self.wait(3) 

       self.play(FadeOut(ft))
       self.play(FadeOut(f1),FadeOut(tt0))
       self.wait(2) 

# exemplo Volume de um cilindro
       tt0 = TextMobject("Como exemplo, vamos obter")
       tt1 = TextMobject("a incerteza padrão $\sigma_V$")
       tt2 = TextMobject("associada ao volume de um cilindro")
       tt3 = TextMobject("de comprimento $L$ e raio $R$")
       tt = VGroup(tt0,tt1,tt2,tt3)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.2).shift(2*UP)

       self.play(FadeIn(tt))
       self.wait(2)
       f1 = TexMobject(r"\displaystyle V=V(R,L)=\pi R^2L")
       f1.set_color(GREEN_SCREEN).scale(1.5).shift(0.8*DOWN)
       self.play(FadeIn(f1))
       self.wait() 
       

       ft = TexMobject(r"\sigma^2_V", #0
                       " = ", #1
                       r"\displaystyle \left(\frac{\partial V}{\partial R}\right)^2", #2
                       r"\sigma^2_R + ", #3
                       r"\displaystyle \left(\frac{\partial V}{\partial L}\right)^2", #4
                       r"\sigma^2_L"
           ).set_color(WHITE).scale(1.2).shift(2.5*DOWN)

       self.play(FadeIn(ft))
       self.wait(2)
       ftx = TexMobject(r"\displaystyle (\pi R^2)^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[1], RIGHT, buff = 0.5)
       fty = TexMobject(r"\displaystyle (2\pi R L )^2").set_color(GREEN_SCREEN).scale(1.2).next_to(ft[3], RIGHT, buff = 0.4)
       
   
       self.play(Transform(ft[2], ftx))
       self.play(Transform(ft[4], fty))
       
       
       ftfinal = TexMobject(r"\displaystyle \left(\frac{\sigma_V}{V}\right)^2 = \left(2\frac{\sigma_R}{R}\right)^2 + \left(\frac{\sigma_L}{L}\right)^2 ").set_color(WHITE).scale(1.2).shift(2.5*DOWN)

       self.wait(2)
       self.play(Transform(ft, ftfinal))
       self.wait(3)
       

       self.play(FadeOut(f1),FadeOut(tt))
       self.wait(2)


       tt0 = TextMobject("Se $L=(103\pm 2)$ cm e $R=(15.2\pm 0.5)$ cm")
       tt1 = TextMobject(" então")
       tt = VGroup(tt0,tt1)
       tt.arrange_submobjects(DOWN,buff=0.3)
       tt.set_color(YELLOW).scale(1.4).shift(1.5*UP)

       self.play(FadeIn(tt))
       self.wait(2)
       ftnum = TexMobject(r"\displaystyle \left(\frac{\sigma_V}{\pi\times (15.2)^2\times 103}\right)^2 = \left(2\frac{0.5}{15.2}\right)^2 + \left(\frac{2}{103}\right)^2 ").set_color(WHITE).scale(1.2).shift(1*DOWN)

       self.play(Transform(ft, ftnum))
       self.wait(2)
       self.play(FadeOut(ft))
       

       ftnum2 = TexMobject(r"\displaystyle \sigma_V^2 = 26297119.2 \hspace{0.1cm}\text{cm}^6").set_color(WHITE).scale(1.5).shift(1*DOWN)

       ftnum3 = TexMobject(r"\displaystyle \sigma_V \simeq 5130 \hspace{0.1cm}\text{cm}^3").set_color(WHITE).scale(1.5).shift(1*DOWN)
       self.wait()
       self.play(FadeIn(ftnum2))
       self.wait(2)

       self.play(Transform(ftnum2, ftnum3))

       self.wait(2)
       self.play(FadeOut(ftnum2),FadeOut(tt))
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
