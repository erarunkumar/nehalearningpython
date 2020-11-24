def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("kevin won", kevsc)
    elif kevsc < stusc:
        print("stuart won",stusc)
    else:
        print("draw")

if __name__ == '__main__':
    s=input("enter any word ")
    minion_game(s)


def minion_game(string):
    # your code goes here

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s))
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")
if __name__ == '__main__':
    s = input("enter word")
    minion_game(s)
