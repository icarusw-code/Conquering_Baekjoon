########### 3번 한지점 부터 B지점까지 최소거리 문제 ###########

# 0 0 1 1
# 0 0 1 1
# 0 0 0 0
# s 0 0 0

# s 부터 1번 섬까지 최소 거리(4)
from collections import deque

borad = list(list(map(int, input().split())) for _ in range(4))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * 4 for _ in range(4)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            if visited[nx][ny] != 0:
                continue
            if borad[nx][ny] == 1:
                print(visited)
                return visited[nx - 1][ny - 1]

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))


print(bfs(3, 0))
