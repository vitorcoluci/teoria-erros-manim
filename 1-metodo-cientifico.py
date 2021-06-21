#!/usr/bin/env python

############################################
############################################

# Animação produzida por Vitor R. Coluci/Faculdade de Tecnologia - UNICAMP
# 2020

#python3 -m manim metodo-cientifico.py Fechamento -l

############################################
############################################

#Definição de Cores

# Apatita (verde)   : código Hex "#43bfca"
# Papoula (laranja) : código Hex "#dc6a40"
apatita = "#43bfca"
papoula = "#dc6a40"


from manimlib.imports import *

############################################
# Cena de abertura
############################################
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color(apatita)

      titulo=TextMobject("Método Científico")
      titulo.scale(2.0)
      titulo.set_color(papoula)
         
      self.play(FadeIn(explora))
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(1.5)

############################################
# Cenas intermediárias
############################################

class metodo(Scene):
    def construct(self):
      #define caixas com os textos das partes do método científico
      caixa_fenomeno = Rectangle(height=1.5,      
                                 width=3,
                                 fill_color=RED, 
                                 fill_opacity=0.7
                                 ) 
      caixa_fenomeno.set_color(RED)
      legenda_fenomeno = TextMobject("Fenômeno")
      legenda_fenomeno.scale(1.0)
      legenda_fenomeno.set_color(WHITE)
      #########
      caixa_experimento = Rectangle(height=1.5,      
                                 width=3,
                                 fill_color=YELLOW_A, 
                                 fill_opacity=0.7
                                 ) 
      caixa_experimento.set_color(YELLOW_A)
      legenda_experimento = TextMobject("Experimento")
      legenda_experimento.scale(1.0)
      legenda_experimento.set_color(BLACK)
      #########
      caixa_medicoes = Rectangle(height=1.5,      
                                 width=2,
                                 fill_color=GREEN_SCREEN, 
                                 fill_opacity=0.7
                                 ) 
      caixa_medicoes.set_color(GREEN_SCREEN)
      legenda_medicoes = TextMobject("Medições")
      legenda_medicoes.scale(1.0)
      legenda_medicoes.set_color(BLACK)
      #########
      caixa_dados = Rectangle(height=1.5,      
                                 width=2,
                                 fill_color=BLUE_C, 
                                 fill_opacity=0.7
                                 ) 
      caixa_dados.set_color(BLUE_C)
      legenda_dados = TextMobject("Dados")
      legenda_dados.scale(1.0)
      legenda_dados.set_color(BLACK)
      #########
      caixa_leis = Rectangle(height=2,      
                                 width=3,
                                 fill_color=papoula, 
                                 fill_opacity=0.7
                                 ) 
      caixa_leis.set_color(papoula)
      legenda_leis1 = TextMobject("   Leis    ")
      legenda_leis1.shift(0.5*UP)
      legenda_leis2 = TextMobject("Científicas")
      legenda_leis2.shift(0.5*DOWN)
      leis_group=VGroup(legenda_leis1,legenda_leis2)
      leis_group.set_color(BLACK)
      #########
      caixa_modelo = Rectangle(height=1.5,      
                                 width=2.5,
                                 fill_color=PURPLE, 
                                 fill_opacity=0.7
                                 ) 
      caixa_modelo.set_color(PURPLE)
      legenda_modelo = TextMobject("Modelo")
      legenda_modelo.scale(1.0)
      legenda_modelo.set_color(WHITE)
      #########
      caixa_previsao = Rectangle(height=1.5,      
                                 width=3,
                                 fill_color=papoula, 
                                 fill_opacity=0.7
                                 ) 
      caixa_previsao.set_color(DARK_BROWN)
      legenda_previsao = TextMobject("Previsão")
      legenda_previsao.scale(1.0)
      legenda_previsao.set_color(WHITE)
      #########
      caixa_confronto = Rectangle(height=1.5,      
                                 width=3,
                                 fill_color=DARK_BLUE, 
                                 fill_opacity=0.7
                                 ) 
      caixa_confronto.set_color(DARK_BLUE)
      legenda_confronto = TextMobject("Confronto")
      legenda_confronto.scale(1.0)
      legenda_confronto.set_color(WHITE)
      #########
      #Aparecimemnto da caixa na tela de cada parte e
      # movimentação para o local da tela final
      
      #fenomeno
      self.play(FadeIn(caixa_fenomeno),FadeIn(legenda_fenomeno))
      self.wait()
      self.play(ApplyMethod(caixa_fenomeno.move_to,5.5*LEFT),
                ApplyMethod(legenda_fenomeno.move_to,5.5*LEFT)
                )
      fen1 = TextMobject("Ponto de partida")
      fen1.scale(1.5)
      fen1.shift(1.0*UP)
      fen2 = TextMobject(" e ")
      fen2.scale(1.5)
      fen3 = TextMobject("teste crucial")
      fen3.scale(1.5)
      fen3.shift(1*DOWN)
      fen4 = TextMobject("das leis naturais")
      fen4.scale(1.5)
      fen4.shift(2*DOWN)
      fenomeno_group=VGroup(fen1,fen2,fen3,fen4)
      fenomeno_group.set_color(WHITE)  
      
      self.play(FadeIn(fenomeno_group))
      self.wait(2)
      self.play(FadeOut(fenomeno_group))

      #experimento
      self.play(FadeIn(caixa_experimento),
                FadeIn(legenda_experimento))
      self.wait()
      self.play(ApplyMethod(caixa_experimento.move_to,5.5*LEFT+3*UP),
                ApplyMethod(legenda_experimento.move_to,5.5*LEFT+3*UP)
                )
      arrow1 = Arrow(caixa_fenomeno.get_corner(UP+LEFT)+1.5*RIGHT,caixa_experimento.get_corner(DOWN+LEFT)+1.5*RIGHT)
      self.play(GrowArrow(arrow1))
      
      exp1 = TextMobject("Reprodução do fenômeno")
      exp1.scale(1.5)
      exp1.shift(1.2*UP)
      exp2 = TextMobject("numa montagem")
      exp2.scale(1.5)
      exp3 = TextMobject("experimental")
      exp3.scale(1.5)
      exp3.shift(1.2*DOWN)
      exp_group=VGroup(exp1,exp2,exp3)
      exp_group.set_color(WHITE)  
      
      self.play(FadeIn(exp_group))
      self.wait(2)
      self.play(FadeOut(exp_group))

      #medicoes
      self.play(FadeIn(caixa_medicoes),
                FadeIn(legenda_medicoes))
      self.wait()
      self.play(ApplyMethod(caixa_medicoes.move_to,2*LEFT+3*UP),
                ApplyMethod(legenda_medicoes.move_to,2*LEFT+3*UP)
                )
      arrow2 = Arrow(caixa_experimento.get_corner(DOWN+RIGHT)+0.75*UP,caixa_medicoes.get_corner(DOWN+LEFT)+0.75*UP)
      self.play(GrowArrow(arrow2))
      
      med1 = TextMobject("Medições são realizadas")
      med1.scale(1.5)
      med1.shift(1.2*UP)
      med2 = TextMobject("durante")
      med2.scale(1.5)
      med3 = TextMobject("o experimento")
      med3.scale(1.5)
      med3.shift(1.2*DOWN)
      med_group=VGroup(med1,med2,med3)
      med_group.set_color(WHITE)  
      
      self.play(FadeIn(med_group))
      self.wait(2)
      self.play(FadeOut(med_group))

      #dados
      self.play(FadeIn(caixa_dados),
                FadeIn(legenda_dados))
      self.wait()
      self.play(ApplyMethod(caixa_dados.move_to,2*RIGHT+3*UP),
                ApplyMethod(legenda_dados.move_to,2*RIGHT+3*UP)
                )
      arrow3 = Arrow(caixa_medicoes.get_corner(DOWN+RIGHT)+0.75*UP,caixa_dados.get_corner(DOWN+LEFT)+0.75*UP)
      self.play(GrowArrow(arrow3))
      
      dad1 = TextMobject("Dados")
      dad1.scale(1.5)
      dad1.shift(1.2*UP)
      dad2 = TextMobject("são então")
      dad2.scale(1.5)
      dad3 = TextMobject("coletados")
      dad3.scale(1.5)
      dad3.shift(1.2*DOWN)
      dad_group=VGroup(dad1,dad2,dad3)
      dad_group.set_color(WHITE)  
      
      self.play(FadeIn(dad_group))
      self.wait(2)
      self.play(FadeOut(dad_group))

      #leis
      self.play(FadeIn(caixa_leis),
                FadeIn(leis_group))
      self.wait()
      self.play(ApplyMethod(caixa_leis.move_to,5.5*RIGHT+3*UP),
                ApplyMethod(leis_group.move_to,5.5*RIGHT+3*UP)
                )
      arrow4 = Arrow(caixa_dados.get_corner(DOWN+RIGHT)+0.75*UP,caixa_leis.get_corner(DOWN+LEFT)+UP)
      self.play(GrowArrow(arrow4))
      
      lei1 = TextMobject("Descrição matemática")
      lei1.scale(1.5)
      lei1.shift(1.2*UP)
      lei2 = TextMobject("do fenômeno.")
      lei2.scale(1.5)
      lei3 = TextMobject("Não é explicação!")
      lei3.scale(1.5)
      lei3.shift(1.2*DOWN)
      lei_group=VGroup(lei1,lei2,lei3)
      lei_group.set_color(WHITE)  
      
      self.play(FadeIn(lei_group))
      self.wait(2)
      self.play(FadeOut(lei_group))

      #modelo
      self.play(FadeIn(caixa_modelo),
                FadeIn(legenda_modelo))
      self.wait()
      self.play(ApplyMethod(caixa_modelo.move_to,3.5*LEFT+3*DOWN),
                ApplyMethod(legenda_modelo.move_to,3.5*LEFT+3*DOWN)
                )
      arrow5 = Arrow(caixa_fenomeno.get_corner(DOWN+RIGHT)+1.5*LEFT,caixa_modelo.get_corner(LEFT+UP)+1.5*RIGHT)
      self.play(GrowArrow(arrow5))
      
      mod1 = TextMobject("Busca da explicação")
      mod1.scale(1.5)
      mod1.shift(1.2*UP)
      mod2 = TextMobject("do fenômeno")
      mod2.scale(1.5)
      mod3 = TextMobject("e das leis científicas.")
      mod3.scale(1.5)
      mod3.shift(1.2*DOWN)
      mod_group=VGroup(mod1,mod2,mod3)
      mod_group.set_color(WHITE)  
      
      self.play(FadeIn(mod_group))
      self.wait(2)
      self.play(FadeOut(mod_group))

      #previsao
      self.play(FadeIn(caixa_previsao),
                FadeIn(legenda_previsao))
      self.wait()
      self.play(ApplyMethod(caixa_previsao.move_to,3.5*RIGHT+3*DOWN),
                ApplyMethod(legenda_previsao.move_to,3.5*RIGHT+3*DOWN)
                )
      arrow6 = Arrow(caixa_modelo.get_corner(DOWN+RIGHT)+0.75*UP,caixa_previsao.get_corner(DOWN+LEFT)+0.75*UP)
      self.play(GrowArrow(arrow6))
      
      prev1 = TextMobject("Previsões resultantes")
      prev1.scale(1.5)
      prev1.shift(1.2*UP)
      prev2 = TextMobject("do")
      prev2.scale(1.5)
      prev3 = TextMobject("modelo")
      prev3.scale(1.5)
      prev3.shift(1.2*DOWN)
      prev_group=VGroup(prev1,prev2,prev3)
      prev_group.set_color(WHITE)  
      
      self.play(FadeIn(prev_group))
      self.wait(2)
      self.play(FadeOut(prev_group))

      #confronto
      self.play(FadeIn(caixa_confronto),
                FadeIn(legenda_confronto))
      self.wait()
      self.play(ApplyMethod(caixa_confronto.move_to,5.5*RIGHT),
                ApplyMethod(legenda_confronto.move_to,5.5*RIGHT)
                )
      arrow7 = Arrow(caixa_previsao.get_corner(UP+LEFT)+1.5*RIGHT,caixa_confronto.get_corner(DOWN+LEFT)+1.5*RIGHT)
      self.play(GrowArrow(arrow7))

      arrow8 = Arrow(caixa_leis.get_corner(DOWN+LEFT)+1.5*RIGHT,caixa_confronto.get_corner(UP+LEFT)+1.5*RIGHT)
      self.play(GrowArrow(arrow8))
      
      conf1 = TextMobject("Comparam-se as previsões")
      conf1.scale(1.5)
      conf1.shift(1.2*UP)
      conf2 = TextMobject("do modelo com")
      conf2.scale(1.5)
      conf3 = TextMobject("as leis científicas")
      conf3.scale(1.5)
      conf3.shift(1.2*DOWN)
      conf_group=VGroup(conf1,conf2,conf3)
      conf_group.set_color(WHITE)  
      
      self.play(FadeIn(conf_group))
      self.wait(2)
      self.play(FadeOut(conf_group))

      #FINAL
      conf1 = TextMobject("Se a previsão não")
      conf1.scale(1.5)
      conf1.shift(1.2*UP)
      conf2 = TextMobject("estiver de acordo")
      conf2.scale(1.5)
      conf3 = TextMobject("com as leis científicas,")
      conf3.scale(1.5)
      conf3.shift(1.2*DOWN)
      conf_group=VGroup(conf1,conf2,conf3)
      conf_group.set_color(WHITE)  
      
      self.play(FadeIn(conf_group))
      self.wait(2)
      self.play(FadeOut(conf_group))

      conf1 = TextMobject("aprimora-se o modelo ")
      conf1.scale(1.5)
      conf1.shift(1.2*UP)
      conf2 = TextMobject("e realiza-se")
      conf2.scale(1.5)
      conf3 = TextMobject("o confronto novamente,")
      conf3.scale(1.5)
      conf3.shift(1.2*DOWN)
      conf_group=VGroup(conf1,conf2,conf3)
      conf_group.set_color(WHITE)  
      
      self.play(FadeIn(conf_group))
      self.wait(2)
      self.play(FadeOut(conf_group))
      
      conf1 = TextMobject("até se chegar na")
      conf1.scale(1.5)
      conf1.shift(1.2*UP)
      conf2 = TextMobject("concordância desejada")
      conf2.scale(1.5)
      conf3 = TextMobject("entre o modelo e a lei.")
      conf3.scale(1.5)
      conf3.shift(1.2*DOWN)
      conf_group=VGroup(conf1,conf2,conf3)
      conf_group.set_color(WHITE)  
      
      self.play(FadeIn(conf_group))
      self.wait(2)
      self.play(FadeOut(conf_group))
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
