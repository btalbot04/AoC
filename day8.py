with open('day8.txt') as f:
    lines = []
    outputs = []
    for line in f.readlines():
        lines.append(line[:line.index('|')-1].split(' '))
        outputs.append(line[line.index('|')+2:].rstrip())

counter = 0

for line in lines:
    for chars in line:
        if len(chars) in [2,3,4,7]:
            counter+=1

#Day 2

def evaluate_line(line):
    sixes = []
    for thing in line:
        if len(thing) == 2:
            five_six = thing
        elif len(thing) == 6:
            sixes.append(thing)
        elif len(thing) == 3:
            sevens = thing
        elif len(thing) == 4:
            fours = thing

    for c in sixes:
        for letter in five_six:
            if letter not in c:
                pos_6 = letter
                break

    five_six = five_six.replace(pos_6, '')
    pos_5 = five_six

    for letter in sevens:
        if letter not in [pos_5, pos_6]:
            pos_1 = letter

    for a in [pos_1,pos_6,pos_5]:
        if a in fours:
            fours=fours.replace(a,'')

    for e in range(len(sixes)):
        for f in sixes[e]:
            if f in [pos_1,pos_5,pos_6]:
                sixes[e] = sixes[e].replace(f, '')

    for e in sixes:
        for f in fours:
            if f not in e:
                pos_7 = f

    for l in fours:
        if l is not pos_7:
            pos_2 = l

    for l in range(len(sixes)):
        for e in fours:
            if e in sixes[l]:
                sixes[l] = sixes[l].replace(e, '')

    for l in sixes:
        if len(l) == 1:
            pos_4 = l

    alphabet = 'abcdefg'
    positions = [pos_1,pos_2,pos_4,pos_5,pos_6,pos_7]

    for letter in alphabet:
        if letter not in positions:
            pos_3 = letter

    positions = [pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7]
    
    return positions

def count(digits, outputs):
    output = []
    digits = evaluate_line(digits)
    for a in outputs.split(' '):
        output.append(str(getValue(a, digits)))
    
    return int(''.join(output))

def getValue(a, digits):
    output = 0
    if len(a)==2:
        output += 1
    elif len(a)==3:
        output += 7
    elif len(a)==4:
        output += 4
    elif len(a)==7:
        output += 8
    elif len(a)==5:
        if digits[1] in a:
            output+=5
        elif digits[2] in a:
            output+=2
        else:
            output+=3
    elif len(a)==6:
        if digits[6] not in a:
            output+=0
        elif digits[2] in a:
            output+=6
        elif digits[2] not in a:
            output+=9

    return output


output = 0
for line in range(len(outputs)):
    output += count(lines[line], outputs[line])

evaluate_line(lines[0])
