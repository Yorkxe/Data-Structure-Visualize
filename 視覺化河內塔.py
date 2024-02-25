import pygame, time
import tkinter as tk

#全域變數plate
global plate

#pygame初始化
pygame.init()

#開始按鈕繪製
x, y = 350, 100
width, height = 100, 50
button_rect = pygame.Rect(x, y, width, height)
button_color = (255, 255, 255)
text_color = (0, 0, 0)
button_font = pygame.font.SysFont('Arial', 20)
button_text = button_font.render("Start", True, text_color)

#視窗大小、名稱
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hanoi Tower")

def button_event():
    if enter.get() == '':
        tk.messagebox.showerror('message', 'Please enter a number')
    elif int(enter.get()) <= 0:
        tk.messagebox.showerror('message', 'Please enter a positive number')
    else:
        global plate
        plate = int(enter.get())
        root.destroy()
   
#限制輸入盤子數量只能輸入正整數
def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False
#顯示棍子   
def show_stick():
    for i in range(3):
        pygame.draw.rect(win, (153, 76, 0),(100 + 300 * i, 300, 20, 300))

#顯示初始盤子數量
def show_plate(plate_list):
    for i in range(3):
        count = 0
        for j in range(plate - 1, -1, -1):
            if plate_list[i][j] != 0:
                count += 1
                pygame.draw.rect(win, (255, 0, 0), (55 + 300 * i + 5 * count, 605 - 15 * count, 110 - 10 * count, 10))

def hanoi(plate, plate_list, p1, p2, p3):
    if plate == 1:
        for i in range(plate):
            for j in range(plate - 1, -1, -1):
                if plate_list[p1][i] != 0 and plate_list[p3][j] == 0:
                    plate_list[p3][j] = plate_list[p1][i]
                    plate_list[p1][i] = 0
                    break
        show_plate(plate_list)
        pygame.display.update()
        time.sleep(1)
    else:
        hanoi(plate - 1, plate_list, p1, p2, p3)
        for i in range(plate):
            for j in range(plate - 1, -1, -1):
                if plate_list[p1][i] != 0 and plate_list[p3][j] == 0:
                    plate_list[p3][j] = plate_list[p1][i]
                    plate_list[p1][i] = 0
                    break
            show_plate(plate_list)
            pygame.display.update()
        time.sleep(1)
        hanoi(plate - 1, plate_list, p1, p2, p3)

#輸入盤子之視窗
root = tk.Tk()
root.title('Hanoi Tower')

mylabel = tk.Label(root, text = 'Enter the amount of plates')
mylabel.grid(row = 0, column = 0)

vcmd = (root.register(validate), '%P')
enter = tk.Entry(root, validate = 'key', validatecommand = vcmd)

enter.grid(row = 0, column = 1)
#按鈕
mybutton = tk.Button(root, text = 'Enter', command = button_event)
mybutton.grid(row = 1, column = 1)

root.mainloop()


plate_list = [[i for i in range(plate, 0, -1)], [0] * plate, [0] * plate]

run = 1
execute = False

while run:  
    
    #判斷操作
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                execute = True
                print("Button clicked!")
    #河內塔畫面
    if not execute :
        win.fill((0, 0, 0))
        pygame.draw.rect(win, button_color, button_rect)
        win.blit(button_text, (button_rect.centerx - button_text.get_width() / 2, button_rect.centery - button_text.get_height() / 2))
        show_stick()
        show_plate(plate_list)
        pygame.display.update()
    else:
        pygame.display.update()
        win.fill((0, 0, 0))
        show_stick()
        hanoi(plate, plate_list, 0, 1, 2)       

    pygame.display.flip()
pygame.quit()
