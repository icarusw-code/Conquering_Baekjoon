from collections import deque

# 2번 미로 찾기
# board = list(list(map(int, input().split())) for _ in range(4))

# visited = list([0] * 5 for _ in range(4))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if (
#                 (0 <= nx < 4)
#                 and (0 <= ny < 5)
#                 and visited[nx][ny] == 0
#                 and board[nx][ny] != 1
#             ):
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx, ny))

#             if nx == 0 and ny == 4:
#                 return visited[nx][ny]
#     return -1


# print(bfs(0, 0))

# board = list((list(map, input().split())) for _ in range(4))

# visited = [[0] * 4 for _ in range(4)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] == 0:
#                 if board[nx][ny] == 1:
#                     return visited[nx - 1][ny - 1]

#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx, ny))


# print(bfs(3,0))

board = list(list(map(int, input().split())) for _ in range(4))

visited = [[0] * 5 for _ in range(4)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 섬의 개수 -> bfs 수행 횟수
cnt = 0
# 섬의 크기 -> bfs 했을때 큐의 크기
size_list = []


def bfs(x, y):
    global size
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        size += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < 4
                and 0 <= ny < 5
                and board[nx][ny] != 0
                and visited[nx][ny] != 0
            ):
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
