import sys
input = sys.stdin.readline

music = input().strip()

ascending = '1 2 3 4 5 6 7 8'
descending = '8 7 6 5 4 3 2 1'

if music == ascending:
    print("ascending")
elif music == descending:
    print("descending")
else:
    print("mixed")