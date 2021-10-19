########### 1번 블룸 문제 ###########
# 0010
# 0001
# 0000
# 0100
# 일때 꽃이 다 피는 날은 몇일이 걸리는가?
from collections import deque

board = list(([0] * 4) for _ in range(4))
board[0][2] = 1
board[1][3] = 1
board[3][1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((3, 1))
    queue.append((0, 2))
    queue.append((1, 3))

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < 4) and (0 <= ny < 4) and board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))
                    result = board[nx][ny]
    return result


print(bfs())
