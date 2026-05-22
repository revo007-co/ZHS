from manim import *
from manim_chemistry import *

class revo(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        #图片组
        init = ImageMobject("scr/init.jpg")
        init.scale_to_fit_height(config.frame_height)
        p2 = ImageMobject("scr/p2.jpg")
        p2.move_to(RIGHT * 4)
        p3 = ImageMobject("scr/p3.jpg")
        p3.move_to(RIGHT * 34)
        p4 = ImageMobject("scr/p4.jpg")
        p4.move_to(RIGHT * 64)
        img_group = Group(p2,p3,p4)
        img_group.scale(0.5)

        

        #文本组
        text1 = Text("生酮饮食\n是健康陷阱？", font_size=60, color=BLUE_E, font="Microsoft YaHei")
        text1.center()
        text2 = Text("生化知识",font_size=100, color=RED_E, font="Microsoft YaHei",)
        text2.move_to(RIGHT * 94)

        #化学式组
        beta = GraphMolecule.molecule_from_pubchem(
            name="beta-Hydroxybutyric acid", 
            label=True,
            ignore_hydrogens=True
        )
        beta.move_to(RIGHT * 65)
        Acetoacetic = GraphMolecule.molecule_from_pubchem(
            name="Acetoacetic acid",  
            label=True,
            ignore_hydrogens=True
        )
        Acetoacetic.move_to(RIGHT * 75)
        Acetone = GraphMolecule.molecule_from_pubchem(
            name="Acetone",  
            label=True,
            ignore_hydrogens=True
        )
        Acetone.move_to(RIGHT * 85)

        #动画组
        self.add(img_group,text2)
        self.add(init)
        self.add(beta,Acetoacetic,Acetone)
        self.camera.frame.move_to(init.get_center())
        self.play(Write(text1), run_time=1.0)
        self.wait(0.6)
        self.play(self.camera.frame.animate.scale(1.5), run_time=0.8)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(text2),run_time=4.0)
        self.wait(0.3)
        self.play(self.camera.frame.animate.scale(0.7), run_time=0.8)
        self.wait(0.3)
        self.play(
            FadeOut(text2, shift=RIGHT),
            run_time=0.5
        )
class revo1(Scene):
    def construct(self):
        
        self.camera.background_color = WHITE

        # 原有代码修改如下：

        rect1 = Rectangle(width=1.0, height=6.0, fill_color=BLUE_D, fill_opacity=0.9)  # 改为 BLUE_D
        rect2 = Rectangle(width=1.0, height=1.0, fill_color=GREEN_D, fill_opacity=0.9)  # 改为 GREEN_D
        rect3 = Rectangle(width=1.0, height=2.5, fill_color=RED_D, fill_opacity=0.9)    # 改为 RED_D

        for rect in [rect1, rect2, rect3]:
            rect.move_to(ORIGIN, aligned_edge=DOWN).shift(DOWN * 1.5)

        # 并排排列（间隔一定距离）
        rect1.shift(LEFT * 2)  # 左边
        # rect2 保持在中间 (原点)
        rect3.shift(RIGHT * 2)  # 右边

        # 添加数值标签 - 添加 color=BLACK
        label1 = Text("高脂", font_size=44, color=BLACK).next_to(rect1, DOWN)
        label2 = Text("低糖", font_size=44, color=BLACK).next_to(rect2, DOWN)
        label3 = Text("适量蛋白", font_size=44, color=BLACK).next_to(rect3, DOWN)

        # 创建辅助线（显示底部对齐）- 改为 GRAY
        bottom_line = Line(LEFT*4, RIGHT*4, color=GRAY, stroke_width=2)
        bottom_line.move_to(ORIGIN, aligned_edge=DOWN)
        bottom_line.shift(DOWN * 1.5)

        rect1_new = Rectangle(width=1.0, height=1.0, fill_color=BLUE_D, fill_opacity=0.9)  # 改为 BLUE_D
        rect2_new = Rectangle(width=1.0, height=6.0, fill_color=GREEN_D, fill_opacity=0.9)  # 改为 GREEN_D
        rect3_new = Rectangle(width=1.0, height=3.0, fill_color=RED_D, fill_opacity=0.9)    # 改为 RED_D

        for rect in [rect1_new, rect2_new, rect3_new]:
            rect.move_to(ORIGIN, aligned_edge=DOWN).shift(DOWN * 1.5)

        rect1_new.shift(LEFT * 2)
        rect3_new.shift(RIGHT * 2)

        # 第二组标签也添加 color=BLACK
        label1_new = Text("低脂", font_size=44, color=BLACK).next_to(rect1_new, DOWN)
        label2_new = Text("高糖", font_size=44, color=BLACK).next_to(rect2_new, DOWN)
        label3_new = Text("丰富蛋白", font_size=44, color=BLACK).next_to(rect3_new, DOWN)

        # 播放动画 - 这部分保持不变
        self.play(Create(bottom_line))  # 添加参考线
        self.play(GrowFromEdge(rect1, DOWN), run_time=0.5)
        self.play(Write(label1))
        self.play(GrowFromEdge(rect2, DOWN), run_time=0.5)
        self.play(Write(label2))
        self.play(GrowFromEdge(rect3, DOWN), run_time=0.5)
        self.play(Write(label3))
        self.play(
            Transform(rect1, rect1_new),
            Transform(rect2, rect2_new),
            Transform(rect3, rect3_new),
            Transform(label1, label1_new),
            Transform(label2, label2_new),
            Transform(label3, label3_new),
            run_time=2
        )
        self.wait(1.0)
        self.play(FadeOut(bottom_line), FadeOut(rect1), FadeOut(rect2), FadeOut(rect3), 
        FadeOut(label1), FadeOut(label2), FadeOut(label3))

class revo2(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        glucose = GraphMolecule.molecule_from_pubchem(
            name="glucose",
            three_d=False,           # ← 确保2D结构
            ignore_hydrogens=False,  # 显示氢原子（默认True会隐藏H）
            label=True,              # 显示原子标签
            numeric_label=False      # 使用元素符号而非数字
        )
        formula = MathTex(r"\mathrm{C_6H_{12}O_6}", font_size=50,color=BLACK)
        text = Text("葡萄糖", font_size=50,color=BLACK)
     
        self.play(Write(glucose))
        self.play(glucose.animate.shift(UP * 3).scale(0.5))
        formula.next_to(glucose, DOWN)
        text.next_to(formula, DOWN)
        self.play(Write(formula),Write(text),run_time=0.7)

        arrow1 = Arrow(1 * UP, 2* DOWN,color=BLACK)
        arrow1.next_to(text, DOWN*1.5)
        p = Text("糖酵解", font_size=50,color=BLACK)
        p.next_to(arrow1, RIGHT*1.5)
        text2 = Text("丙酮酸", font_size=50,color=BLACK)
        text2.next_to(arrow1, DOWN*1.5)
        

        arrow2 = Arrow(1 * UP, 2* DOWN,color=BLACK)
        arrow2.next_to(text2, DOWN*1.5)
        p2 = Text("氧化脱羧", font_size=50,color=BLACK)
        p2.next_to(arrow2, RIGHT*1.5)
        text3 = Text("乙酰辅酶A", font_size=50,color=BLACK)
        text3.next_to(arrow2, DOWN*1.5)

        arrow3 = Arrow(1 * UP, 2* DOWN,color=BLACK)
        arrow3.next_to(text3, DOWN*1.5)
        p3 = Text("三羧酸循环\n电子传递链", font_size=40,color=BLACK)
        p3.next_to(arrow3, RIGHT*1.5)
        text4 = Text("大量ATP", font_size=50,color=BLACK)
        text4.next_to(arrow3, DOWN*1.5)


        self.play(
                self.camera.frame.animate.move_to(text4),
                AnimationGroup(
                GrowArrow(arrow1),
                Write(text2),
                FadeIn(p,shift=LEFT),
                GrowArrow(arrow2),
                Write(text3),
                FadeIn(p2,shift=LEFT),
                GrowArrow(arrow3),
                Write(text4),
                FadeIn(p3,shift=LEFT),
                lag_ratio=0.25,  # 控制每个动画之间的间隔比例
                ),
                run_time=4.0)
        self.play( FadeOut(text3),  FadeOut(p2), FadeOut(p3), FadeOut(arrow2), FadeOut(arrow3))
        self.play(self.camera.frame.animate.scale(0.7))
        self.play(FadeOut(text4,shift=UP),run_time=0.5)
        t=Text("提供能量", font_size=50,color=RED_E)
        t.move_to(text4)
        self.play(FadeIn(t,shift=DOWN),run_time=0.5)

class revo3(MovingCameraScene):

    def construct(self):
        radius = 2
        
        # 圆圈
        circle = Circle(radius=radius, color=BLUE)
        circle.move_to(ORIGIN)
        
        # 初始扇形（角度为 0）
        sector = Sector(
            radius=radius,
            angle=60*DEGREES,
            start_angle=0,
            color=YELLOW,
            fill_opacity=0.9
        )
        
        self.play(Create(circle))
        self.play(Create(sector))  # 先添加，虽然角度为0但可见
        
        self.wait(1)

        
       





     
