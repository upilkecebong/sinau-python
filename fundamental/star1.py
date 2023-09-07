for i in range(5):
    for j in range(5):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()