'''

a3 = false
| a10 = false: c0 (11.0/1.0)
| a10 = true
| | a2 = false
| | | a13 = false: c3 (12.0)
| | | a13 = true
| | | | a0 = false: c0 (2.0)
| | | | a0 = true: c3 (2.0)
| | a2 = true: c0 (7.0/2.0)
a3 = true
| a0 = false
| | a8 = false: c1 (12.0)
| | a8 = true
| | | a10 = false: c0 (5.0)
| | | a10 = true: c1 (4.0)
| a0 = true
| | a10 = false
| | | a8 = false
| | | | a4 = false: c2 (6.0/1.0)
| | | | a4 = true: c3 (2.0)
| | | a8 = true: c0 (7.0)
| | a10 = true
| | | a5 = false: c1 (5.0)
| | | a5 = true
| | | | a6 = false: c0 (7.0/2.0)
| | | | a6 = true: c3 (3.0)

Prolog Rules: (hand written)

is_accuator_activated(a3, false),
is_accuator_activated(a10, false) :- move(rover, forward).

is_accuator_activated(a3, false),
is_accuator_activated(a10, true),
is_accuator_activated(a2, true) :- move(rover, forward).

is_accuator_activated(a3, false),
is_accuator_activated(a10, true),
is_accuator_activated(a2, false),
is_accuator_activated(a13, false) :- move(rover, backward).

is_accuator_activated(a3, false),
is_accuator_activated(a10, true),
is_accuator_activated(a2, false),
is_accuator_activated(a13, true),
is_accuator_activated(a0, false) :- move(rover, forward).

is_accuator_activated(a3, false),
is_accuator_activated(a10, true),
is_accuator_activated(a2, false),
is_accuator_activated(a13, true),
is_accuator_activated(a0, true) :- move(rover, backward).

is_accuator_activated(a3, true),
is_accuator_activated(a0, false),
is_accuator_activated(a8, false) :- move(rover, left).

is_accuator_activated(a3, true),
is_accuator_activated(a0, false),
is_accuator_activated(a8, true),
is_accuator_activated(a10, false) :- move(rover, forward).

is_accuator_activated(a3, true),
is_accuator_activated(a0, false),
is_accuator_activated(a8, true),
is_accuator_activated(a10, true) :- move(rover, left).

is_accuator_activated(a3, true),
is_accuator_activated(a0, true),
is_accuator_activated(a10, false),
is_accuator_activated(a8, false),
is_accuator_activated(a4, false):- move(rover, right).

is_accuator_activated(a3, true),
is_accuator_activated(a0, true),
is_accuator_activated(a10, false),
is_accuator_activated(a8, false),
is_accuator_activated(a4, true):- move(rover, backward).

is_accuator_activated(a3, true),
is_accuator_activated(a0, true),
is_accuator_activated(a10, false),
is_accuator_activated(a8, true) :- move(rover, forward).

is_accuator_activated(a3, true),
is_accuator_activated(a0, true),
is_accuator_activated(a10, true),
is_accuator_activated(a5, false) :- move(rover, left).

is_accuator_activated(a3, true),
is_accuator_activated(a0, true),
is_accuator_activated(a10, true),
is_accuator_activated(a5, true),
is_accuator_activated(a6, false):- move(rover, forward).

is_accuator_activated(a3, true),
is_accuator_activated(a0, true),
is_accuator_activated(a10, true),
is_accuator_activated(a5, true),
is_accuator_activated(a6, true) :- move(rover, backward).

'''

import pandas as pd
df = pd.read_csv('second.csv')

decision_tree_for_prolog = '''a3 = false
| a10 = false: c0 (11.0/1.0)
| a10 = true
| | a2 = false
| | | a13 = false: c3 (12.0)
| | | a13 = true
| | | | a0 = false: c0 (2.0)
| | | | a0 = true: c3 (2.0)
| | a2 = true: c0 (7.0/2.0)
a3 = true
| a0 = false
| | a8 = false: c1 (12.0)
| | a8 = true
| | | a10 = false: c0 (5.0)
| | | a10 = true: c1 (4.0)
| a0 = true
| | a10 = false
| | | a8 = false
| | | | a4 = false: c2 (6.0/1.0)
| | | | a4 = true: c3 (2.0)
| | | a8 = true: c0 (7.0)
| | a10 = true
| | | a5 = false: c1 (5.0)
| | | a5 = true
| | | | a6 = false: c0 (7.0/2.0)
| | | | a6 = true: c3 (3.0)'''

import re

prolog_rules = []

pipe_map = {}

for line in decision_tree_for_prolog.split('\n'):
    line = line.replace(' ', '')
    pipe_cnt = line.count('|')
    if pipe_cnt == 0:
        pipe_map[pipe_cnt] = line.replace('t', 'T').replace('f', 'F').replace('=', '==')

    if '|' in line and ':' not in line:
        pipe_map[pipe_cnt] = re.findall(r"\|(.*)", line)[0].replace('|', '').replace('t', 'T').replace('f',
                                                                                                       'F').replace('=',
                                                                                                                    '==')

    if ':' in line:
        pipe_map[pipe_cnt] = re.findall(r"\|(.*?)\:", line)[0].replace('|', '').replace('t', 'T').replace('f',
                                                                                                          'F').replace(
            '=', '==')
        rule = ' and '.join(
            [pipe_map[i].replace('a', 'a[').replace('==', ']==').replace('Fa[', 'Fa') for i in range(pipe_cnt + 1)])
        action = re.findall(r"\:(.*?)\(", line)[0]
        rule = ' '.join(rule.split())
        prolog_rules.append((rule, action))


def process_parameters(input_params):
    params = list(input_params)
    if len(params) != 14:
        print("please input exactly 14 input parameters")
        return ''

    if set(list(input_params)) != set(('T', 'F')):
        print("please enter only in format of 'T' and 'F'")
        return ''

    a = [True if p == 'T' else False for p in input_params]

    for rule, action in prolog_rules:
        if eval(rule):
            return action

n_matches = 0
for i in range(df.shape[0]):
    gen = process_parameters(''.join(['T' if p == True else 'F' for p in df.iloc[i].values if p in (True, False)]))
    # print('generated:',)
    act = df.iloc[i]['class']
    # print('actual   :',act)
    # print('-'*10)
    if gen == act: n_matches += 1

print('our Prolog rules based predictor is accurate:',100*round(n_matches / df.shape[0],3),'% times')

directions = {'c0':'Forword','c1':'Left','c2':'Right','c3':'Backward'}
user_wants_to_stop = False

if __name__ == '__main__':
    while not user_wants_to_stop:
        input_params = input('enter 14 parameters to move rover(like TTTFTFTFFFTFTF) or enter "STOP" to exit:')
        if input_params == 'STOP' : break
        output = process_parameters(input_params)
        try:print('rover would move',output, 'i.e',directions[output])
        except:pass