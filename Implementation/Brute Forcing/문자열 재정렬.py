import time

s = input()

start_time = time.time()

character = []
number = []
string = ''
for c in s:
    if ord(c) < 58:
        number.append(int(c))
    else:
        character.append(c)

for c in sorted(character):
    string += str(c)
print(string + str(sum(number)))
end_time = time.time()
print(end_time - start_time)