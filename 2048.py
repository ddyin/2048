#!/usr/bin/env python
# coding=utf-8
import random

v = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def display(v, score):
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[0][0], v[0][1], v[0][2], v[0][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[1][0], v[1][1], v[1][2], v[1][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[2][0], v[2][1], v[2][2], v[2][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(v[3][0], v[3][1], v[3][2], v[3][3]), ' Total score:', score)


def init(v):
    for i in range(4):
        v[i] = [random.choice([0, 0, 0, 2, 2, 4]) for x in v[i]]


def align(vList, direction):
    for i in range(vList.count(0)):
        vList.remove(0)
    zeros = [0 for x in range(4-len(vList))]

    if direction == 'left':
        vList.extend(zeros)
    else:
        vList[:0] = zeros


def addSame(vList,direction):
    score = 0
    if direction == 'left':
        for i in [0, 1, 2]:
            if vList[i] == vList[i+1] != 0:
                vList[i] *= 2
                vList[i+1] = 0
                score += vList[i]
                return {'bool': True, 'score': score}
    else:
        for i in [3, 2, 1]:
            if vList[i] == vList[i - 1] != 0:
                vList[i-1] *= 2
                vList[i] = 0
                score += vList[i-1]
                return {'bool': True, 'score': score}
    return {'bool': False, 'score': score}


def handle(vList, direction):
    totalScore = 0
    align(vList, direction)
    result=addSame(vList,direction)
    while result['bool'] == True:
        totalScore += result['score']
        align(vList,direction)
        result = addSame(vList,direction)
    return totalScore


def operation(v):
    totalScore = 0
    gameOver = False
    direction = 'left'
    op = input("pls input W(上)A(左)S(下)D(右) or lowercase,operator:")
    if op in ['a', 'A']:
        # 左移
        direction = 'left'
        for row in range(4):
            totalScore+=handle(v[row], direction)
    elif op in ['d', 'D']:
        # 右移
        direction = 'right'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['w', 'W']:
        # 右移
        direction = 'left'
        for col in range(4):
            vList = [v[row][col] for row in range(4)]
            totalScore += handle(vList, direction)
            for row in range(4):
                v[row][col] = vList[row]

    elif op in ['s', 'S']:
        # 右移
        direction = 'right'
        for col in range(4):
            vList = [v[row][col] for row in range(4)]
            totalScore += handle(vList, direction)
            for row in range(4):
                v[row][col] = vList[row]

    else:
        print("invalid input,pls input W(上)A(左)S(下)D(右) or lowercase ")
        return {'gameOver': gameOver, 'score': totalScore}

    N = 0
    for q in v:
        N += q.count(0)

    if N == 0:
        gameOver = True
        return {'gameOver': gameOver, 'score': totalScore}

    num = random.choice([2, 2, 2, 4])
    k = random.randrange(1, N+1)
    n = 0
    for i in range(4):
        for j in range(4):
            if v[i][j] == 0:
                n += 1
                if n == k:
                    v[i][j] = num
                    break
    return {'gameOver': gameOver, 'score': totalScore}


init(v)
score = 0
print("pls input pls input W(上)A(左)S(下)D(右) or lowercase")
while True:
    display(v, score)
    result = operation(v)
    if result['gameOver'] == True:
        print("game over,you failed")
        print("your totalscore:",score)
    else:
        score += result['score']
        if score >= 2048:
            print("game over ,you win")
            print("your totalscore:", score)
