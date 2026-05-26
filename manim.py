from manim import *
from manim_chemistry import *

class revo(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        #图片组
        init = ImageMobject("scr/init.jpg")
        init.scale_to_fit_height(config.frame_height)
        #文本组
        text1 = Text("生酮饮食\n是健康陷阱？", font_size=60, color=BLUE_E, font="Microsoft YaHei")
        text1.center()
        

        #化学式组
        glucose = GraphMolecule.molecule_from_pubchem(
            name="glucose",          
            ignore_hydrogens=True,  # 显示氢原子（默认True会隐藏H）
            label=True,              # 显示原子标签
        )
        glucose.next_to(init,RIGHT*18.0)
        # 生成甘油分子

        glycerol = GraphMolecule.molecule_from_pubchem(
            name="glycerol",          # PubChem 中的化合物名称
            ignore_hydrogens=True,   # 是否忽略氢原子 (True: 不显示H, False: 显示H)
            label=True,              # 是否显示原子标签
        )
        glycerol.next_to(glucose,RIGHT*18.0)

        fatty_acid = GraphMolecule.molecule_from_pubchem(
            name="stearic acid",      # 替换为需要的脂肪酸名称，如 "palmitic acid" 或 "oleic acid"
            ignore_hydrogens=True,
            label=True,
        )
        fatty_acid.next_to(glycerol,RIGHT*18.0)

        beta = GraphMolecule.molecule_from_pubchem(
            name="beta-Hydroxybutyric acid", 
            label=True,
            ignore_hydrogens=True
        )
        beta.next_to(fatty_acid,RIGHT*18.0)

        Acetoacetic = GraphMolecule.molecule_from_pubchem(
            name="Acetoacetic acid",  
            label=True,
            ignore_hydrogens=True
        )
        Acetoacetic.next_to(beta,RIGHT*18.0)

        Acetone = GraphMolecule.molecule_from_pubchem(
            name="Acetone",  
            label=True,
            ignore_hydrogens=True
        )
        Acetone.next_to(Acetoacetic,RIGHT*18.0)

        group = VGroup(glucose,glycerol,fatty_acid,beta,Acetoacetic,Acetone)

        text2 = Text("原理",font_size=100, color=RED_C, font="Microsoft YaHei",)
        text2.next_to(Acetone,RIGHT*18.0)

        #动画组
        self.add(text2,group)
        self.add(init)
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
        text1 = Text("生酮饮食", font_size=45, color=BLACK, font="Microsoft YaHei")
        text2 = Text("传统饮食", font_size=45, color=BLACK, font="Microsoft YaHei")
        

        rect1 = Rectangle(width=1.0, height=6.0, fill_color=BLUE_D, fill_opacity=0.9)  # 改为 BLUE_D
        rect2 = Rectangle(width=1.0, height=1.0, fill_color=GREEN_D, fill_opacity=0.9)  # 改为 GREEN_D
        rect3 = Rectangle(width=1.0, height=2.5, fill_color=RED_D, fill_opacity=0.9)    # 改为 RED_D

        for rect in [rect1, rect2, rect3]:
            rect.move_to(ORIGIN, aligned_edge=DOWN).shift(DOWN * 1.5)

        # 并排排列（间隔一定距离）
        rect1.shift(LEFT * 2.5)  # 左边
        # rect2 保持在中间 (原点)
        rect3.shift(RIGHT * 2.5)  # 右边

        # 添加数值标签 - 添加 color=BLACK
        label1 = Text("高脂肪", font_size=44, color=BLACK).next_to(rect1, DOWN)
        label2 = Text("低碳水", font_size=44, color=BLACK).next_to(rect2, DOWN)
        label3 = Text("适量蛋白", font_size=44, color=BLACK).next_to(rect3, DOWN)

        # 创建辅助线（显示底部对齐）- 改为 GRAY
        bottom_line = Line(LEFT*4, RIGHT*4, color=GRAY, stroke_width=2)
        bottom_line.move_to(ORIGIN, aligned_edge=DOWN)
        bottom_line.shift(DOWN * 1.5)
        text1.next_to(bottom_line, DOWN*6.0)
        text2.next_to(bottom_line, DOWN*6.0)

        rect1_new = Rectangle(width=1.0, height=1.0, fill_color=BLUE_D, fill_opacity=0.9)  # 改为 BLUE_D
        rect2_new = Rectangle(width=1.0, height=6.0, fill_color=GREEN_D, fill_opacity=0.9)  # 改为 GREEN_D
        rect3_new = Rectangle(width=1.0, height=3.0, fill_color=RED_D, fill_opacity=0.9)    # 改为 RED_D

        for rect in [rect1_new, rect2_new, rect3_new]:
            rect.move_to(ORIGIN, aligned_edge=DOWN).shift(DOWN * 1.5)

        rect1_new.shift(LEFT * 2.5)
        rect3_new.shift(RIGHT * 2.5)

        # 第二组标签也添加 color=BLACK
        label1_new = Text("低脂肪", font_size=44, color=BLACK).next_to(rect1_new, DOWN)
        label2_new = Text("高碳水", font_size=44, color=BLACK).next_to(rect2_new, DOWN)
        label3_new = Text("丰富蛋白", font_size=44, color=BLACK).next_to(rect3_new, DOWN)

        r = RoundedRectangle(corner_radius=0.5, height=2.0, width=4.0,fill_color=GREEN, fill_opacity=0.3)

        # 播放动画 - 这部分保持不变
        self.play(Create(bottom_line))  # 添加参考线
        self.play(Write(text1))
        self.play(GrowFromEdge(rect1, DOWN), run_time=0.5)
        self.play(Write(label1))
        self.play(GrowFromEdge(rect2, DOWN), run_time=0.5)
        self.play(Write(label2))
        self.play(GrowFromEdge(rect3, DOWN), run_time=0.5)
        self.play(Write(label3))
        self.play(
            Transform(text1, text2),
            Transform(rect1, rect1_new),
            Transform(rect2, rect2_new),
            Transform(rect3, rect3_new),
            Transform(label1, label1_new),
            Transform(label2, label2_new),
            Transform(label3, label3_new),
            run_time=2
        )
        self.wait(1.0)
        self.play(FadeOut(bottom_line), FadeOut(rect1), FadeOut(rect3), 
        FadeOut(label1), FadeOut(label2), FadeOut(label3),FadeOut(text1),
        Transform(rect2, r),label2_new.animate.move_to(ORIGIN))
        self.wait(1.5)
        self.play(FadeOut(rect2),FadeOut(label2_new))


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
        text3 = Text("乙酰CoA", font_size=50,color=BLACK)
        text3.next_to(arrow2, DOWN*1.5)

        arrow3 = Arrow(1 * UP, 2* DOWN,color=BLACK)
        arrow3.next_to(text3, DOWN*1.5)
        p3 = Text("三羧酸循环\n电子传递链", font_size=40,color=BLACK)
        p3.next_to(arrow3, RIGHT*1.5)
        text4 = Text("大量ATP", font_size=50,color=BLACK)
        text4.next_to(arrow3, DOWN*1.5)

        arrow4 = Arrow(1 * UP, 2* DOWN,color=BLACK)
        arrow4.next_to(text4, DOWN*1.5)
        p4 = Text("供能", font_size=50,color=BLACK)
        p4.next_to(arrow4, RIGHT*1.5)
        svg = SVGMobject("C:/Users/zbx/Downloads/brain.svg") 
        svg.next_to(arrow4,DOWN*4.0)
        svg.scale(1.5)



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
        self.play(self.camera.frame.animate.move_to(svg),
                    AnimationGroup(
                    GrowArrow(arrow4),
                    FadeIn(p4,shift=LEFT),
                    Create(svg),
                    lag_ratio=0.25,  # 控制每个动画之间的间隔比例
                ),
                run_time=3.0
                )
        
        title =Text("思路?", font_size=60,color=WHITE,line_spacing=0.5)
        title.move_to(svg)
        black_screen = ScreenRectangle(
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).stretch_to_fit_height(config.frame_height+1.0) \
         。stretch_to_fit_width(config.frame_width) \
         。move_to(UP * (config.frame_height+1.0 ))  # 初始在上方
        self.play(black_screen.animate.move_to(svg),run_time=3.0,rate_func=rate_functions.ease_out_quad)
        self.play(Write(title))
        self.wait(1.5)
        self.play(FadeOut(title))


from manim import *
from manim_chemistry import *

class revo3(MovingCameraScene):
    def construct(self):

        text1 = Text("极低碳水",font_size=60)
        text2 = Text("葡萄糖不足",font_size=60).next_to(text1,RIGHT).shift(RIGHT*10)
        text3 = Text("寻找替代能源",font_size=60).next_to(text2,RIGHT).shift(RIGHT*10)
        text4 = Text("分解脂肪",font_size=60).next_to(text3,RIGHT).shift(RIGHT*10)
        self.add(text2,text3,text4)
        self.play(Write(text1))
        self.play(self.camera.frame.animate.move_to(text2),run_time=2.0)
        self.play(self.camera.frame.animate.move_to(text3),run_time=2.0)
        self.play(self.camera.frame.animate.move_to(text4),run_time=2.0)

        line = Line(LEFT*1 ,RIGHT*3)
        line.next_to(text4,RIGHT)

        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        bezier1 = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        bezier1.next_to(text4,RIGHT).shift(DOWN*1)

        p1n = np.array([-3, -1, 0])
        p1bn = p1n + [1, 0, 0]
        p2n = np.array([3, 1, 0])
        p2bn = p2n - [1, 0, 0]
        bezier2 = CubicBezier(p1bn, p1bn + 3 * RIGHT, p2bn - 3 * RIGHT, p2bn)
        bezier2.next_to(text4,RIGHT).shift(UP*1)

        title1 = Text("脂肪动员",font_size=60)
        title2 = Text("肝脏加工",font_size=60)
        title3 = Text("酮体供能",font_size=60)
        title1.next_to(bezier2,RIGHT*1).shift(UP*1.0)
        title2.next_to(line,RIGHT*1)
        title3.next_to(bezier1,RIGHT*1).shift(DOWN*1.0)

        self.play(self.camera.frame.animate.move_to(title2),
                  Create(bezier1),Create(bezier2),Create(line),
                  AnimationGroup(
                      Write(title1),Write(title2),Write(title3),lag_ratio=0.25
                  ),
                  run_time=2.0)
        self.play(title1.animate.shift(UP*12),self.camera.frame.animate.shift(UP*10),run_time=2.0)
        self.play(FadeOut(title1))

class revo4(MovingCameraScene):
    def construct(self):
        text1 = Text("白色脂肪细胞",font_size=39,color=BLACK)
        r = RoundedRectangle(corner_radius=0.5, height=6.5, width=7.0,fill_color=ManimColor("#F5E6A3"), fill_opacity=0.9)
        text1.next_to(r, DOWN, buff=0.1).shift(UP*1.0)
        cell = VGroup(r,text1)
        self.play(FadeIn(cell))
        semicircle = Arc(angle=PI, radius=0.7, start_angle=PI,fill_color=ManimColor("#DB6440"),fill_opacity=0.9,stroke_width=0).shift(UP*5.0)
        p1 = Text("脂解激素", font_size=50,color=WHITE)
        p1.next_to(semicircle, UP)
        h = Group(p1,semicircle)
        arrow = Arrow(UP*1.0, DOWN*3.0,color=BLACK).next_to(r,UP).shift(DOWN*3.5)
        gysz = Text("甘油\n三脂", font_size=40,color=BLACK)
        arrow1 = Arrow(LEFT*2.0, RIGHT*1.0,color=BLACK)
        gysz.next_to(arrow1,LEFT)
        arrow2 = CurvedArrow(start_point=LEFT*1.5, end_point=DOWN*1, angle=-PI/3,color=BLACK)
        self.play(FadeIn(h))
        self.play(h.animate.next_to(r,UP),run_time=1.0)
        self.play(GrowArrow(arrow))
        text2 = Text(" 游离\n脂肪酸", font_size=40,color=BLACK)
        text3 = Text("甘油", font_size=40,color=BLACK)
        text2.next_to(arrow1,RIGHT)
        text3.next_to(arrow2,DOWN).shift(RIGHT*0.5)


        self.play(
            AnimationGroup(
                FadeIn(gysz),
                GrowArrow(arrow1),
                FadeIn(text2),
                Create(arrow2),
                FadeIn(text3),
                lag_ratio=0.25
            ))
        blood = Rectangle(height=100,width=2,color=RED,fill_color=RED,fill_opacity=0.7).next_to(r,RIGHT*8)

        self.add(blood)
        pro = Ellipse(width=1.8,height=3.0,color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        pro.move_to(blood.get_center())
        bloodname = Text("血管", font_size=40,color=WHITE).next_to(pro,DOWN*3.0)
        self.add(pro,bloodname)
        text2.set_z_index(2)
        self.play(self.camera.frame.animate.move_to(blood),text2.animate.move_to(pro.get_center()))
        self.wait(1.0)
        self.play(
            self.camera.frame.animate.shift(UP*20),
            text2.animate.shift(UP*20),
            pro.animate.shift(UP*20),
            run_time=2.0
            )

class revo5(MovingCameraScene):
    def construct(self):
        blood = Rectangle(height=100,width=2,color=RED,fill_color=RED,fill_opacity=0.7)
        pro = Ellipse(width=1.8,height=3.0,color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        text2 = Text(" 游离\n脂肪酸", font_size=40,color=BLACK).move_to(pro.get_center()).set_z_index(2)
        liver = Rectangle(height=40,width=4,color=WHITE,fill_color=ManimColor("#E6C4A8"),fill_opacity=1.0).next_to(blood,LEFT*12)
        self.add(blood,pro)
        self.add(text2)
        self.wait(1.0)
        text3 = Text(" 游离\n脂肪酸", font_size=30,color=BLACK).move_to(liver.get_center()).set_z_index(2)
        livername = Text("肝脏", font_size=40,color=BLACK).move_to(liver.get_center()).shift(DOWN*4.0).set_z_index(2)
        self.add(livername)
        self.add(liver)
        self.play(self.camera.frame.animate.move_to(liver),
                  text2.animate.move_to(liver.get_center()),
                  run_time=2.0)
        self.play(self.camera.frame.animate.scale(0.5),Transform(text2,text3),run_time=2.0)

class revo6(MovingCameraScene):
        def construct(self):
            liver = Rectangle(height=40,width=10,color=WHITE,fill_color=ManimColor("#E6C4A8"),fill_opacity=1.0)
            text2 = Text(" 游离\n脂肪酸", font_size=60,color=BLACK)
            self.add(liver,text2)

            arrow1 = Arrow(DOWN*1.0, UP*2.0,color=BLACK).next_to(text2,UP*1.0)
            p1 = Text("活化", font_size=45,color=BLACK).next_to(arrow1,LEFT)
            text4   = Text("脂肪酰CoA", font_size=60,color=BLACK).next_to(arrow1,UP)

            arrow2 = Arrow(DOWN*1.0, UP*2.0,color=BLACK).next_to(text4,UP*1.0)
            p2 = Text("Beta氧化", font_size=45,color=BLACK).next_to(arrow2,LEFT)
            text5   = Text("乙酰CoA", font_size=60,color=BLACK).next_to(arrow2,UP)

            arrow3 = Arrow(DOWN*1.0, UP*2.0,color=BLACK).next_to(text5,UP*1.0)
            p3 = Text("分解", font_size=45,color=BLACK).next_to(arrow3,LEFT)
            text6   = Text("酮体", font_size=60,color=ManimColor("#000000")).next_to(arrow3,UP).set_z_index(2)
            self.play(self.camera.frame.animate.move_to(text6),
                      AnimationGroup(
                        GrowArrow(arrow1),
                        FadeIn(p1,shift=RIGHT),
                        FadeIn(text4),
                        GrowArrow(arrow2),
                        FadeIn(p2,shift=RIGHT),
                        FadeIn(text5),
                        GrowArrow(arrow3),
                        FadeIn(p3,shift=RIGHT),
                        FadeIn(text6),
                        lag_ratio=0.25
                      ),
                      run_time=6.0)
            
            blood = Rectangle(height=100,width=2,color=RED,fill_color=RED,fill_opacity=0.7).shift(RIGHT*12)
            self.add(blood)
            self.play(self.camera.frame.animate.shift(RIGHT*12),
                      text6.animate.shift(RIGHT*12),
                      run_time=2.0)
            


class revo7(MovingCameraScene):       
     def construct(self):
            blood = Rectangle(height=50,width=2,color=RED,fill_color=RED,fill_opacity=0.7)
            text6   = Text("酮体", font_size=60,color=ManimColor("#000000")).set_z_index(2)
            self.add(blood,text6)
            brain = Rectangle(height=50,width=50,color=WHITE,fill_color=ManimColor("#FFFFFF"),fill_opacity=1.0)
            brain.shift(RIGHT*30)
            self.add(brain)
            self.play(self.camera.frame.animate.shift(RIGHT*10),
                      text6.animate.shift(RIGHT*10),
                      run_time=2.0)
            
            arrow1 = Arrow(LEFT*1.0, RIGHT*2.0,color=BLACK).next_to(text6,RIGHT)  
            p1 = Text("分解", font_size=45,color=BLACK).next_to(arrow1,UP)
            text1  = Text("ATP", font_size=60,color=BLACK).next_to(arrow1,RIGHT)

            arrow2 = Arrow(LEFT*1.0, RIGHT*2.0,color=BLACK).next_to(text1,RIGHT*1.0)
            p2 = Text("供能", font_size=45,color=BLACK).next_to(arrow2,UP)
            svg = SVGMobject("C:/Users/zbx/Downloads/brain.svg").next_to(arrow2,RIGHT)

            self.play(self.camera.frame.animate.move_to(svg),
                      AnimationGroup(
                        GrowArrow(arrow1),
                        FadeIn(p1,shift=DOWN),
                        FadeIn(text1),
                        GrowArrow(arrow2),
                        FadeIn(p2,shift=DOWN),
                        FadeIn(svg),
                        lag_ratio=0.25
                      ),
                      run_time=4.0
            )
            text2 = Text("“酮症状态”", font_size=70,color=BLACK).next_to(svg,RIGHT).shift(RIGHT*8.0)
            self.add(text2)
            self.play(self.camera.frame.animate.move_to(text2),run_time=2.0)
            self.play(ShowPassingFlash(Underline(text2,color=BLACK)))
        
class revo8(MovingCameraScene):
     def construct(self):
          self.camera.background_color = WHITE
          text2 = Text("“酮症状态”", font_size=70,color=BLACK)
          self.add(text2)

          Acetone = GraphMolecule.molecule_from_pubchem(
                name="Acetone",
                label=True,
                ignore_hydrogens=True
            )
          Acetone.next_to(text2, LEFT*18.0)

          Acetoacetic = GraphMolecule.molecule_from_pubchem(
                name="Acetoacetic acid",
                label=True,
                ignore_hydrogens=True
            )
          Acetoacetic.next_to(Acetone, LEFT*18.0)

          beta = GraphMolecule.molecule_from_pubchem(
             name="beta-Hydroxybutyric acid",
                label=True,
                ignore_hydrogens=True
            )
          beta.next_to(Acetoacetic, LEFT*18.0)

          fatty_acid = GraphMolecule.molecule_from_pubchem(
                name="stearic acid",
                ignore_hydrogens=True,
                label=True,
            )
          fatty_acid.next_to(beta, LEFT*18.0)

          glycerol = GraphMolecule.molecule_from_pubchem(
                name="glycerol",
                ignore_hydrogens=True,
                label=True,
            )
          glycerol.next_to(fatty_acid, LEFT*18.0)

          glucose = GraphMolecule.molecule_from_pubchem(
                name="glucose",
                ignore_hydrogens=True,
                label=True,
            )
          glucose.next_to(glycerol, LEFT*18.0)

          group = VGroup(glucose,glycerol,fatty_acid,beta,Acetoacetic,Acetone)
          self.add(group)

          p1 = Text("丙酮（酮体）", font_size=45,color=BLACK).next_to(Acetone,DOWN*2)
          p2 = Text("乙酰乙酸（酮体）", font_size=45,color=BLACK).next_to(Acetoacetic,DOWN*2)
          p3 = Text("beta-羟丁酸（酮体）", font_size=45,color=BLACK).next_to(beta,DOWN*2)
          p4 = Text("硬脂酸（脂肪酸）", font_size=45,color=BLACK).next_to(fatty_acid,DOWN*2)
          p5 = Text("甘油", font_size=45,color=BLACK).next_to(glycerol,DOWN*2)
          p6 = Text("葡萄糖", font_size=45,color=BLACK).next_to(glucose,DOWN*2)
          te_group = VGroup(p1,p2,p3,p4,p5,p6)       
          self.add(te_group) 

          Title = Text("陷阱？", font_size=70,color=RED).next_to(glucose,LEFT*18)
          self.add(Title)

          self.play(self.camera.frame.animate.move_to(Title),run_time=6.0)

 


        

 













        
       





     
