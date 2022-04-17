# внешний вид приложения описывается в том (единственном) экземпляре класса App, 
# у которого вызывается run(). 
# программа с двумя экранами
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.
class ScrButton(Button): #создаем класс ScrButton он главный без него никак 
   def __init__(self, screen, direction='right', goal='main', **kwargs):
       super().__init__(**kwargs)
       self.screen = screen
       self.direction = direction
       self.goal = goal
   def on_press(self):
       self.screen.manager.transition.direction = self.direction
       self.screen.manager.current = self.goal
class MainScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
       hl = BoxLayout()
       txt = Label(text= 'Выбирите знак зодиака') 
 
       vl.add_widget(ScrButton(self, direction='left', goal='first', text="Овен")) #много кнопок
       vl.add_widget(ScrButton(self, direction='right', goal='second', text="Телец"))#много кнопок
       vl.add_widget(ScrButton(self, direction='down', goal='third', text="Близнецы"))#много кнопок
       vl.add_widget(ScrButton(self, direction='up', goal='fourth', text="Рак"))#много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='fifth', text="Лев")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='sixth', text="Дева")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='seventh', text="Весы")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='eighth', text="Скорпион")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='ninth', text="Стрелец")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='tenth', text="Козерог")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='eleventh', text="Водолей")) #много кнопок
       vl.add_widget(ScrButton(self, direction='left', goal='twelfth', text="Рыбы")) #много кнопок
       hl.add_widget(txt)#  вывод на экран 'Выбери экран'
       hl.add_widget(vl)
       self.add_widget(hl)
class FirstScr(Screen): # создаем 1 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Блум', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class SecondScr(Screen): # создаем 2 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Айси', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class ThirdScr(Screen):# создаем 3 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Флора', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class FourthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Лейла', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class fifthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Стелла', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class sixthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Фарагонда', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class seventhScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Текна', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class eighthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Дарси', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class ninthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Валтор', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class tenthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Сторми', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class eleventhScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Муза', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)
class twelfthScr(Screen):#делаем 4 экран
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})#параметры
       btn = Button(text= 'Кико', size_hint=(.5, 1), pos_hint={'left': 0}) # кнопка 'Выбор: 1' которая ничего не делает ;)
       btn_back = ScrButton(self, direction='right', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})#создание кнопки назад которая вернёт на гл экран
       vl.add_widget(btn)#добавляем в бокс
       vl.add_widget(btn_back)#добавляем в бокс
       self.add_widget(vl)      
class MyApp(App):
   def build(self):
       sm = ScreenManager() #добавляем экраны
       sm.add_widget(MainScr(name='main'))
       sm.add_widget(FirstScr(name='first'))
       sm.add_widget(SecondScr(name='second'))
       sm.add_widget(ThirdScr(name='third'))
       sm.add_widget(FourthScr(name='fourth'))
       sm.add_widget(fifthScr(name='fifth'))
       sm.add_widget(sixthScr(name='sixth'))
       sm.add_widget(seventhScr(name='seventh'))
       sm.add_widget(eighthScr(name='eighth'))
       sm.add_widget(ninthScr(name='ninth'))
       sm.add_widget(tenthScr(name='tenth'))
       sm.add_widget(eleventhScr(name='eleventh'))
       sm.add_widget(twelfthScr(name='twelfth'))
 
       return sm
 
MyApp().run() #старт программы