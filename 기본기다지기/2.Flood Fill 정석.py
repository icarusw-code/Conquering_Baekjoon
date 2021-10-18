from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = ([0] * 4 for _ in range(4))
# board[0][2] = 1
# board[1][3] = 1
# board[3][1] = 1

queue = deque(0, 2)
x, y = queue.pop()
print(x, y)

# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
