class Solution:
    # # [题解]1. O(n^2)(n为blocked个数) t:228ms(92%) m:162M(100%) 双向BFS+hash
    # def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    #     d, u, n, base = 0, int(1e6), len(blocked), 131 # base根据题目范围凑一个
    #     block = {p[0] * base + p[1] for p in blocked} # hash
    #     limit = n * (n-1) // 2
    #     def check(a, b):
    #         vis = {a[0] * base + a[1]}
    #         du = deque([a])
    #         while len(du) and len(vis) <= limit:
    #             x, y = du.popleft()
    #             if x == b[0] and y == b[1]: 
    #                 return True
    #             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #                 nx, ny = x + dx, y + dy
    #                 if nx < d or nx >= u or ny < d or ny >= u:
    #                     continue
    #                 h = nx * base + ny
    #                 if h in vis or h in block:
    #                     continue
    #                 du.append((nx, ny))
    #                 vis.add(h)
    #         return len(vis) > limit
        
    #     return check(source, target) and check(target, source)

    # [题解]2. O(n^2) t:324ms(47.2%) m:16.3M(95.2%) 压缩+BFS
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:
            return True
            
        BOUNDARY = 10**6

        # 离散化
        rows = sorted(set(pos[0] for pos in blocked) | {source[0], target[0]})
        columns = sorted(set(pos[1] for pos in blocked) | {source[1], target[1]})
        r_mapping, c_mapping = dict(), dict()
        

        r_id = (0 if rows[0] == 0 else 1)
        r_mapping[rows[0]] = r_id
        for i in range(1, len(rows)):
            r_id += (1 if rows[i] == rows[i - 1] + 1 else 2)
            r_mapping[rows[i]] = r_id
        if rows[-1] != BOUNDARY - 1:
            r_id += 1

        c_id = (0 if columns[0] == 0 else 1)
        c_mapping[columns[0]] = c_id
        for i in range(1, len(columns)):
            c_id += (1 if columns[i] == columns[i - 1] + 1 else 2)
            c_mapping[columns[i]] = c_id
        if columns[-1] != BOUNDARY - 1:
            c_id += 1
        print(c_id+1, r_id+1)
        grid = [[0] * (c_id + 1) for _ in range(r_id + 1)]
        for x, y in blocked:
            grid[r_mapping[x]][c_mapping[y]] = 1
        
        sx, sy = r_mapping[source[0]], c_mapping[source[1]]
        tx, ty = r_mapping[target[0]], c_mapping[target[1]]

        q = deque([(sx, sy)])
        grid[sx][sy] = 1
        while q:
            x, y = q.popleft()
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx <= r_id and 0 <= ny <= c_id and grid[nx][ny] != 1:
                    if (nx, ny) == (tx, ty):
                        return True
                    q.append((nx, ny))
                    grid[nx][ny] = 1
        
        return False
