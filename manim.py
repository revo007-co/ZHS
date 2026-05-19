from manim import *

class revo(MovingCameraScene):
    def construct(self):
        img = ImageMobject("scr/init.jpg")
        img.scale_to_fit_height(config.frame_height)
        self.add(img)
        self.camera.frame.move_to(img.get_center())
        
        text = Text("生酮饮食\n是一场骗局？", font_size=60, color=BLUE_E, font="Microsoft YaHei")
        text.center()
        self.play(Write(text), run_time=1.0)
        self.wait(0.6)
        
        self.play(self.camera.frame.animate.scale(2.0), run_time=0.8)
        self.wait(0.3)
        
        # 一行显示，超出截断
        text2 = Text(
            "在回答此问题前， ",
            font_size=100, 
            color=WHITE, 
            font="Microsoft YaHei",
            
        )
        text2.move_to(RIGHT * 18)
       


        text3 = Text(
            "我将以最通俗易懂的方式，",
            font_size=100, 
            color=WHITE, 
            font="Microsoft YaHei",
            
        )
        text3.move_to(RIGHT * 32)
        

        text4 = Text(
            "为你讲解与此相关的",
            font_size=100, 
            color=WHITE, 
            font="Microsoft YaHei",
         
        )
        text4.move_to(RIGHT * 48)

        text5 = Text(
            "生化知识",
            font_size=100, 
            color=RED_E, 
            font="Microsoft YaHei",
        )
        text5.move_to(RIGHT * 59)

        text_group = VGroup(text2, text3, text4, text5)

        self.add(text_group)
        
        self.play(self.camera.frame.animate.move_to(text2))
        self.wait(0.1)
        self.play(self.camera.frame.animate.move_to(text3))
        self.wait(0.1)
        self.play(self.camera.frame.animate.move_to(text4))
        self.wait(0.1)
        self.play(self.camera.frame.animate.move_to(text5))

        self.wait(0.3)
        self.play(self.camera.frame.animate.scale(0.55), run_time=0.8)
        self.wait(0.3)
        self.play(
            FadeOut(text5, shift=RIGHT),
            run_time=0.5
        )
