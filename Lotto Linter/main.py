""" Lotto Linter Ver: 1.0
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.23-1049 """


import tkinter
import urllib.request
import pandas as pd


# VARS
version = 1.0


def get_nums():
    mega_millions_url = 'https://www.texaslottery.com/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv'
    power_ball_url = 'https://www.texaslottery.com/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv'
    urllib.request.urlretrieve(mega_millions_url, 'data/mm2022.csv')
    urllib.request.urlretrieve(power_ball_url, 'data/pb2022.csv')
    mega_millions_data = pd.read_csv('data/mm2022.csv')
    power_ball_data = pd.read_csv('data/pb2022.csv')
    header_list = ['Lotto', 'Month', 'Day', 'Year', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'MegaPower', 'Multiply']
    mega_millions_data.to_csv('data/mm2022.csv', header=header_list, index=False)
    power_ball_data.to_csv('data/pb2022.csv', header=header_list, index=False)
    mega_millions = pd.read_csv('data/mm2022.csv')
    power_ball = pd.read_csv('data/pb2022.csv')

    mega_list = []
    power_list = []

    fetch = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'MegaPower']
    for item in fetch:
        pick = mega_millions[item].mode().iloc[0]
        mega_list.append(pick)

    for item in fetch:
        pick = power_ball[item].mode().iloc[0]
        power_list.append(pick)

    mega_label['text'] = f'Mega Millions: {mega_list}'
    power_label['text'] = f'Power Ball: {power_list}'


# Display
display = tkinter.Tk()
display.title(f'Lotto Linter {version}')
display.configure(bg='black')
display.minsize(width=600, height=200)
mega_label = tkinter.Label(text='Mega Millions!', font=('Arial', 24, 'bold'), bg='black', fg='teal')
power_label = tkinter.Label(text='Power Ball', font=('Arial', 24, 'bold'), bg='black', fg='teal')
magic_button = tkinter.Button(text='Got dem nums?', command=get_nums, bg='black', fg='purple', font=('Arial', 24, 'bold'))
mega_label.pack()
power_label.pack()
magic_button.pack()


display.mainloop()
