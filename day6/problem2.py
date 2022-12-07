from collections import deque

charset = deque()
count = 0

with open("input_stream.txt", "r") as f:
    for line in f:
        for char in line:
            if count < 14:
                charset.append(char)
                count += 1
            else:
                if len(charset) == len(set(charset)):
                    break
                else:
                    charset.popleft()
                    charset.append(char)
                    count += 1

print(count)