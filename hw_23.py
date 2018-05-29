def chess_reward():
    num_of_corns = 1
    cell_num = 1

    while num_of_corns <= 1000000:
        num_of_corns = 2 * num_of_corns
        cell_num += 1


    return (cell_num -1, num_of_corns - 1)

print(chess_reward())




