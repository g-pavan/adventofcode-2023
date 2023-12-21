def add_to_dict(hashmap, key, value):
    if key in hashmap:
        hashmap[key].append(value)
    else:
        hashmap[key] = [value]
    
    return hashmap

def check(hashmap, key, value):
    if key not in hashmap:
        return False

    return not(value in hashmap[key])

def step_counter(matrix, start, steps):
    ans = 0
    curr_step = 0

    m = len(matrix)
    n = len(matrix[0])

    dim_x = 0
    dim_y = 0
    queue = [(start[0], start[1], curr_step, dim_x, dim_y)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x_dict = {}
    y_dict = {}

    while(len(queue) != 0):

        print(f"Level {curr_step} my queue is {queue}")
        i,j, curr_step, dim_x, dim_y = queue.pop(0)

        x_dict = add_to_dict(x_dict, dim_x, i)
        y_dict = add_to_dict(y_dict, dim_y, j)

        if(curr_step % 2 == 0):
            ans += 1
            # ans_values.append((i,j))

        curr_step += 1
        print(x_dict, y_dict)

        for k in range(4):
            new_x = i + dx[k]
            new_y = j + dy[k]
            new_x_dim = new_x // m
            new_y_dim = new_y // n

            new_x %= m
            new_y %= n

            print(x_dict, new_x_dim, new_x, check(x_dict, new_x_dim, new_x))
            if((0 <= new_x < m) and (0 <= new_y < n) and (matrix[new_x][new_y] == '.') and (curr_step <= steps) and (check(x_dict, new_x_dim, new_x) and check(y_dict, new_y_dim, new_y))):
                x_dict = add_to_dict(x_dict, dim_x, i)
                y_dict = add_to_dict(y_dict, dim_y, j)
                queue.append((new_x, new_y, curr_step, new_x_dim, new_y_dim))
        
        
        
    
    # while(len(queue) != 0):
    #     i,j, reached = queue.pop(0)
    #     if(reached % 2 == 0):
    #         ans += 1
    #         ans_values.append((i,j))

    # print(ans_values)
    return ans

if __name__ == "__main__":
    matrix = []
    with open('input.txt', 'r') as f:
        while True:
            line = f.readline()

            if not line:
                break
                
            line = line.strip()
            matrix.append(list(line))
    
    start = [0,0]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 'S'):
                start = [i, j]
                break
        
    
    ans = step_counter(matrix, start, steps=6)

    print(ans)