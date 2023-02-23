def find_max(user_list):
    maxi = 0
    for every in user_list:
        if every > maxi:
            maxi = every
    return int(maxi)
