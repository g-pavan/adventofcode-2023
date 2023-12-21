def step_counter(matrix, start, steps):
    ans = 0
    curr_step = 0
    queue = [(start[0], start[1], curr_step)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while(len(queue) != 0):

        # print(f"Level {curr_step} my queue is {queue}")
        i,j, curr_step = queue.pop(0)
        if(curr_step % 2 == 0):
            ans += 1
            # ans_values.append((i,j))

        curr_step += 1
        matrix[i][j] = '#'

        for k in range(4):
            new_x = i + dx[k]
            new_y = j + dy[k]

            if((0 <= new_x < len(matrix)) and (0 <= new_y < len(matrix[0])) and (matrix[new_x][new_y] == '.') and (curr_step <= steps)):
                matrix[new_x][new_y] = '#'
                queue.append((new_x, new_y, curr_step))
        
        
        
    
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
        
    
    ans = step_counter(matrix, start, steps=64)

    print(ans)