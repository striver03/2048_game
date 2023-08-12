from collections import deque

def initialize(len = 4):
    global score, listWithZeroes, moves_stack
    score = 0
    moves_stack = deque()
    listWithZeroes = []
    for i in range(len):
        for j in range(len):
            listWithZeroes.append([i,j])