########### 2번 미로찾기 문제 ###########
# s 1 1 1 *
# 0 0 0 1 0
# 0 1 1 1 0
# 0 0 0 0 0

# 0 1 1 1 0
# 0 0 0 1 0
# 0 1 1 1 0
# 0 0 0 0 0

# s 에서 * 까지 가는 최단경로 문제
# visited 배열과 / lev 이 핵심(몇번만에 갔는가)
from collections import deque

board = list(list(map(int, input().split())) for _ in range(4))

visited = list(([0] * 5) for _ in range(4))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited[0][0] = 0


def bfs(x, y):
    lev = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 5:
                continue
            if visited[nx][ny] != 0:
                continue
            if board[nx][ny] == 1:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            if nx == 0 and ny == 4:
                return visited[nx][ny]
    return -1


print(bfs(0, 0))
