import tkinter
import tkinter as tk
from PIL import ImageTk
import pygame
import threading
import time
import random

# 载入 音乐模块
pygame.mixer.init()


# 函数模块——————————————————————————————————————————


def get_green():
    global on_but1st
    global on_music
    global musicOnRun
    if not on_but1st:
        on_but1st = True
        mainTi_text.set("绿的你发光")
    else:
        on_but1st = False
        mainTi_text.set("爱是一道光")
    if on_music:
        mainTi_text.set(musicOnRun)


def playmusic():
    global on_music
    global musicOnRun
    pygame.mixer.music.load('mp3/1.mp3')
    musicOnRun = "要  坚  强"
    but1st.configure(text='？？？？')
    but1st.configure(fg='green')
    but3th.configure(fg='green')
    mainTi.configure(bg='green')
    partOne.configure(bg='green')
    if not on_music:
        pygame.mixer.music.play()
        on_music = True
    else:
        pygame.mixer.music.stop()
        but1st.configure(text='虚伪的力量')
        but1st.configure(fg='black')
        but3th.configure(fg='black')
        mainTi.configure(bg='black')
        partOne.configure(bg='black')
        if not pygame.mixer.music.get_busy():
            on_music = False


def playmusicforlist():
    global on_music
    global musicName
    global musicOnRun
    if musicName == '尚未选择':
        msg = tk.Toplevel()
        msg.geometry('300x100')
        msg.resizable(width=False, height=False)
        msg.title("ERROR")
        msg_lab = tk.Label(msg, text="尚未选择要播放的音乐！")
        msg_lab.place(x=90, y=20)

        def msg_qt():
            msg.destroy()

        msg_but = tk.Button(msg, text='确认', command=msg_qt, width=8)
        msg_but.place(x=120, y=60)
    else:
        pygame.mixer.music.load("mp3/" + mscDic[musicName])
        musicOnRun = "正在播放:" + musicName
        but1st.configure(text="正在播放？")
        but1st.configure(bg="yellow")
        if not on_music:
            pygame.mixer.music.play()
            on_music = True
            but4th.configure(text='停止')
        else:
            global on_rand_play
            on_rand_play = False
            global on_list_play_loop
            on_list_play_loop = False
            pygame.mixer.music.stop()
            but4th.configure(text='播放')
            but1st.configure(text="虚伪的力量")
        if not pygame.mixer.music.get_busy():
            on_music = False
            but4th.configure(text='播放')
            but1st.configure(bg="white")


def pause_music():
    global on_pause_music
    if not on_pause_music:
        pygame.mixer.music.pause()
        on_pause_music = True
        pauseBut.configure(text='继续播放')
    else:
        pygame.mixer.music.unpause()
        on_pause_music = False
        pauseBut.configure(text='暂停播放')


def msclist_selection(event):
    global musicName
    musicName = str(musicListBox.get(musicListBox.curselection()))
    mscLabelVal.set(musicName)


def change_bg():
    global bgNum
    global bk_gd
    if bgNum == 4:
        bgNum = 1
        bk_gd = ImageTk.PhotoImage(file=('background/bg' + str(bgNum) + '.png'))
        bg.configure(image=bk_gd)
    else:
        bgNum += 1
        bk_gd = ImageTk.PhotoImage(file=('background/bg' + str(bgNum) + '.png'))
        bg.configure(image=bk_gd)


def rand_play():
    import random
    temp = random.randint(0, len(mscKey)-1)
    global on_music
    global musicName
    global musicOnRun
    global on_rand_play
    musicName = mscKey[temp]
    pygame.mixer.music.load("mp3/" + mscDic[musicName])
    musicOnRun = "正在播放:" + musicName
    but1st.configure(text="正在播放？")
    but1st.configure(bg="yellow")
    pygame.mixer.music.play()
    on_music = True
    but4th.configure(text='停止')
    on_rand_play = True


def list_play():
    global on_music
    global musicName
    global musicOnRun
    global mscKey
    global mscDic
    global on_list_play_loop
    global list_play_num
    if not pygame. mixer.get_busy():
        if list_play_num != len(mscKey)-1:
            musicName = mscKey[list_play_num]
            musicOnRun = "正在播放:" + musicName
            pygame.mixer.music.load("mp3/" + mscDic[mscKey[list_play_num]])
            pygame.mixer.music.play()
            list_play_num += 1
            but1st.configure(text="正在播放？")
            but1st.configure(bg="yellow")
            on_music = True
            on_list_play_loop = True
        if list_play_num == len(mscKey)-1:
            musicName = mscKey[list_play_num]
            musicOnRun = "正在播放:" + musicName
            pygame.mixer.music.load("mp3/" + mscDic[mscKey[list_play_num]])
            pygame.mixer.music.play()
            list_play_num = 0
            but1st.configure(text="正在播放？")
            but1st.configure(bg="yellow")
            on_music = True
            on_list_play_loop = True
        but4th.configure(text='停止')


# 窗体初定义————————————————————————————————————————
top = tkinter.Tk()
top.title("试作型人工播放器I型")
top.geometry('800x600+500+200')
top.resizable(width=False, height=False)
top.iconbitmap('icon.ico')
bgNum = 1
bk_gd = ImageTk.PhotoImage(file=('background/bg' + str(bgNum) + '.png'))
bg = tk.Label(top, width=800, height=600, image=bk_gd)
bg.pack()


def explain():
    explain_page = tk.Toplevel()
    explain_page.geometry('300x100+800+500')
    explain_page.resizable(width=False, height=False)
    explain_page.title("说明")
    explain_page_msg_lab = tk.Label(explain_page, text="素材均来源与公开的网络于个人购买")
    explain_page_msg_lab.pack()


explain_but_img = ImageTk.PhotoImage(file='but_kizuna.png')
explain_but = tk.Button(top, width=30, height=30, image=explain_but_img, command=explain)
explain_but.place(x=750, y=50)

# 全局开关变量————————————————————————————————————————
on_music = False
on_but1st = True

# 布局设定——————————————————————————————————————————
rb_pic = tk.Label(top, text='鲸某人永不为奴', width=12, height=1, bg='black', fg='yellow')
rb_pic.place(x=700, y=570)
rb_pic2 = tk.Label(top, text='v0.1.2', width=12, height=1, bg='black', fg='yellow')
rb_pic2.place(x=700, y=550)
lb_pic = tk.Label(top, text='我是真的懒。', width=10, height=1, bg='black', fg='yellow')
lb_pic.place(x=8, y=570)


# partOne Label标签联动————————————————————————————————————
partOne = tk.Frame(top, width=240, height=100, bg='black')
partOne.place(x=0, y=0)
mainTi_text = tkinter.StringVar()
mainTi = tkinter.Label(partOne, textvariable=mainTi_text, font=('Arial', 12), width=24, height=2, bg='black', fg='yellow')
mainTi.place(x=10, y=0)
mainTi_text.set("给我力量!!!")
but1st = tkinter.Button(partOne, text='虚伪的力量', width=12, height=2, command=get_green)
but1st.place(x=20, y=40)
but3th = tk.Button(partOne, text='真正的力量', width=12, height=2, command=playmusic)
but3th.place(x=130, y=40)

# 音乐列表——————————————————————————————————————————
partTwo = tk.Frame(top, width=240, height=260, bg='black')
partTwo.place(x=0, y=100)
mscLabelVal = tk.StringVar()
musicOnRun = tk.StringVar()
musicName = "尚未选择"
mscVal = ["The Verkkars - EZ4ENCE (kannatuslaulu).mp3",
          "Hanser - 藤原千花角色歌-テカっとチカ千花っ（Cover：小原好美）.mp3"
          ]

mscKey = ["EZ4ENCE",
          "テカっとチカ千花っ"]

mscDic = {"テカっとチカ千花っ": "Hanser - 藤原千花角色歌-テカっとチカ千花っ（Cover：小原好美）.mp3",
          "EZ4ENCE": "The Verkkars - EZ4ENCE (kannatuslaulu).mp3"
          }
musicListBox = tk.Listbox(partTwo, width=22, bg='black', fg='yellow')
musicListBox.place(x=0, y=0)
for i in mscKey:
    musicListBox.insert('end', i)

musicListBox.bind('<ButtonRelease-1>', msclist_selection)

on_rand_play = False
but4th = tk.Button(partTwo, text='播放', width=10, height=2, command=playmusicforlist)
but4th.place(x=160, y=0)
on_pause_music = False
pauseBut = tk.Button(partTwo, text='暂停播放', width=10, height=2, command=pause_music)
pauseBut.place(x=160, y=50)

on_list_play_loop = False
list_play_num = 0
loopBut = tk.Button(partTwo, text='循环播放', width=10, height=2, command=list_play)
loopBut.place(x=160, y=100)

but_randMusic = tk.Button(partTwo, width=10, height=2, text='随机播放', command=rand_play)
but_randMusic.place(x=160, y=150)
mscLabelVal.set(str(musicName))
mscLabel1 = tk.Label(partTwo, text='当前选定：                ', width=22, height=2, bg='black', fg='white')
mscLabel1.place(x=0, y=185)
mscLabel2 = tk.Label(partTwo, textvariable=mscLabelVal, width=22, height=2, bg='black', fg='yellow')
mscLabel2.place(x=40, y=215)

on_of_volume_frame = False
volume_frame = tk.Frame(top, width=100, height=120)
pygame_volume = eval("{:.2f}".format(0.5))
pygame_volume_display = tk.StringVar()
pygame_volume_display.set("音量：" + str(pygame_volume))
pygame.mixer.music.set_volume(pygame_volume)


def open_volume_frame():
    global on_of_volume_frame
    if not on_of_volume_frame:
        volume_frame.place(relx=0.31, rely=0.4)
        on_of_volume_frame = True
    else:
        volume_frame.place_forget()
        on_of_volume_frame = False


def up_volume():
    global pygame_volume
    pygame_volume += 0.1
    pygame_volume = eval("{:.2f}".format(pygame_volume))
    if pygame_volume > 1.0:
        pygame_volume = 1.0
    pygame.mixer.music.set_volume(pygame_volume)
    pygame_volume_display.set("音量：" + str(pygame_volume))


def down_volume():
    global pygame_volume
    pygame_volume -= 0.1
    pygame_volume = eval("{:.2f}".format(pygame_volume))
    if pygame_volume < 0.1:
        pygame_volume = 0.1
    pygame.mixer.music.set_volume(pygame_volume)
    pygame_volume_display.set("音量：" + str(pygame_volume))


plus_of_volume_frame = tk.Button(partTwo, width=3, height=1, text='+', command=open_volume_frame)
plus_of_volume_frame.place(x=205, y=200)
but_volume_plus = tk.Button(volume_frame, width=10, height=1, text='音量 ＋ ', command=up_volume)
but_volume_plus.place(x=10, y=10)
but_volume_subtract = tk.Button(volume_frame, width=10, height=1, text='音量 － ', command=down_volume)
but_volume_subtract.place(x=10, y=50)
volume_display = tk.Label(volume_frame, width=10, height=1, textvariable=pygame_volume_display)
volume_display.place(x=10, y=90)

# 更换壁纸模块——————————————————————————————————————
bg_but = tk.Button(top, width=10, height=2, text='更换壁纸', command=change_bg)
bg_but.place(x=10, y=370)


# pet模块——————————————————————————————————————————

# 存读雏形

# 读档


pet_file = open('pet_attribute.txt', 'r')
txt = pet_file.read()
txt = txt.split("\n")
val_key = []                    # 键值中介，读档存档中都要应用
key_val = []                    # 值中介,仅在读档中用到
for i in range(0, len(txt)):
    val_key.insert(i, txt[i][:2])    # txt[i][:2]使得key值为2位
    key_val.insert(i, txt[i][3:])
pet_attribute = {}
for i in range(0, len(txt)):
    pet_attribute[val_key[i]] = key_val[i]

# 部分属性的更新
pet_attribute["攻击"] = str(8 + int(pet_attribute["等级"]) * 1.25)
pet_attribute["防御"] = str(3 + int(pet_attribute["等级"]) * 0.75)
pet_file.close()
print(pet_attribute)


# 存档
def save():
    global lab_petVal
    save_txt = ''
    for i in range(0, len(txt)):
        save_txt += str(val_key[i]) + ":" + str(pet_attribute[val_key[i]])
        if i != len(txt) - 1:
            save_txt += '\n'
    print(save_txt)
    file = open('pet_attribute.txt', 'w')
    file.write(save_txt)
    print(lab_petVal.get())
    file_setting = open('pet_setting.txt', 'w')
    file_setting.write(lab_petVal.get())


pet_save = tk.Button(top, width=10, height=2, text='存档', cursor='heart', command=save, bg='black', fg='yellow')
pet_save.place(x=280, y=370)


# 属性面板 动态值——————————————————————————————————————
pet_attribute_lv = tk.StringVar()
pet_attribute_lv.set("等级：" + pet_attribute["等级"])
pet_attribute_life = tk.StringVar()
pet_attribute_life.set("生命值：" + pet_attribute["生命"] + "/100")
pet_attribute_atk = tk.StringVar()
pet_attribute_atk.set("攻击力：" + pet_attribute["攻击"])
pet_attribute_def = tk.StringVar()
pet_attribute_def.set("防御力：" + pet_attribute["防御"])
pet_attribute_hgr = tk.StringVar()
pet_attribute_hgr.set("饱食度：" + pet_attribute["饥饿"])
pet_attribute_like = tk.StringVar()
pet_attribute_like.set("好感度：" + pet_attribute["好感"])
pet_attribute_money = tk.StringVar()
pet_attribute_money.set("零花钱：" + pet_attribute["金钱"])
pet_attribute_food = tk.StringVar()
pet_attribute_food.set("食物：" + pet_attribute["食物"])
pet_attribute_suger = tk.StringVar()
pet_attribute_suger.set("糖果：" + pet_attribute["糖果"])
pet_attribute_bandage = tk.StringVar()
pet_attribute_bandage.set("绷带：" + pet_attribute["绷带"])


on_off_pet_frame = False


# 属性界面的开关：——————————————————————————————————————


def open_pet_frame():
    global on_off_pet_frame
    if not on_off_pet_frame:
        pet_frame.place(x=390, y=340)
        on_off_pet_frame = True
    else:
        pet_frame.place_forget()
        on_off_pet_frame = False


but_opWin = tk.Button(top, width=10, height=2, text='宠物属性', command=open_pet_frame)
but_opWin.place(x=100, y=370)

# 宠物头像加载
lab_petVal = tk.StringVar()

# 加载头像时载入配置
pet_img_index = {
    "花園セレナ": "pet1.png",
    "神楽めあ": "pet2.png",
    "湊あくあ": "pet3.png",
}
pet_setting_read = open('pet_setting.txt', 'r')
txt_setting = pet_setting_read.read()
petImg = ImageTk.PhotoImage(file=pet_img_index[txt_setting])
lab_petVal.set(str(txt_setting))


def pet_talk():
    import random
    # 默认对话集
    if lab_petVal.get() == "花園セレナ":
        talk_list = ["救...救猫猫~",
                     ]
    if lab_petVal.get() == "神楽めあ":
        talk_list = ["妮耗，我喊苦艾",
                     "你丫的对mea我有什么意见吗？？",
                     "请给我打钱",
                     "阿夸又把我鸽了",
                     "这不完全是死肥宅吗",
                     "？",
                     "？？",
                     "N·M·S·L",
                     "(擦盘子)"]

    if lab_petVal.get() == "湊あくあ":
        talk_list = ["我已经完全理解了！！！",
                     "理解、理解！！",
                     "真的？！",
                     "我就是力量的化身!",
                     "いいっすね！",
                     "原来如此，懂了懂了！！",
                     "お前、弱い、あたし、強い！",
                     "等我拿到和平你就死定了.jpg",
                     "あ·く·あ·ま·じ·て·ん·し！",
                     "本·社·爆·破",
                     "Mea由我来守护！",
                     "因为喜欢所以是没办法的啊!"]

    a = talk_list[random.randint(0, len(talk_list)-1)]
    pet_text.config(state='normal')
    pet_text.insert('end', a + "\n")
    pet_text.see(tkinter.END)
    pet_text.config(state='disable')
    lab_talkVal.set(a)


pet_mea_image = ImageTk.PhotoImage(file='pet2.png')
pet_serena_image = ImageTk.PhotoImage(file='pet1.png')
pet_aqua_image = ImageTk.PhotoImage(file='pet3.png')


def pet_switch_button():
    global pet_mea_image
    global pet_serena_image

    def switch_to_mea():
        global petImg
        global lab_petVal
        petImg = pet_mea_image
        but_pet.configure(image=pet_mea_image)
        lab_petVal.set("神楽めあ")

    def switch_to_serena():
        global petImg
        global lab_petVal
        petImg = pet_serena_image
        but_pet.configure(image=pet_serena_image)
        lab_petVal.set("花園セレナ")

    def switch_to_aqua():
        global petImg
        global lab_petVal
        petImg = pet_aqua_image
        but_pet.configure(image=pet_aqua_image)
        lab_petVal.set("湊あくあ")

    pet_switch = tk.Toplevel()
    pet_switch.geometry("380x180")
    pet_switch.title("_(:з」∠)_我是ＤＤ")
    pet_switch.iconbitmap("icon.ico")
    pet_switch.resizable(width=False, height=False)

    pet_mea_img = tk.Button(pet_switch, width=100, height=100, image=pet_mea_image, command=switch_to_mea)
    pet_mea_img.place(x=20, y=20)
    pet_mea_name = tk.Label(pet_switch, width=10, height=1, text="神楽めあ")
    pet_mea_name.place(x=35, y=140)

    pet_serena_img = tk.Button(pet_switch, width=100, height=100, image=pet_serena_image, command=switch_to_serena)
    pet_serena_img.place(x=140, y=20)
    pet_serena_name = tk.Label(pet_switch, width=10, height=1, text="花園セレナ")
    pet_serena_name.place(x=155, y=140)

    pet_aqua_img = tk.Button(pet_switch, width=100, height=100, image=pet_aqua_image, command=switch_to_aqua)
    pet_aqua_img.place(x=260, y=20)
    pet_aqua_name = tk.Label(pet_switch, width=10, height=1, text="湊あくあ")
    pet_aqua_name.place(x=275, y=140)


but_pet = tk.Button(top, width=100, height=100, image=petImg, command=pet_talk)
but_pet.place(x=10, y=420)

lab_pet = tk.Button(top, textvariable=lab_petVal, width=10, height=1, font=('微软雅黑', 12), command=pet_switch_button)
lab_pet.place(x=8, y=530)
lab_talkVal = tk.StringVar()
lab_talkVal.set("今天又是充满希望的一天！")
lab_talk = tk.Label(top, textvariable=lab_talkVal, width=30, height=3, font=('微软雅黑', 10))
lab_talk.place(x=130, y=425)


# 宠物属性界面的值传递设定：————————————————————————————————


pet_frame = tk.Frame(top, width=180, height=250)
pet_frame_title = tk.Label(pet_frame, width=20, height=1, text='———— 属性栏 ————', anchor='w')
pet_frame_title.place(x=10, y=0)
pet_frame_lv = tk.Label(pet_frame, textvariable=pet_attribute_lv, width=20, height=2, anchor="nw")
pet_frame_lv.place(x=10, y=20)
pet_frame_life = tk.Label(pet_frame, textvariable=pet_attribute_life, width=20, height=2, anchor="nw")
pet_frame_life.place(x=10, y=40)
pet_frame_atk = tk.Label(pet_frame, textvariable=pet_attribute_atk, width=20, height=2, anchor="nw")
pet_frame_atk.place(x=10, y=60)
pet_frame_def = tk.Label(pet_frame, textvariable=pet_attribute_def, width=20, height=2, anchor="nw")
pet_frame_def.place(x=10, y=80)
pet_frame_hgr = tk.Label(pet_frame, textvariable=pet_attribute_hgr, width=20, height=2, anchor="nw")
pet_frame_hgr.place(x=10, y=100)
pet_frame_like = tk.Label(pet_frame, textvariable=pet_attribute_like, width=20, height=2, anchor="nw")
pet_frame_like.place(x=10, y=120)
pet_frame_money = tk.Label(pet_frame, textvariable=pet_attribute_money, width=20, height=2, anchor="nw")
pet_frame_money.place(x=10, y=140)
pet_frame_food = tk.Label(pet_frame, textvariable=pet_attribute_food, width=20, height=2, anchor="nw")
pet_frame_food.place(x=10, y=160)


def clear_pet_text():
    pet_text.config(state='normal')
    pet_text.delete(0.0, 'end')
    pet_text.config(state='disable')


pet_text = tk.Text(top, width=20, height=7)
pet_text.place(x=130, y=495)
pet_text.config(state='disable')
pet_text_clearBut = tk.Button(top, text='清屏', width=10, height=2, command=clear_pet_text)
pet_text_clearBut.place(x=290, y=520)


# 饱食度恢复————————————————————————————————————————


def eating():
    if int(pet_attribute['食物']) > 0:
        pet_attribute['饥饿'] = str(int(pet_attribute['饥饿'])+40)
        pet_attribute['食物'] = str(int(pet_attribute['食物'])-1)
        pet_attribute_hgr.set("饱食度：" + pet_attribute["饥饿"])
        pet_attribute_food.set("食物：" + pet_attribute["食物"])
    else:
        a = "食物不足！请通过探索或购买获得食物吧！"
        pet_text.config(state='normal')
        pet_text.insert('end', a + "\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')
    if eval(pet_attribute['饥饿']) > 100:
        pet_attribute['饥饿'] = '100'
        pet_attribute_hgr.set("饱食度：" + pet_attribute["饥饿"])
        pet_attribute_food.set("食物：" + pet_attribute["食物"])
        pet_text.config(state='normal')
        pet_text.insert('end', "已经吃的很饱饱啦！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')


# 宠物打工————————————————————————————————————————
working_on_busy = False
on_of_pet_finding = False


def working():
    global working_on_busy
    global on_of_pet_finding
    if on_of_pet_finding:
        pet_text.config(state='normal')
        pet_text.insert('end', "正在探索中！无法工作！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')
    else:
        if not working_on_busy:
            def work_timer():
                global working_on_busy
                pet_attribute['金钱'] = str(int(pet_attribute['金钱'])+100)
                pet_attribute_money.set("零花钱：" + pet_attribute["金钱"])
                pet_text.config(state='normal')
                pet_text.insert('end', "6分钟已经结束啦！薪水已经进账了\n")
                pet_text.see(tkinter.END)
                pet_text.config(state='disable')
                working_on_busy = False
                pet_working.configure(bg='white', fg='black', text='搬砖')

            timer_work = threading.Timer(5, work_timer)
            timer_work.start()

            working_on_busy = True
            pet_working.configure(bg='black', fg='yellow', text='正在搬砖')
            pet_text.config(state='normal')
            pet_text.insert('end', "已经开始搬砖了！6分钟后可以获得薪水！\n")
            pet_text.see(tkinter.END)
            pet_text.config(state='disable')


# 购买食物的操作————————————————————————————————————
def add_food():
    if eval(pet_attribute['金钱']) >= 40:
        pet_attribute['食物'] = str(int(pet_attribute['食物']) + 1)
        pet_attribute_food.set("食物：" + pet_attribute["食物"])
        pet_attribute['金钱'] = str(int(pet_attribute['金钱']) - 40)
        pet_attribute_money.set("零花钱：" + pet_attribute["金钱"])
    if eval(pet_attribute['金钱']) < 40:
        pet_text.config(state='normal')
        pet_text.insert("end", "零花钱不足！无法购买食物！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')


def add_bandage():
    if eval(pet_attribute['金钱']) >= 60:
        pet_attribute['绷带'] = str(int(pet_attribute['绷带']) + 1)
        pet_attribute['金钱'] = str(int(pet_attribute['金钱']) - 60)
    if eval(pet_attribute['金钱']) < 60:
        pet_text.config(state='normal')
        pet_text.insert("end", "零花钱不足！无法购买绷带！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')


def add_suger():
    if eval(pet_attribute['金钱']) >= 100:
        pet_attribute['糖果'] = str(int(pet_attribute['糖果']) + 1)
        pet_attribute['金钱'] = str(int(pet_attribute['金钱']) - 100)
    if eval(pet_attribute['金钱']) < 100:
        pet_text.config(state='normal')
        pet_text.insert("end", "零花钱不足！无法购买糖果！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')


# 宠物探索————————————————————————————————————————
def pet_finding_but():
    global on_of_pet_finding
    global working_on_busy
    if working_on_busy:
        pet_text.config(state='normal')
        pet_text.insert('end', "正在工作中！无法探索！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')
    else:
        if not on_of_pet_finding:
            on_of_pet_finding = True
            pet_text.config(state='normal')
            pet_text.insert('end', "进行探索！！5分钟后收获。\n")
            pet_text.see(tkinter.END)
            pet_text.config(state='disable')
            pet_finding.configure(bg='green', fg='black', text='正在探索')

            def find_timer():
                import random
                global on_of_pet_finding
                randItem = random.randint(0,2)
                randItemList = ["食物", "绷带", "糖果"]
                randItemNum = random.randint(1, 3)
                pet_attribute[randItemList[randItem]] = str(int(pet_attribute[randItemList[randItem]]) + randItemNum)
                pet_text.config(state='normal')
                pet_text.insert('end', "获得了" + randItemList[randItem] + "*" + str(randItemNum) + "\n")
                pet_text.see(tkinter.END)
                pet_text.config(state='disable')
                pet_attribute_food.set("食物：" + pet_attribute["食物"])
                pet_attribute_bandage.set("绷带：" + pet_attribute["绷带"])
                pet_attribute_suger.set("糖果：" + pet_attribute["糖果"])
                pet_finding.configure(bg='white', fg='black', text='探索')
                on_of_pet_finding = False

            timer_find = threading.Timer(3, find_timer)
            timer_find.start()


# 宠物商店界面的定义，以及商城道具的定义————————————————————————————
on_pet_shop = False
pet_shop_frame = tk.Frame(top, width=360, height=200)
pet_shop_frame_title = tk.Label(pet_shop_frame, width=40, height=1, text='—————————— 商店 ——————————', anchor='w')
pet_shop_frame_title.place(x=30, y=0)
pet_shop_item_01 = tk.Button(pet_shop_frame, width=12, height=2, text='购买食物($40)', command=add_food)
pet_shop_item_01.place(x=10, y=40)
pet_shop_item_02 = tk.Button(pet_shop_frame, width=12, height=2, text='购买绷带($60)', command=add_bandage)
pet_shop_item_02.place(x=10, y=90)
pet_shop_item_03 = tk.Button(pet_shop_frame, width=12, height=2, text='购买糖果($100)', command=add_suger)
pet_shop_item_03.place(x=10, y=140)


# 宠物操作中商店的开关————————————————————————————————————
def open_pet_shop():
    global on_pet_shop
    if not on_pet_shop:
        pet_shop_frame.place(x=360, y=130)
        on_pet_shop = True
    else:
        pet_shop_frame.place_forget()
        on_pet_shop = False


# 操作界面——————————————————————————————————————————
on_off_pet_action_but = False
on_of_pet_item_frame = False
pet_item_frame = tk.Frame(top, width=300, height=110)
pet_item_frame_title = tk.Label(pet_item_frame, width=40, height=1, text='—————— 道具栏 ——————')
pet_item_frame_title.place(x=0, y=0)
pet_item_frame_01 = tk.Label(pet_item_frame, width=4, height=1, text='绷带')
pet_item_frame_01.place(x=20, y=80)
pet_item_frame_01_img_file = ImageTk.PhotoImage(file='item_block/item_01.png')
pet_item_frame_01_img = tk.Button(pet_item_frame, width=50, height=50, image=pet_item_frame_01_img_file)
pet_item_frame_01_img.place(x=10, y=20)

pet_item_frame_02 = tk.Label(pet_item_frame, width=4, height=1, text='糖果')
pet_item_frame_02.place(x=80, y=80)
pet_item_frame_02_img_file = ImageTk.PhotoImage(file='item_block/item_02.png')
pet_item_frame_02_img = tk.Button(pet_item_frame, width=50, height=50, image=pet_item_frame_02_img_file)
pet_item_frame_02_img.place(x=70, y=20)


def open_pet_item():
    global on_of_pet_item_frame
    if not on_of_pet_item_frame:
        pet_item_frame.place(x=360, y=10)
        on_of_pet_item_frame = True
    else:
        pet_item_frame.place_forget()
        on_of_pet_item_frame = False


# 操作界面开关————————————————————————————————————————
def open_pet_action():
    global on_off_pet_action_but
    if not on_off_pet_action_but:
        pet_action_frame.place(x=250, y=40)
        on_off_pet_action_but = True
    else:
        pet_action_frame.place_forget()
        on_off_pet_action_but = False


pet_action_but = tk.Button(top, text='宠物操作', width=10, height=2, command=open_pet_action)
pet_action_but.place(x=190, y=370)
pet_action_frame = tk.Frame(top, width=100, height=320)
pet_item = tk.Button(pet_action_frame, text='道具', bg="white", width=10, height=2, command=open_pet_item)
pet_item.place(x=10, y=10)
pet_eating = tk.Button(pet_action_frame, text='投食', bg="white", width=10, height=2, command=eating)
pet_eating.place(x=10, y=60)
pet_working = tk.Button(pet_action_frame, text='搬砖', bg="white", width=10, height=2, command=working)
pet_working.place(x=10, y=110)
pet_shop = tk.Button(pet_action_frame, text='商店', bg="white", width=10, height=2, command=open_pet_shop)
pet_shop.place(x=10, y=160)
pet_finding = tk.Button(pet_action_frame, text='探索', bg="white", width=10, height=2, command=pet_finding_but)
pet_finding.place(x=10, y=210)

# 怪物的属性暂用与global传递
monster_attribute = {"hp": 70, "def": 10, "atk": 12}
monster_attribute_in_battle = {"hp": 70, "def": 10, "atk": 12}


on_battleMod = False
battleMod_on_of_but_item = False
battleMod_on_of_but_skill = False

test_enemy_head = ImageTk.PhotoImage(file='enemy_head/1.png')


# 战斗事件——————————————————————————————————————————
def pet_battle_event():
    # 播放音乐时停止
    global on_list_play_loop
    global on_rand_play
    # 传入pet的name属性（暂无用）
    global lab_petVal
    # 传入pet的属性
    global pet_attribute
    global petImg
    global pet_img_index
    global on_battleMod
    global test_enemy_head

    if on_battleMod:
        pet_text.config(state='normal')
        pet_text.insert('end', "你已经处于一场战斗中了！\n")
        pet_text.see(tkinter.END)
        pet_text.config(state='disable')
        return 0

    on_battleMod = True

    battleMod = tk.Toplevel()
    battleMod.title("战斗")
    battleMod.geometry('500x500+300+200')
    battleMod.resizable(width=False, height=False)
    battleMod.iconbitmap('icon.ico')

    pygame.mixer.music.stop()
    on_list_play_loop = False
    on_rand_play = False
    battle_music_list = [
        "battle_bgm/光宗信吉 - クリティウスの牙.mp3",
        "battle_bgm/口袋妖怪OLD.mp3",
        "battle_bgm/鶴山尚史 - Trombe!.mp3",
        "battle_bgm/末廣健一郎 - 英雄のタクト -起源-.mp3",

    ]
    battle_music_in_use = random.randint(0, len(battle_music_list)-1)
    pygame.mixer.music.load(battle_music_list[battle_music_in_use])
    pygame.mixer.music.play(loops=-1)

    # 显示 主窗口，主窗口背景
    frame1_bg_file = ImageTk.PhotoImage(file="battle_bg/battle_bg_1.png")
    frame1 = tk.Frame(battleMod, width=500, height=350, bg='pink')
    frame1.place(x=-2, y=0)
    frame1_bg = tk.Label(frame1, width=500, height=350, image=frame1_bg_file)
    frame1_bg.pack()

    # 血条、头像
    frame1_pet_pic = tk.Label(frame1, width=100, height=100, image=petImg)
    frame1_pet_pic.place(x=20, y=230)
    frame1_pet_name = tk.Label(frame1, width=14, height=1, textvariable=lab_petVal)
    frame1_pet_name.place(x=20, y=200)
    frame1_pet_hp_long = tk.Label(frame1, width=30, height=1)
    frame1_pet_hp_long.place(x=130, y=310)
    frame1_pet_hp_short = tk.Label(frame1, width=30, height=1, bg='red')
    frame1_pet_hp_short.place(x=130, y=310)
    frame1_pet_hp_short.configure(width=int((eval(pet_attribute["生命"])/100) * 30))

    pet_hp_now = tk.StringVar()
    pet_hp_now.set("HP：" + pet_attribute["生命"] + " / " + "100")
    frame1_pet_hp_now = tk.Label(frame1, width=14, height=1, textvariable=pet_hp_now)
    frame1_pet_hp_now.place(x=130, y=280)

    frame1_monster_pic = tk.Label(frame1, width=100, height=100, image=test_enemy_head)
    frame1_monster_pic.place(x=380, y=10)
    frame1_monster_name = tk.Label(frame1, width=14, height=1, text='爱酱')
    frame1_monster_name.place(x=380, y=120)
    frame1_monster_hp_long = tk.Label(frame1, width=30, height=1)
    frame1_monster_hp_long.place(x=160, y=10)
    frame1_monster_hp_short = tk.Label(frame1, width=30, height=1, bg='red')
    frame1_monster_hp_short.place(x=160, y=10)
    frame1_monster_hp_short.configure(width=int(monster_attribute_in_battle["hp"] / 70 * 30))

    monster_hp_now = tk.StringVar()
    monster_hp_now.set("HP：" + str(monster_attribute_in_battle["hp"]) + " / " + "70")
    frame1_monster_hp_now = tk.Label(frame1, width=14, height=1, textvariable=monster_hp_now)
    frame1_monster_hp_now.place(x=270, y=40)

    # 按钮
    frame2_under = tk.Frame(battleMod, width=200, height=150, bg='black')
    frame2_under.place(x=300, y=350)
    frame2 = tk.Frame(battleMod, width=200, height=150, bg='black')
    frame2.place(x=300, y=350)
    frame2Lbl = tk.Label(frame2, width=20, height=1, bg='black', fg='yellow', textvariable=lab_petVal)
    frame2Lbl.place(x=-25, y=10)
    frame2Lbl_2 = tk.Label(frame2, width=10, height=1, bg='black', fg='white', text='准备做什么？')
    frame2Lbl_2.place(x=100, y=10)

    # 攻击事件——————————————————————————————————————
    def battle_atk_event():
        global monster_attribute_in_battle, battleMod_on_of_but_item, battleMod_on_of_but_skill

        # 关闭道具栏和技能栏
        if battleMod_on_of_but_item:
            battleMod_on_of_but_item = False
            but_item_frame.place_forget()

        if battleMod_on_of_but_skill:
            battleMod_on_of_but_skill = False
            but_skill_frame.place_forget()

        # 攻击，计算伤害（1）
        print(monster_attribute_in_battle["hp"])
        battle_text.insert('end', lab_petVal.get() + "开始进行攻击！\n")
        battle_text.see(tkinter.END)
        frame2.place_forget()

        # 我方攻击行动的伤害计算
        damage_floating = random.randint(-5, 5)
        damage = int((eval(pet_attribute["攻击"]) - monster_attribute_in_battle["def"] * 1.25) * 1.75) + damage_floating

        # 暴击的判定
        damage_critical = random.randint(0, 100)
        if damage_critical < 90:
            text_type = [
                lab_petVal.get() + "对敌方造成了" + str(damage) + "点伤害！\n",
                lab_petVal.get() + "试图攻击敌方, 成功造成了" + str(damage) + "点伤害！\n",
                lab_petVal.get() + "抓住了敌方造成了" + str(damage) + "点伤害！\n",
                     ]
        else:
            damage *= 2.5
            damage = int(damage)
            text_type = [
                lab_petVal.get() + "打出了致命一击！对敌方造成了" + str(damage) + "点伤害！\n",
                lab_petVal.get() + "抓住了敌方的弱点！成功造成了" + str(damage) + "点伤害！\n",
            ]
        rand_type = random.randint(0, len(text_type)-1)

        # 战斗日志的更新，造成伤害后怪物HP的更新（2）
        def battle_atk_event_going_1():
            global monster_attribute_in_battle
            battle_text.insert('end', text_type[rand_type])
            battle_text.see(tkinter.END)
            monster_attribute_in_battle["hp"] -= damage

            if monster_attribute_in_battle["hp"] < 0:
                monster_attribute_in_battle["hp"] = 0

            frame1_monster_hp_short.configure(width=int(monster_attribute_in_battle["hp"] / 70 * 30))
            monster_hp_now.set("HP：" + str(monster_attribute_in_battle["hp"]) + " / " + "70")

            # 敌方HP小于0，结束战斗界面，获得奖励
            if monster_attribute_in_battle["hp"] == 0:
                pygame.mixer.music.stop()
                # 胜利BGM——EZ4enceenceence dens putted upperbelt
                pygame.mixer.music.load("mp3/The Verkkars - EZ4ENCE (kannatuslaulu).mp3")
                pygame.mixer.music.play(loops=-1)
                battle_text.insert('end', "战斗结束，恭喜你获得了胜利！\n")
                battle_text.see(tkinter.END)

                # 战斗结束
                def end_battle():
                    end_frame = tk.Frame(battleMod, width=300, height=300)
                    end_frame.place(x=100, y=100)

                    def end_frame_but_event():
                        global on_battleMod, monster_attribute_in_battle, monster_attribute
                        battleMod.destroy()
                        pygame.mixer.music.stop()
                        on_battleMod = False
                        # 结束时为下一场战斗reload，爱酱我错了。
                        monster_attribute_in_battle = monster_attribute

                    end_frame_but = tk.Button(end_frame, width=10, height=2, text='返回', command=end_frame_but_event)
                    end_frame_but.place(x=110, y=240)

                timer_end_battle = threading.Timer(2, end_battle)
                timer_end_battle.start()
            else:
                timer_battle_atk_event_2.start()

        # 过度到敌方回合，日志更新（3）
        def battle_atk_event_going_2():
            global monster_attribute_in_battle
            battle_text.insert('end', "现在是敌方的回合！\n")
            battle_text.see(tkinter.END)
            timer_battle_atk_event_3.start()

        # 战斗日志的更新，造成伤害后pet hp的更新（4）
        def battle_atk_event_going_3():
            global monster_attribute_in_battle
            damage = int((monster_attribute_in_battle["atk"] - eval(pet_attribute["防御"]) * 0.75) * 1.75)
            if damage < 0:
                damage = 0
            text_type = [
                "对我方造成了" + str(damage) + "点伤害！\n",
                "试图攻击我方, 成功造成了" + str(damage) + "点伤害！\n",
                "虚伪的攻击，对我方造成了" + str(damage) + "点伤害！\n",
                "为什么要打爱酱？爱酱做错了什么！对我方造成了" + str(damage) + "点伤害！\n",
                "人被杀就会死。对我方造成了" + str(damage) + "点伤害！\n"
            ]
            battle_text.insert('end', text_type[rand_type])
            battle_text.see(tkinter.END)

            # 血量条的更新
            pet_attribute["生命"] = str(int(eval(pet_attribute["生命"]) - damage))
            frame1_pet_hp_short.configure(width=int((eval(pet_attribute["生命"]) / 100) * 30))
            pet_hp_now.set("HP：" + pet_attribute["生命"] + " / " + "100")

            # 我方回合到来，交互回归（5）
            def frame2_replace():
                frame2.place(x=300, y=350)
                battle_text.insert('end', "现在是你的回合！\n")
                battle_text.see(tkinter.END)
            timer_battle_atk_event_4 = threading.Timer(1, frame2_replace)
            timer_battle_atk_event_4.start()

        timer_battle_atk_event_1 = threading.Timer(1, battle_atk_event_going_1)
        timer_battle_atk_event_2 = threading.Timer(1, battle_atk_event_going_2)
        timer_battle_atk_event_3 = threading.Timer(1, battle_atk_event_going_3)
        timer_battle_atk_event_1.start()

    # 逃跑事件——————————————————————————————————————
    def battle_run_event():
        global monster_attribute_in_battle, battleMod_on_of_but_item, battleMod_on_of_but_skill

        # 关闭道具栏和技能栏
        if battleMod_on_of_but_item:
            battleMod_on_of_but_item = False
            but_item_frame.place_forget()

        if battleMod_on_of_but_skill:
            battleMod_on_of_but_skill = False
            but_skill_frame.place_forget()

        run_threshold = random.randint(0, 100)
        battle_text.insert('end', "敌人太强了，" + lab_petVal.get() + "决定战术性撤退！\n")
        battle_text.see(tkinter.END)
        frame2.place_forget()

        # 低于阈值（成功）
        if run_threshold < 80:

            def battle_run_successful():
                battle_text.insert('end', "成功脱离战场！\n")
                battle_text.see(tkinter.END)

                def battle_run_backtomain():
                    global on_battleMod
                    on_battleMod = False
                    battleMod.destroy()
                    pygame.mixer.music.stop()

                timer_battle_run_backtomain = threading.Timer(2, battle_run_backtomain)
                timer_battle_run_backtomain.start()

            timer_battle_run_successful = threading.Timer(2, battle_run_successful)
            timer_battle_run_successful.start()

        # 高于阈值（失败）
        else:
            def battle_run_unsuccessful():
                battle_text.insert('end', "对方追了上来！\n")
                battle_text.insert('end', "逃脱失败了！\n")
                battle_text.see(tkinter.END)
                timer_battle_atk_event_2.start()

            def battle_atk_event_going_2():
                global monster_attribute_in_battle
                battle_text.insert('end', "现在是敌方的回合！\n")
                battle_text.see(tkinter.END)
                timer_battle_atk_event_3.start()

            def battle_atk_event_going_3():
                global monster_attribute_in_battle
                damage = int((monster_attribute_in_battle["atk"] - eval(pet_attribute["防御"]) * 0.75) * 1.75)
                if damage < 0:
                    damage = 0
                text_type = [
                    "劲敌造成了" + str(damage) + "点伤害！\n",
                    "劲敌试图攻击敌方, 成功造成了" + str(damage) + "点伤害！\n",
                    "劲敌抓住了敌方造成了" + str(damage) + "点伤害！\n",
                ]
                rand_type = random.randint(0, len(text_type) - 1)
                battle_text.insert('end', text_type[rand_type])
                battle_text.see(tkinter.END)

                pet_attribute["生命"] = str(int(eval(pet_attribute["生命"]) - damage))
                frame1_pet_hp_short.configure(width=int((eval(pet_attribute["生命"]) / 100) * 30))
                pet_hp_now.set("HP：" + pet_attribute["生命"] + " / " + "100")

                def frame2_replace():
                    frame2.place(x=300, y=350)
                    battle_text.insert('end', "现在是你的回合！\n")
                    battle_text.see(tkinter.END)

                timer_battle_atk_event_4 = threading.Timer(1, frame2_replace)
                timer_battle_atk_event_4.start()

            timer_battle_run_unsuccessful = threading.Timer(1, battle_run_unsuccessful)
            timer_battle_atk_event_2 = threading.Timer(1, battle_atk_event_going_2)
            timer_battle_atk_event_3 = threading.Timer(1, battle_atk_event_going_3)
            timer_battle_run_unsuccessful.start()

    # 战斗中道具菜单
    def but_item_event():
        global battleMod_on_of_but_item
        if not battleMod_on_of_but_item:
            but_item_frame.place(x=210, y=310)
            battleMod_on_of_but_item = True
        else:
            but_item_frame.place_forget()
            battleMod_on_of_but_item = False

    def but_skill_event():
        global battleMod_on_of_but_skill
        if not battleMod_on_of_but_skill:
            but_skill_frame.place(x=385, y=165)
            battleMod_on_of_but_skill = True
        else:
            but_skill_frame.place_forget()
            battleMod_on_of_but_skill = False

    # fream2的按钮设定——————————————————————————————————
    but_atk = tk.Button(frame2, width=10, height=2, text='攻击', command=battle_atk_event)
    but_atk.place(x=15, y=40)
    but_skill = tk.Button(frame2, width=10, height=2, text='技能', command=but_skill_event)
    but_skill.place(x=105, y=40)
    but_item = tk.Button(frame2, width=10, height=2, text='道具', command=but_item_event)
    but_item.place(x=15, y=90)
    but_escape = tk.Button(frame2, width=10, height=2, text='逃跑', command=battle_run_event)
    but_escape.place(x=105, y=90)

    # 交互反馈——————————————————————————————————————
    frame3 = tk.Frame(battleMod, width=300, height=150, bg='black')
    battle_text = tk.Text(frame3, width=30, height=7)
    battle_text.place(x=20, y=40)
    frame3Lbl = tk.Label(frame3, width=30, height=1, bg='black', fg='yellow', text='————    战斗日志    ————')
    frame3Lbl.place(x=15, y=10)
    battle_text.insert('end', "战斗现在开始了！\n")
    pet_text.see(tkinter.END)
    battle_text.insert('end', "现在是你的回合！\n")
    pet_text.see(tkinter.END)
    frame3.place(x=0, y=350)

    but_item_frame = tk.Frame(battleMod, width=100, height=180)
    but_skill_frame = tk.Frame(battleMod, width=100, height=180)

    battleMod.mainloop()


pet_battle = tk.Button(pet_action_frame, text='战斗', bg="white", width=10, height=2, command=pet_battle_event)
pet_battle.place(x=10, y=260)
# 宠物模组用计时器————————————————————————————————————
time_pet_exp = ''


def tick_exp():
    global time_pet_exp
    time2 = time.strftime('%H:%M:%S')
    if time2 != time_pet_exp:
        time_pet_exp = time2
        pet_attribute['xp'] = str(int(pet_attribute['xp']) + 1)
        if eval(pet_attribute['xp']) >= eval(pet_attribute['等级']) * 7:
            pet_attribute['等级'] = str(int(pet_attribute['等级']) + 1)
            pet_attribute_lv.set("等级：" + pet_attribute["等级"])
    pet_frame.after(120000, tick_exp)


tick_exp()
# 计时器不区分开会有【意想得到】的冲突BUG使得某一方不作为。————————————————
time_pet_money = ''


def tick_money():
    global time_pet_money
    time2 = time.strftime('%H:%M:%S')
    if time2 != time_pet_money:
        time_pet_money = time2
        pet_attribute['金钱'] = str(int(pet_attribute['金钱']) + 1)
        pet_attribute_money.set("零花钱：" + pet_attribute["金钱"])
    pet_frame.after(120000, tick_money)


tick_money()
time_pet_hgr = ''


def tick_hgr():
    global time_pet_hgr
    time2 = time.strftime('%H:%M:%S')
    if time2 != time_pet_hgr:
        time_pet_hgr = time2
        pet_attribute['饥饿'] = str(int(pet_attribute['饥饿']) - 1)
        pet_attribute_hgr.set("饱食度：" + pet_attribute["饥饿"])
    pet_frame.after(60000, tick_hgr)


tick_hgr()
time_pet_like = ''


def tick_like():
    global time_pet_like
    time2 = time.strftime('%H:%M:%S')
    if time2 != time_pet_like:
        time_pet_like = time2
        pet_attribute['好感'] = str(int(pet_attribute['好感']) + 1)
        pet_attribute_like.set("好感度：" + pet_attribute["好感"])
    pet_frame.after(120000, tick_like)


tick_like()
time_update = ''


# 宠物属性全局的实时更新——————————————————————————————————
def tick_pet_update():
    global time_update
    time2 = time.strftime('%H:%M:%S')
    if time2 != time_pet_like:
        time_update = time2
        pet_attribute_lv.set("等级：" + pet_attribute["等级"])
        pet_attribute_life.set("生命值：" + pet_attribute["生命"] + "/100")
        pet_attribute_atk.set("攻击力：" + pet_attribute["攻击"])
        pet_attribute_def.set("防御力：" + pet_attribute["防御"])
        pet_attribute_hgr.set("饱食度：" + pet_attribute["饥饿"])
        pet_attribute_like.set("好感度：" + pet_attribute["好感"])
        pet_attribute_money.set("零花钱：" + pet_attribute["金钱"])
        pet_attribute_food.set("食物：" + pet_attribute["食物"])
        pet_attribute_suger.set("糖果：" + pet_attribute["糖果"])
        pet_attribute_bandage.set("绷带：" + pet_attribute["绷带"])
    pet_frame.after(200, tick_pet_update)


tick_pet_update()


# 时钟————————————————————————————————————————————
def tick():
    global time1
    # 从运行程序的计算机上面获取当前的系统时间
    time2 = time.strftime('%H:%M:%S')
    # 如果时间发生变化，代码自动更新显示的系统时间
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)


time1 = ''
clock = tk.Label(top, font=('times', 20, 'bold'), bg='black', fg='yellow')
clock.place(x=692, y=0)
tick()

# 随机循环播放监视器————————————————————————————————————
time_rand_play_check = ''


def rand_play_looper():
    global on_rand_play
    global time_rand_play_check
    time2 = time.strftime('%H:%M:%S')
    if on_rand_play:
        if time2 != time_rand_play_check:
            time_rand_play_check = time2
            if not pygame.mixer.music.get_busy():
                rand_play()
    top.after(1000, rand_play_looper)


rand_play_looper()
time_list_play_check = ''


def list_play_looper():
    global on_list_play_loop
    global time_list_play_check
    time2 = time.strftime('%H:%M:%S')
    if on_list_play_loop:
        if time2 != time_list_play_check:
            time_list_play_check = time2
            if not pygame.mixer.music.get_busy():
                list_play()
    top.after(1000, list_play_looper)


list_play_looper()

top.mainloop()







