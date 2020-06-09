from random import randint

print('Initializing....')
subjects = ({'id': randint(100000, 999999), 'flips': []}
            for x in range(10000))
standing = [subject for subject in subjects]
#sitting = []
round = 0
print('Initialized')


def sit_stand(standing):
    global subjects_lost
    subjects_lost = 0
    dic = iter(standing.copy())
    for x in dic:
        if 0 in x['flips'][:-1]:
            print('ANOMALY')
        if x.get('flips')[-1] == 0:
            #print(f'{x["id"]} lost')
            subjects_lost += 1
            # sitting.append(x)
            standing.remove(x)


while len(standing) > 1:
    round += 1
    for x in standing:
        #print(f'Processing {x.get("id")}...')
        x['flips'].append(randint(0, 1))
    print('Coins Flipped!')
    r1p = len(standing)
    sit_stand(standing)
    print(f'Round {round} over!')
    print(f'Out of {r1p}; {subjects_lost} subjects lost in this round...')
    try:
        print(f'Loss Ratio {(subjects_lost/r1p *100)}%\n')
    except:
        break

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
