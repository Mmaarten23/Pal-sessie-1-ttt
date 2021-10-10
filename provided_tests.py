from opgave_template import is_lege_matrix, eentonige_lijst, is_matrix, gelijke_rand_matrix, strip_matrix


def runChecks():
    print("")
    print("====================================")
    print("          provided tests            ")
    print("====================================")
    print("")
    print("-- is_lege_matrix --")
    print(is_lege_matrix([]) is True)  # True
    print(is_lege_matrix([[]]) is True)  # True
    print(is_lege_matrix([[1, 1]]) is False)  # False
    print(is_lege_matrix([[1, 2]]) is False)  # False
    print("-- eentonige_lijst --")
    print(eentonige_lijst([]) is True)  # True
    print(eentonige_lijst([1]) is True)  # True
    print(eentonige_lijst([1, 1]) is True)  # True
    print(eentonige_lijst([1, 2]) is False)  # False
    print(eentonige_lijst([1, '1']) is False)  # False
    print("-- is_matrix --")
    print(is_matrix([]) is True)  # True

    print(is_matrix([[]]) is True)  # True
    print(is_matrix([[1]]) is True)  # True
    print(is_matrix([[1, 'a']]) is True)  # True
    print(is_matrix([[1, 'a'], [True, 1.2]]) is True)  # True
    print(is_matrix([[1, 'a'], [True, 1.2], ["hello"]]) is False)  # False
    print("-- gelijke_rand_matrix --")
    print(gelijke_rand_matrix([[1, 'a'], [True, 1.2]]) is False)  # False
    print(gelijke_rand_matrix([[1, 1, 1, 1],
                               [1, 1.2, True, 1],
                               [1, 1, 2, 1]])
          is False)  # False
    print(gelijke_rand_matrix([[1, 1, 1, 1],
                               [1, 1.2, True, 1],
                               [1, 1, 1, 1]])
          is True)  # True
    print(gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                               ['a', 1.2, True, 'a'],
                               ['a', 1, 1, 'a'],
                               ['a', 'a', 'a', 'a']])
          is True)  # True
    print(gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                               ['a', 1.2, True, 'a'],
                               ['a', 1, 1, 'a'],
                               ['a', 'b', 'a', 'a']])
          is False)  # False
    print("-- strip_matrix --")
    print(strip_matrix([['a', 'a', 'a', 'a'],
                        ['a', 1.2, True, 'a'],
                        ['a', 1, 1, 'a'],
                        ['a', 'b', 'a', 'a']]) == [[1.2, True], [1, 1]])  # [[1.2, True], [1, 1]]
    print(strip_matrix([['a', 'a', 'a', 'a'],
                        ['a', 1.2, True, 'a'],
                        ['a', 'b', 'a', 'a']]) == [[1.2, True]])  # [[1.2, True]]
    m = strip_matrix([[1, 1, 1, 1]])
    print(m == [] or m == [[]])  # een lege matrix, [] of[[]]
