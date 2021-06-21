#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim metodo-cientifico.py Fechamento -l

############################################
############################################

#
#Definição de Cores
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

      titulo=TextMobject("Precisão e Exatidão")
      titulo.scale(3.0)
      titulo.set_color(papoula)
         
      self.play(FadeIn(explora))
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(1.5)

############################################
# Cena intermediárias
############################################

class metodo(Scene):
    def construct(self):
      #criação dos "alvos"
      
      rectangle = Rectangle(height=7, width=6.7,color=YELLOW)

      valor_verdadeiro = Circle(radius=0.1,
                         color=apatita,
                         fill_color=apatita, 
                         fill_opacity=1
                         )
                      
      medida = Circle(radius=0.06,
                         color=papoula,
                         fill_color=papoula, 
                         fill_opacity=1
                         ) 
      medida.shift(0.5*RIGHT+0.8*UP) 
      reta_x = Line(1.5*LEFT,1.5*RIGHT, color=WHITE)
      reta_y = Line(1.5*UP,1.5*DOWN, color=WHITE)
      circ_1 = Circle(radius=0.4,color=WHITE) 
      circ_2 = Circle(radius=0.8,color=WHITE) 
      circ_3 = Circle(radius=1.2,color=WHITE) 
      #agrupa as partes para compor o alvo
      alvo = VGroup(reta_x,reta_y,circ_1,circ_2,circ_3)
      alvo.set_color(WHITE)
      
      #define os textos 
      
      texto_valor_verdadeiro = TextMobject("Valor verdadeiro")
      texto_desconhecido = TextMobject("(desconhecido)")
      texto_valor_verdadeiro.shift(0.3*UP)
      texto_desconhecido.shift(0.3*DOWN)
      verdadeiro = VGroup(texto_valor_verdadeiro,texto_desconhecido)
      verdadeiro.set_color(WHITE)
      verdadeiro.shift(3.5*RIGHT+2*DOWN)

      texto_1 = TextMobject("Conhecido só aproximadamente")
      texto_2 = TextMobject("devido a erros de medição")
      texto_1.shift(0.3*UP)
      texto_2.shift(0.3*DOWN)
      texto_3 = VGroup(texto_1,texto_2)
      texto_3.set_color(WHITE)
      texto_3.shift(3.5*RIGHT+2*DOWN)

      texto_grandeza1 = TextMobject("Valor da grandeza")
      texto_grandeza2 = TextMobject("física experimental")
      texto_grandeza3 = TextMobject("obtido a partir do")
      texto_grandeza4 = TextMobject("processo de medição")
      texto_grandeza1.shift(0.9*UP)
      texto_grandeza2.shift(0.3*UP)
      texto_grandeza3.shift(0.3*DOWN)
      texto_grandeza4.shift(0.9*DOWN)
      texto_grandeza = VGroup(texto_grandeza1,texto_grandeza2,texto_grandeza3,texto_grandeza4)
      texto_grandeza.set_color(WHITE)
      texto_grandeza.shift(3.5*RIGHT+2*UP)
     
      #########
      # Início da animação
      # definição do centro do alvo como sendo o valor verdadeiro
      # de uma grandeza 
      self.play(FadeIn(valor_verdadeiro))
      self.wait(1)
      
      
      arrow1 = Arrow(alvo.get_center(),verdadeiro.get_corner(UP+LEFT))
      self.play(GrowArrow(arrow1))


      self.play(FadeIn(verdadeiro))
      self.wait(1)
      self.play(FadeOut(verdadeiro))
      self.wait(1)
      self.play(FadeIn(alvo),FadeIn(texto_3))
      self.wait(1)
      self.play(FadeOut(texto_3),FadeOut(arrow1))
      self.wait(1)

      
      # um "tiro" aparece indicando uma medição realizada
      self.play(FadeIn(medida))
      self.wait()
      arrow2 = Arrow(medida.get_center(),texto_grandeza.get_corner(DOWN+LEFT)+UP)

      self.play(FadeIn(texto_grandeza),GrowArrow(arrow2))
      self.wait(2.5)
      
      self.play(FadeOut(medida),FadeOut(texto_grandeza),FadeOut(arrow2))
      self.wait()
  
      texto_med1 = TextMobject("Conjunto de medições")
      texto_med2 = TextMobject("nas mesmas condições")
      texto_med1.shift(0.3*UP)
      texto_med2.shift(0.3*DOWN)
      texto_med = VGroup(texto_med1,texto_med2)
      texto_med.set_color(WHITE)
      texto_med.shift(3*UP)

      self.play(FadeIn(texto_med))
      self.wait(2)
      self.play(FadeOut(texto_med))  
      
      # definição de círculos que representarão o conjunto de medições
    
      p1=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p2=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p3=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p4=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p5=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p6=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p7=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p8=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p9=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      p10=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      
      q1=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q2=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q3=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q4=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q5=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q6=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q7=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q8=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q9=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      q10=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      
      r1=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r2=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r3=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r4=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r5=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r6=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r7=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r8=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r9=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      r10=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      
      s1=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s2=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s3=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s4=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s5=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s6=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s7=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s8=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s9=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      s10=Circle(radius=0.06,color=papoula,fill_color=papoula,fill_opacity=1)
      
      p=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
      q=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
      r=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
      s=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
      
      # Casos possíveis envolvendo precisão e exatidão
      
      #1) preciso e exato
      p_e = TextMobject("Preciso e Exato")
      p_e.shift(3*UP)
      p_e.scale(1.5)
      p_e.set_color(YELLOW)

      p_e_copy = p_e.copy()
      p_e_copy.scale(0.5)
      p_e_copy.shift(-2.8*UP+5*LEFT)

      self.play(FadeIn(p_e),FadeIn(rectangle))
      # ajusta posição dos "tiros" em torno do centro (ponto (0,0))
      # e mostra na tela
      for i in p:
                        x1=0 + 0.1 * np.random.randn()
                        x2=0 + 0.1 * np.random.randn()                     
                        i.shift(x1*RIGHT+x2*UP)
                        self.add(i)
                        self.wait(0.2)

      alvo1_copy = alvo.copy()
      alvo1_copy.set_color(GREY)
      v1=valor_verdadeiro.copy()
      p1_copy=p1.copy()
      p2_copy=p2.copy()
      p3_copy=p3.copy()
      p4_copy=p4.copy()
      p5_copy=p5.copy()
      p6_copy=p6.copy()
      p7_copy=p7.copy()
      p8_copy=p8.copy()
      p9_copy=p9.copy()
      p10_copy=p10.copy()


      alvo1 = VGroup(v1,alvo1_copy,
                     p1_copy,p2_copy,p3_copy,
                     p4_copy,p5_copy,p6_copy,
                     p7_copy,p8_copy,p9_copy,
                     p10_copy)
    
      alvo1.shift(5*LEFT+2*UP)

      self.play(FadeOut(p_e),FadeOut(p1),
                FadeOut(p2),FadeOut(p3),
                FadeOut(p4),FadeOut(p5),
                FadeOut(p6),FadeOut(p7),
                FadeOut(p8),FadeOut(p9),
                FadeOut(p10),FadeIn(alvo1),
                FadeIn(p_e_copy))
      
      self.wait(2)

      

      #2) preciso e inexato
      p_ie = TextMobject("Preciso e Inexato")
      p_ie.shift(3*UP)
      p_ie.scale(1.5)
      p_ie.set_color(YELLOW)
      
      p_ie_copy = p_ie.copy()
      p_ie_copy.scale(0.5)
      p_ie_copy.shift(-6.5*UP+5*LEFT)

      self.play(FadeIn(p_ie))
      # ajusta posição dos "tiros" em torno de ponto (1,1)
      # e mostra na tela
      for i in q:
                        x1=1 + 0.1 * np.random.randn()
                        x2=1 + 0.1 * np.random.randn()                        
                        i.shift(x1*RIGHT+x2*UP)
                        self.add(i)
                        self.wait(0.2)

      alvo2_copy = alvo.copy()
      alvo2_copy.set_color(GREY)
      v2=valor_verdadeiro.copy()
      q1_copy=q1.copy()
      q2_copy=q2.copy()
      q3_copy=q3.copy()
      q4_copy=q4.copy()
      q5_copy=q5.copy()
      q6_copy=q6.copy()
      q7_copy=q7.copy()
      q8_copy=q8.copy()
      q9_copy=q9.copy()
      q10_copy=q10.copy()


      alvo2 = VGroup(v2,alvo2_copy,
                     q1_copy,q2_copy,
                     q3_copy,q4_copy,
                     q5_copy,q6_copy,
                     q7_copy,q8_copy,
                     q9_copy,q10_copy)
    
      alvo2.shift(5*LEFT-2*UP)

      self.play(FadeOut(p_ie),FadeOut(q1),
                FadeOut(q2),FadeOut(q3),
                FadeOut(q4),FadeOut(q5),
                FadeOut(q6),FadeOut(q7),
                FadeOut(q8),FadeOut(q9),
                FadeOut(q10),FadeIn(alvo2),
                FadeIn(p_ie_copy))

      self.wait(2)

      
      #3) impreciso e exato
      ip_e = TextMobject("Impreciso e Exato")
      ip_e.shift(3*UP)
      ip_e.scale(1.5)
      ip_e.set_color(YELLOW)

      ip_e_copy = ip_e.copy()
      ip_e_copy.scale(0.5)
      ip_e_copy.shift(-2.8*UP+5*RIGHT)
     
      self.play(FadeIn(ip_e))
      # ajusta posição dos "tiros" em torno de ponto (0.5,0) e com
      # maior dispersão e mostra na tela
      for i in r:
                        x1=0.5 + 0.6 * np.random.randn()
                        x2=0   + 0.6 * np.random.randn()                        
                        i.shift(x1*RIGHT+x2*UP)
                        self.add(i)
                        self.wait(0.2)

      alvo3_copy = alvo.copy()
      alvo3_copy.set_color(GREY)
      v3=valor_verdadeiro.copy()
      r1_copy=r1.copy()
      r2_copy=r2.copy()
      r3_copy=r3.copy()
      r4_copy=r4.copy()
      r5_copy=r5.copy()
      r6_copy=r6.copy()
      r7_copy=r7.copy()
      r8_copy=r8.copy()
      r9_copy=r9.copy()
      r10_copy=r10.copy()


      alvo3 = VGroup(v3,alvo3_copy,
                     r1_copy,r2_copy,
                     r3_copy,r4_copy,
                     r5_copy,r6_copy,
                     r7_copy,r8_copy,
                     r9_copy,r10_copy)
    
      alvo3.shift(5*RIGHT+2*UP)
  
      self.play(FadeOut(ip_e),FadeOut(r1),
                FadeOut(r2),FadeOut(r3),
                FadeOut(r4),FadeOut(r5),
                FadeOut(r6),FadeOut(r7),
                FadeOut(r8),FadeOut(r9),
                FadeOut(r10),FadeIn(alvo3),
                FadeIn(ip_e_copy))

      self.wait(2)
      
      #4) impreciso e inexato
      ip_ie = TextMobject("Impreciso e Inexato")
      ip_ie.shift(3*UP)
      ip_ie.scale(1.5)
      ip_ie.set_color(YELLOW)

      ip_ie_copy = ip_ie.copy()
      ip_ie_copy.scale(0.5)
      ip_ie_copy.shift(-6.5*UP+5*RIGHT)

      self.play(FadeIn(ip_ie))
      # ajusta posição dos "tiros" em torno de ponto (1.5,1.5) e com
      # maior dispersão e mostra na tela
      for i in s:
                        x1=1.5 + 0.6 * np.random.randn())
                        x2=1.5 + 0.6 * np.random.randn()                       
                        i.shift(x1*RIGHT+x2*UP)
                        self.add(i)
                        self.wait(0.2)

      alvo4_copy = alvo.copy()
      alvo4_copy.set_color(GREY)
      v4=valor_verdadeiro.copy()
      s1_copy=s1.copy()
      s2_copy=s2.copy()
      s3_copy=s3.copy()
      s4_copy=s4.copy()
      s5_copy=s5.copy()
      s6_copy=s6.copy()
      s7_copy=s7.copy()
      s8_copy=s8.copy()
      s9_copy=s9.copy()
      s10_copy=s10.copy()


      alvo4 = VGroup(v4,alvo4_copy,
                     s1_copy,s2_copy,
                     s3_copy,s4_copy,
                     s5_copy,s6_copy,
                     s7_copy,s8_copy,
                     s9_copy,s10_copy)
    
      alvo4.shift(5*RIGHT-2*UP)

      self.play(FadeOut(ip_ie),FadeOut(s1),
                FadeOut(s2),FadeOut(s3),
                FadeOut(s4),FadeOut(s5),
                FadeOut(s6),FadeOut(s7),
                FadeOut(s8),FadeOut(s9),
                FadeOut(s10),FadeIn(alvo4),
                FadeIn(ip_ie_copy))

      self.wait(2)

      self.play(FadeOut(alvo),FadeOut(valor_verdadeiro),FadeOut(rectangle))
      self.wait(2)
                        

      
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
