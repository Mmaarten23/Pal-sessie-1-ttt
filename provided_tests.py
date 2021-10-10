from opgave_template import is_lege_matrix, eentonige_lijst, is_matrix, gelijke_rand_matrix, strip_matrix


def printResult(actual, expected):
    print("succeeded" if actual == expected else "failed")


def runChecks():
    print("")
    print("====================================")
    print("          provided tests            ")
    print("====================================")
    print("")
    print("-- is_lege_matrix --")
    printResult(is_lege_matrix([]), True)
    printResult(is_lege_matrix([[]]), True)
    printResult(is_lege_matrix([[1, 1]]), False)
    printResult(is_lege_matrix([[1, 2]]), False)

    print("-- eentonige_lijst --")
    printResult(eentonige_lijst([]), True)
    printResult(eentonige_lijst([1]), True)
    printResult(eentonige_lijst([1, 1]), True)
    printResult(eentonige_lijst([1, 2]), False)
    printResult(eentonige_lijst([1, '1']), False)

    print("-- is_matrix --")
    printResult(is_matrix([]), True)
    printResult(is_matrix([[]]), True)
    printResult(is_matrix([[1]]), True)
    printResult(is_matrix([[1, 'a']]), True)
    printResult(is_matrix([[1, 'a'], [True, 1.2]]), True)
    printResult(is_matrix([[1, 'a'], [True, 1.2], ["hello"]]), False)

    print("-- gelijke_rand_matrix --")
    printResult(
        gelijke_rand_matrix(
            [[1, 'a'],
             [True, 1.2]]),
        False
    )
    printResult(
        gelijke_rand_matrix(
            [[1, 1, 1, 1],
             [1, 1.2, True, 1],
             [1, 1, 2, 1]]),
        False
    )
    printResult(
        gelijke_rand_matrix(
            [[1, 1, 1, 1],
             [1, 1.2, True, 1],
             [1, 1, 1, 1]]),
        True
    )
    printResult(
        gelijke_rand_matrix(
            [['a', 'a', 'a', 'a'],
             ['a', 1.2, True, 'a'],
             ['a', 1, 1, 'a'],
             ['a', 'a', 'a', 'a']]),
        True
    )
    printResult(
        gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                             ['a', 1.2, True, 'a'],
                             ['a', 1, 1, 'a'],
                             ['a', 'b', 'a', 'a']]),
        False
    )
    print("-- strip_matrix --")
    printResult(
        strip_matrix(
            [['a', 'a', 'a', 'a'],
             ['a', 1.2, True, 'a'],
             ['a', 1, 1, 'a'],
             ['a', 'b', 'a', 'a']]),
        [[1.2, True],
         [1, 1]]
    )

    printResult(
        strip_matrix(
            [['a', 'a', 'a', 'a'],
             ['a', 1.2, True, 'a'],
             ['a', 'b', 'a', 'a']]),
        [[1.2, True]]
    )
    m = strip_matrix([[1, 1, 1, 1]])
    printResult(m, [])
