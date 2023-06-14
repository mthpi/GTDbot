from PIL import Image, ImageDraw, ImageFont

'''
В это файле мы создаем класс для создания пнг изображения  - "визуализации"
нашей GTD схемы
'''

array = [['text_quest_1', 'text_if_no1'], ['text_quest_2', 'text_if_no_2'], ['text_quest_3', 'text_if_no_3'], 
         ['text_quest_4', 'text_if_no_4'], ['text_quest_5', 'text_if_no_5'], ['text_quest_6', 'text_if_no_6'], ['text_quest_7', 'text_if_no_7'], 
         ['text_quest_8', 'text_if_no_8'], 'name_of_last_list']


class Png_generator:

    def __init__(self):
        self.image = Image.new('RGB', (1800,2000), (255,255,255)) # создаем полотно 1800 на 1800 пикселей белого цвета
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype('arial.ttf', size=32)
        self.x = 800
        self.y = 200
    
    def draw_rectangles(self, x, y):
        self.draw.rectangle((x, y, x+200, y+100), fill='white', outline=(0,0,0), width=3) # создаем базовый прямоугольник размером 200 на 100 пикселей

    
    def draw_gorizont_arrow(self, x, y): # создаем горизонтальную стрелку вправо длинной 100 пикселей
        self.draw.line((x, y, x+100, y), fill='black', width=3)
        self.draw.line((x+80,y+10, x+100, y), fill='black', width=3)
        self.draw.line((x+80, y-10, x+100, y), fill='black', width=3)

    def draw_vertikal_arrow(self, x, y): # создаем вертикальную стрелку вниз длинной 100 пикселей
        self.draw.line((x, y, x, y+100), fill='black', width=3)
        self.draw.line((x-10, y+80, x, y+100), fill='black', width=3)
        self.draw.line((x+10, y+80, x, y+100), fill='black', width=3)

    
    def draw_many_rectangles(self, n): # создаем макет нашей визуализации, где n - число вопросов, через которая проходит задача (см. GTD система)
        
        base_for_text = self.image
        
        if n==1:
            self.draw_rectangles(self.x, self.y)
            self.draw_rectangles(self.x+300, self.y)
            self.draw_gorizont_arrow(self.x+200, self.y+50)
            self.draw_vertikal_arrow(self.x+100, self.y+100)
            self.draw.text((self.x+225,self.y+10), 'Нет', fill='black', font=self.font)
            self.draw.text((self.x+30,self.y+125), 'Да', fill='black', font=self.font)

        
        else:

            for c in range(1,n+1): # цикл рисует и возвращает изображение с нужным количеством прямоугольников, стрелочек и "да" "нет"
                self.draw_rectangles(self.x, self.y*c)
                self.draw_rectangles(self.x+300, self.y*c)
                self.draw_gorizont_arrow(self.x+200, self.y*c+50)
                self.draw_vertikal_arrow(self.x+100, self.y*c+100)
                self.draw.text((self.x+225,self.y*c+10), 'Нет', fill='black', font=self.font)
                self.draw.text((self.x+30,self.y*c+125), 'Да', fill='black', font=self.font)


        self.draw_rectangles(self.x, self.y*(n+1))
        
        return base_for_text
    
    
    def add_text_to_rectangle(self, array_of_quest_and_names_of_lists): # возвращает картинку с прямоугольниками и текстом через массив названий
        image = self.draw_many_rectangles(len(array_of_quest_and_names_of_lists)-1)
        draw = ImageDraw.Draw(image)

        for i in range(0, len(array_of_quest_and_names_of_lists)-1):
            draw.text((self.x+5,(self.y+5)*(i+1)), array_of_quest_and_names_of_lists[i][0], fill='black', font=self.font)
            draw.text((self.x+305, (self.y+5)*(i+1)), array_of_quest_and_names_of_lists[i][1], fill='black', font=self.font)
            draw.text((self.x+5, self.y*len(array_of_quest_and_names_of_lists)), array_of_quest_and_names_of_lists[-1], fill='black', font=self.font)
        return image
                





png = Png_generator()
png.add_text_to_rectangle(array).show()