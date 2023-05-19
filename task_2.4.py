# A
def remove_exclamation_marks(s_A):
    print(s_A.replace('!', ''))

remov = input()
remove_exclamation_marks(remov)

# B
def remove_word_with_one_em(s_B):
     if s_B.endswith("!"):
         print(s_B[:-1])
     else:
         print(s_B)

word_with_one_em = input()
remove_word_with_one_em(word_with_one_em)

#C
def remove_word_with_one_em(s_C):
    words = s_C.split()
    not_em = []
    for s in words:
        if s.count('!') == 1:
            continue
        else:
            not_em.append(s)
    print(' '.join(not_em))

word_with_em = input()
remove_word_with_one_em(word_with_em)

