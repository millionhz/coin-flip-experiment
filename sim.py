from random import randint

subjects = ({'id': randint(100000, 999999), 'flips': []}
            for x in range(10000))
standing = [subject for subject in subjects]
sitting = []


def sit_stand(standing):
    dic = standing.copy()
    for x in dic:
        if 0 in x['flips'][:-1]:
            print('ANOMALY')
        if x.get('flips')[-1] == 0:
            sitting.append(x)
            standing.remove(x)


while len(standing) != 1:
    for x in standing:
        x['flips'].append(randint(0, 1))
    sit_stand(standing)
print(sitting[-2])
print(sitting[-1])
print()
print(standing)
