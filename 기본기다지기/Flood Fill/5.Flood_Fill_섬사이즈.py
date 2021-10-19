########### 5번 섬의 개수와 크기 구하기 문제 ###########
########### BOJ 2667 단지번호 붙히기 풀어보기 ##########

# BFS 를 돌려 섬이 있으면 맵에서 제거 하는게 핵심 아이디어
# BFS 횟수 : 섬의 개수
# BFS 했을때 큐의 크기: 섬의 크기

# 0 1 1 1 0
# 0 0 0 1 0
# 0 0 1 0 0
# 0 1 1 0 0


from collections import deque

board = list(list(map(int, input().split())) for _ in range(4))
visited = list([0] * 5 for _ in range(4))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 섬의 개수
cnt = 0
# 각 섬의 크기
size_list = []


def bfs(x, y):
    global size
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        print(x, y)
        size += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 5:
                continue
            if board[nx][ny] == 0:
                continue
            if visited[nx][ny] == 1:
                continue
            board[nx][ny] = 0
            queue.append((nx, ny))

    return size


for j in range(4):
    for i in range(5):
        if board[j][i] == 1:
            size = 0
            tmp = bfs(j, i)
            size_list.append(tmp)
            cnt += 1

print(cnt)
print(size_list)
