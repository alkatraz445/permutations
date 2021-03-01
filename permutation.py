def permutation(string, i, length):
    if i == length:
        output = "".join(string)
        print(output)
        f = open("wynik.txt", "a")
        f.write(str(output) + "\n")
        f.close()

    else:
        for j in range(i, length):
            string[i], string[j] = string[j], string[i]
            permutation(string, i+1, length)
            string[i], string[j] = string[j], string[i]


word = str(input("Wpisz wyraz: "))
n = len(word)
string = list(word)
permutation(string, 0, n)
