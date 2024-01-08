#代码原文
#https://blog.csdn.net/weixin_44351032/article/details/132627167?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-132627167-blog-128551130.235%5Ev39%5Epc_relevant_anti_vip&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-132627167-blog-128551130.235%5Ev39%5Epc_relevant_anti_vip&utm_relevant_index=5
#谱
#https://www.bilibili.com/read/cv20800994/
#安装pygame
#https://blog.csdn.net/liuboxx1/article/details/79570351
import os
import threading
import time

import mido
import pygame

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)


def play_midi(file):
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 1024
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(1)
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
    except:
        import traceback
        print(traceback.format_exc())
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)


KEY = 1
neg_SPEED = 1.2  # 数值越小速度越快


# bpm = \frac{60000000}{tempo}
def music(note, base_num, base_time):
    base_num, base_time = base_num + KEY, base_time * neg_SPEED
    # mid = mido.MidiFile()
    # track = mido.MidiTrack()
    # mid.tracks.append(track)
    # meta_time = 60 * 60 * 10 / bpm
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(mido.Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:note]), velocity=96, time=0,
                              channel=1))
    track.append(mido.Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:note]), velocity=96,
                              time=int(480 * base_time), channel=1))
    # print('正在合成(',note, base_num, base_time,')音')
    # track.append(mido.Message('note_on', note=base_note, velocity=96, time=0))
    # track.append(mido.Message('note_off', note=base_note, velocity=96, time=480*base_time))
    # mid.save('1.mid')
    # play_midi('1.mid')


def lemon_music():
    a = 0
    b = 1
    # 前奏
    # music(1, a+b + 1, 2)

#50
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(6, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)

    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(6, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)

#51
    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(5, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)

    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(5, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)

#52
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

#51
    music(7, a + 0, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(5, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)

    music(7, a + 0, 0.5-0.01)
    music(6, a + 0, 0.5-0.01)
    music(7, a + 0, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(7, a + 0, 0.5-0.01)
    music(6, a + 0, 0.5-0.01)

#52
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(6, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)

    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(6, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)

    # 51
    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(5, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)

    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(5, a + 1, 0.5-0.01)
    music(3, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)

    # 52
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(7, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

    music(5, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(7, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

#51
    music(7, a + 0, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(7, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)

    music(5, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)
    music(7, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)

#第三行
#52
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(6, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)

    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(6, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)

#52
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)

    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)

#52
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

    #52
    music(7, a + 0, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(5, a + 1, 0.5-0.02)
    music(2, a + 1, 0.5-0.02)
    music(1, a + 1, 0.5-0.02)

    music(7, a + 0, 0.5-0.02)
    music(6, a + 0, 0.5-0.02)
    music(7, a + 0, 0.5-0.02)
    music(3, a + 1, 0.5-0.02)
    music(7, a + 0, 0.5-0.02)
    music(6, a + 0, 0.5-0.02)

#第四行
#53

    music(3, a + 1, 0.5-0.03)
    music(2, a + 1, 0.5-0.03)
    music(3, a + 1, 0.5-0.03)
    music(6, a + 1, 0.5-0.03)
    music(3, a + 1, 0.5-0.03)
    music(2, a + 1, 0.5-0.03)

    music(3, a + 1, 0.5-0.03)
    music(2, a + 1, 0.5-0.03)
    music(3, a + 1, 0.5-0.03)
    music(6, a + 1, 0.5-0.03)
    music(3, a + 1, 0.5-0.03)
    music(2, a + 1, 0.5-0.03)

    # 52
    music(3, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)
    music(3, a + 1, 0.5 - 0.02)
    music(5, a + 1, 0.5 - 0.02)
    music(3, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)

    music(3, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)
    music(3, a + 1, 0.5 - 0.02)
    music(5, a + 1, 0.5 - 0.02)
    music(3, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)

    # 52
    music(2, a + 1, 0.5 - 0.02)
    music(1, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)
    music(7, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)
    music(1, a + 1, 0.5 - 0.02)

    music(5, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)
    music(1, a + 1, 0.5 - 0.02)
    music(7, a + 1, 0.5 - 0.02)
    music(2, a + 1, 0.5 - 0.02)
    music(1, a + 1, 0.5 - 0.02)

#51
    music(7, a + 0, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(7, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)

    music(5, a + 1, 0.5-0.01)
    music(2, a + 1, 0.5-0.01)
    music(1, a + 1, 0.5-0.01)
    music(7, a + 1, 0.5-0.01+0.25)

    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480 * 1))

#主歌部分
    #100
    music(2, a + 0, 0.5)
    music(3, a + 0, 0.5)
    music(2, a + 0, 0.5)
    music(6, a - 1, 0.5)
    music(2, a + 0, 2)

    music(0, a + 0, 1)
    music(2, a + 0, 0.5)
    music(3, a + 0, 0.5)
    music(2, a + 0, 0.5)
    music(3, a + 0, 0.5)
    music(5, a + 0, 0.5)
    music(3, a + 0, 0.5)

    music(2, a + 0, 0.5)
    music(3, a + 0, 0.5)
    music(2, a + 0, 0.5)
    music(6, a - 1, 0.5)
    music(1, a + 0, 2)

    music(0, a + 0, 1)
    music(1, a + 1, 1)
    music(7, a + 0, 0.5)
    music(5, a + 0, 0.5)
    music(3, a + 0, 1)

    music(2, a + 0, 0.5)
    music(3, a + 0, 0.5)
    music(2, a + 0, 0.5)
    music(6, a - 1, 0.5)
    music(2, a + 0, 2)

    #99
    music(0, a + 0, 1 + 0.01)
    music(2, a + 0, 0.5 + 0.01)
    music(3, a + 0, 0.5 + 0.01)
    music(2, a + 0, 0.5 + 0.01)
    music(3, a + 0, 0.5 + 0.01)
    music(5, a + 0, 0.5 + 0.01)
    music(3, a + 0, 0.5 + 0.01)

    music(2, a + 0, 0.5 + 0.01)
    music(3, a + 0, 0.5 + 0.01)
    music(2, a + 0, 0.5 + 0.01)
    music(1, a + 0, 0.5 + 0.01)
    music(6, a - 1, 4 + 0.01)
    music(0, a + 0, 1 + 0.01)
    music(0, a + 0, 1 + 0.01)

    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(6, a + 0, 0.5 + 0.01)
    music(2, a + 1, 2 + 0.01)

    music(0, a + 0, 1 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(5, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)

    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(6, a + 0, 0.5 + 0.01)
    music(1, a + 1, 2 + 0.01)

    music(0, a + 0, 1 + 0.01)
    music(1, a + 2, 1 + 0.01)
    music(7, a + 1, 0.5 + 0.01)
    music(5, a + 1, 0.5 + 0.01)
    music(3, a + 1, 1 + 0.01)

    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(6, a + 0, 0.5 + 0.01)
    music(2, a + 1, 2 + 0.01)

    music(0, a + 0, 1 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(5, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)

    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(1, a + 1, 0.5 + 0.01)
    music(6, a + 0, 4 + 0.01)
    music(0, a + 0, 1 + 0.01)
    music(0, a + 0, 1 + 0.01)

    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(6, a + 0, 0.5 + 0.01)
    music(2, a + 1, 2 + 0.01)

    music(0, a + 0, 1 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(2, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)
    music(5, a + 1, 0.5 + 0.01)
    music(3, a + 1, 0.5 + 0.01)

    #98
    music(2, a + 1, 0.5 + 0.02)
    music(3, a + 1, 0.5 + 0.02)
    music(2, a + 1, 0.5 + 0.02)
    music(6, a + 0, 0.5 + 0.02)
    music(1, a + 1, 2 + 0.02)

    music(0, a + 0, 1 + 0.02)
    music(1, a + 2, 1 + 0.02)
    music(7, a + 1, 0.5 + 0.02)
    music(5, a + 1, 0.5 + 0.02)
    music(3, a + 1, 1 + 0.02)

    music(2, a + 1, 0.5 + 0.02)
    music(3, a + 1, 0.5 + 0.02)
    music(2, a + 1, 0.5 + 0.02)
    music(6, a + 0, 0.5 + 0.02)
    music(2, a + 1, 2 + 0.02)

#97
    music(0, a + 0, 1 + 0.03)
    music(2, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)
    music(2, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)
    music(5, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)

    music(2, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)
    music(2, a + 1, 0.5 + 0.03)
    music(1, a + 1, 0.5 + 0.03)
    music(6, a + 0, 2 + 0.03)

    music(0, a + 0, 1 + 0.03)
    music(0, a + 0, 1 + 0.03)
    music(7, a - 1, 1 + 0.03)
    music(1, a + 0, 1 + 0.03)

    #主歌第五行
    #97
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 0.5 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 1 + 0.03)
    music(6, a + 0, 1 + 0.03)
    music(6, a + 0, 1 + 0.03)#连音

    music(5, a + 0, 0.5 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 1 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 0.5 + 0.03)
    music(6, a + 0, 0.5 + 0.03)

    music(3, a + 0, 0.5 + 0.03)
    music(2, a + 0, 0.5 + 0.03)
    music(3, a + 0, 0.5 + 0.03)
    music(2, a + 0, 1 + 0.03)
    music(3, a + 0, 1 + 0.03)
    music(3, a + 0, 1 + 0.03)#连音

    music(2, a + 0, 0.5 + 0.03)
    music(3, a + 0, 0.5 + 0.03)
    music(2, a + 0, 1 + 0.03)
    music(0, a + 0, 0.5 + 0.03)
    music(3, a + 0, 0.5 + 0.03)
    music(4, a + 0, 0.5 + 0.03)

    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 0.5 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 1 + 0.03)
    music(6, a + 0, 1 + 0.03)
    music(6, a + 0, 1 + 0.03)#连音

    music(5, a + 0, 0.5 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 1 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(5, a + 0, 0.5 + 0.03)
    music(4, a + 0, 0.5 + 0.03)

    music(3, a + 0, 0.5 + 0.03)
    music(2, a + 0, 0.5 + 0.03)
    music(3, a + 0, 0.5 + 0.03)
    music(6, a + 0, 1 + 0.03)
    music(3, a + 0, 1 + 0.03)
    music(3, a + 0, 1 + 0.03)#连音

    music(2, a + 0, 0.5 + 0.03)
    music(3, a + 0, 0.5 + 0.03)#升高半音做不到
    music(5, a + 0, 2.5 + 0.03)

    music(2, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)
    music(2, a + 1, 0.5 + 0.03)
    music(6, a + 0, 0.5 + 0.03)
    music(2, a + 1, 2 + 0.03)


    music(0, a + 0, 1 + 0.03)
    music(2, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)
    music(2, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)
    music(5, a + 1, 0.5 + 0.03)
    music(3, a + 1, 0.5 + 0.03)


    #100
    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(6, a + 0, 0.5)
    music(1, a + 1, 2 )

    music(0, a + 0, 1 )
    music(1, a + 2, 1 )
    music(7, a + 1, 0.5 )
    music(5, a + 1, 0.5 )
    music(3, a + 1, 1 )

    music(2, a + 1, 0.5 )
    music(3, a + 1, 0.5 )
    music(2, a + 1, 0.5 )
    music(6, a + 0, 0.5 )
    music(2, a + 1, 2 )

    music(0, a + 0, 1 )
    music(2, a + 1, 0.5 )
    music(3, a + 1, 0.5 )
    music(2, a + 1, 0.5 )
    music(3, a + 1, 0.5 )
    music(5, a + 1, 0.5 )
    music(3, a + 1, 0.5 )


    #101
    music(2, a + 1, 0.5 -0.01)
    music(3, a + 1, 0.5 -0.01)
    music(2, a + 1, 0.5 -0.01)
    music(1, a + 1, 0.5 -0.01)
    music(6, a + 0, 2 -0.01)

#100
    music(2, a + 1, 0.5)
    music(7, a + 0, 0.5)
    music(1, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(7, a + 0, 0.5)
    music(1, a + 1, 0.5)
    music(7, a + 0, 0.5)


    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(6, a + 0, 0.5)
    music(2, a + 1, 2)

    music(0, a + 0, 1)
    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(5, a + 1, 0.5)
    music(3, a + 1, 0.5)

    music(2, a + 1, 0.5)
    music(3, a + 1, 0.5)
    music(2, a + 1, 0.5)
    music(6, a + 0, 0.5)
    music(1, a + 1, 2)

    music(0, a + 0, 1 )
    music(1, a + 2, 1 )
    music(7, a + 1, 0.5 )
    music(5, a + 1, 0.5 )
    music(3, a + 1, 1 )

    music(2, a + 1, 0.5 )
    music(3, a + 1, 0.5 )
    music(2, a + 1, 0.5 )
    music(6, a + 0, 0.5 )
    music(2, a + 1, 2 )

#98
    music(0, a + 0, 1 + 0.02)
    music(2, a + 1, 0.5 + 0.02)
    music(3, a + 1, 0.5 + 0.02)
    music(2, a + 1, 0.5 + 0.02)
    music(3, a + 1, 0.5 + 0.02)
    music(5, a + 1, 0.5 + 0.02)
    music(3, a + 1, 0.5 + 0.02)

    music(2, a + 1, 0.5 + 0.02)
    music(3, a + 1, 0.5 + 0.02)
    music(2, a + 1, 0.5 + 0.02)
    music(1, a + 1, 0.5 + 0.02)
    music(6, a + 0, 1 + 0.02)
    music(1, a + 1, 0.5 + 0.02)
    music(1, a + 1, 0.5 + 0.02)

# #108
    music(5, a + 0, 1.5 -0.08)
#     music(5, a + 0, 0.5 -0.08)
#     music(5, a + 0, 1 -0.08)
#     music(3, a + 0, 0.5 -0.08)
#     music(3, a + 0, 0.5 -0.08)
#
#     music(3, a + 0, 1 -0.08)

lemon_music()
mid.save('a2.mid')


def play():
    play_midi('a2.mid')


# def show():
#     for i in f.readlines():
#         print("\033[0;34;40m%s\033[0m" % i)
#         time.sleep(len(i) / 3)
#         os.system('cls')


if __name__ == '__main__':
    # f = open('lyrics.txt', 'r', encoding='utf-8')
    t1 = threading.Thread(target=play)
    # t2 = threading.Thread(target=show)
    t1.start()
    # t2.start()
    # os.remove('a2.mid')