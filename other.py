import time
import pygame
def bofang(hour, name ,yinliang): #报时播放
    hours = str(hour)
    if hour < 10:
        path = name + "/0" + hours + ".mp3"
    elif hour == 24:
        path = name + "/0" + '0' + ".mp3"

    else:
        path = name + "/" + hours + ".mp3"

    print(path)
    pygame.mixer.init()

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(yinliang)

name = 'xiang'
yinliang =  0.50
flag = 1
while flag:
    passtime = time.localtime(time.time())
    # print(passtime)
    # 开始时间
    # print(passtime.tm_hour, passtime.tm_min, passtime.tm_sec)
    # 时 分 秒
    cha = (59 - passtime.tm_min) * 60 + 60 - passtime.tm_sec
    print(cha)
    time.sleep(5)
    bofang(passtime.tm_hour + 1, name, yinliang)