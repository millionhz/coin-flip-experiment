from random import randint

# *limit = 10000000
# *max memory usage = 2000MB
# https://www.youtube.com/watch?v=uTChrirK-hw&t=373s
# the lost and sitting array and is commented out
# as right now there is no real necessity to store that
# info in memory
print('\nInitializing....')
# subjects = ({'id': randint(100000, 999999), 'flips': []}
#             for x in range(100000000))
# standing = [subject for subject in subjects]
# "".join(sample(f"{ascii_letters}{digits}=_",9))
standing = [{'id': x, 'flips': []}
            for x in range(10000000)]
#sitting = []
round = 0
print('Initialized \n')


def sit_stand():
    global subjects_lost
    global standing
    #global sitting
    # subjects_lost is declared inside the function
    # as it need to be reset everytime the function
    # run and it also need to be accessable outside
    # the function
    subjects_lost = 0
    win = []
    #lost = []
    for x in standing:
        if 0 in x['flips'][:-1]:
            print('ANOMALY')
        if x.get('flips')[-1] == 0:
            # print(f'{x["id"]} lost')
            subjects_lost += 1
            # lost.append(x)
        else:
            win.append(x)
    standing = win.copy()
    # sitting.extend(lost)


while len(standing) > 1:
    round += 1
    for x in standing:
        # print(f'Processing {x.get("id")}...')
        x['flips'].append(randint(0, 1))
    r1p = len(standing)
    sit_stand()
    print(f'Round {round} over!')
    print(f'Out of {r1p}; {subjects_lost} subjects lost in this round...')
    try:
        print(
            f'{r1p-subjects_lost} many people flipped heads {len(standing[0]["flips"])} time/s')
    except:
        pass
    try:
        print(f'Loss Ratio {(subjects_lost/r1p *100)}%\n')
    except:
        pass
# print()
# print(sitting)
print()
standing = list(standing)
print(standing, "\n")
try:
    print(
        f'{standing[-1]["id"]} flipped heads {len(standing[-1]["flips"])} times \n')
except:
    pass

input('Press Enter To Exit...')
