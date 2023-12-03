#自動問答程式
from question import ss

test = [
    "6*5=?\n(a) 24\n(b) 30\n(c) 48\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 1000\n(c) 100\n",
    "香蕉是什麼顏色?\n(a) 黃色\n(b) 紅色\n(c) 黑色\n"
]

questions = [
    ss(test[0],"b"),
    ss(test[1],"c"),
    ss(test[2],"a")
]

def run_test(question):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1

    print('你得到'+ str(score)+ '分，共'+ str(len(questions))+ '題')


run_test(questions)