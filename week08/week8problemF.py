from sys import stdin
trim = lambda s: s[:-1] if s[-1] == "\n" else s
s = trim(stdin.readline())

length = len(s)
while (True not in [s[i:i+length] != s[i:i+length][::-1] for i in range(0, len(s)-length+1)]) and (length > 0):
    length -= 1

print(length)
