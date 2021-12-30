# Local files.
from utils.pickle_read import *
from handlers.check_new import *
from test import TestYoutubeLiker
from automatization.likes import YoutubeLiker

# Libraries.
import os
from time import sleep
from random import choice

tyl = TestYoutubeLiker()


def read_comments():
    with open('files/t_comments.txt', 'r') as first:
        f = choice(first.read().split('\n'))
    with open('files/s_comments.txt', 'r') as second:
        s = choice(second.read().split('\n'))
    with open('files/t_comments.txt', 'r') as third:
        t = choice(third.read().split('\n'))
    return [f, s, t]


def read_channels():
    with open('files/the_first_channel.txt', 'r') as first:
        f = first.read().split('\n')
    with open('files/the_second_channel.txt', 'r') as second:
        s = second.read().split('\n')
    with open('files/the_third_channel.txt', 'r') as third:
        t = third.read().split('\n')
    return [f, s, t]


def main(url: str, num_of_account):
    try:
        ca = CheckAvailability(url)
        ca.pars_the_last_video()
        compared_video = ca.compare_id()
        if compared_video == 'NEW_VIDEO':
            print('New video')
            print(ca.video_id)
            tyl.start_work(ca.video_id, read_comments()[num_of_account], num_of_account)
            print('Video was commented. ')
        elif compared_video == 'OLD_VIDEO':
            print(read_comments()[num_of_account])
            print('OLD')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    print(os.getcwd())
    while True:
        channels_list = read_channels()
        for i in range(len(channels_list)):
            for j in range(len(channels_list[i])):
                main(channels_list[i][j], i)
            sleep(10)
        sleep(600)
