from random import randint

# limit = 5000000

print('Initializing....')
# subjects = ({'id': randint(100000, 999999), 'flips': []}
#             for x in range(100000000))
# standing = [subject for subject in subjects]
standing = [{'id': randint(100000, 999999), 'flips': []}
            for x in range(5000000)]
sitting = []
round = 0
print('Initialized')


def sit_stand():
    global subjects_lost
    global standing
    global sitting
    subjects_lost = 0
    win = []
    lost = []
    for x in standing:
        if 0 in x['flips'][:-1]:
            print('ANOMALY')
        if x.get('flips')[-1] == 0:
            # print(f'{x["id"]} lost')
            subjects_lost += 1
            lost.append(x)
        else:
            win.append(x)
    standing = [x for x in win]
    sitting.extend(lost)


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
print(standing)
try:
    print(
        f'{standing[-1]["id"]} flipped heads {len(standing[-1]["flips"])} times \n')
except:
    pass
