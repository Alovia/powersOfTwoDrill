#!/usr/bin/python
"""Drill powers of 2, with this one simple trick!"""

import os
import sys
import random
import time

def main(argv):
    print """
    Drill powers of 2, with this one simple trick!

    Tip:  the answer is always: number + quantifier, where
          number     = exponent mod 10 
          quantifier = exponent div 10   in 
             1: k(KB),         2: m (M),  
             3: g(GB),         4: t(Terabyte), 
             5: p (Petabyte),  6: e(Exabyte), 
             7: z(Zettabyte),  8: y (Yottabyte)

    This is because simplifying the numbers to human readable format
    give this (approximate) solution matrix:

   | 2^0  2^1  2^2  2^3  2^4   2^5   2^6   2^7    2^8    2^9   |  ^n
 ---------------------------------------------------------------------
   | 1    2    4    8    16    32    64    128    256    512   |  0-10 
 k | 1k   2k   4k   8k   16k   32k   64k   128k   256k   512k  | 11-20
 m | 1m   2m   4m   8m   16m   32m   64m   128m   256m   512m  | 21-30
 g | 1g   2g   4g   8g   16g   32g   64g   128g   256g   512g  | 31-40
 t | 1t   2t   4t   8t   16t   32t   64t   128t   256t   512t  | 41-50
 p | 1p   2p   4p   8p   16p   32p   64p   128p   256p   512p  | 51-60
 e | 1e   2e   4e   8e   16e   32e   64e   128e   256e   512e  | 60-70
 z | 1z   2z   4z   8z   16z   32z   64z   128z   256z   512z  | 70-80
 y | 1y   2y   4y   8y   16y   32y   64y   128y   256y   512y  | 80-90

 Example: 2^15 = 32k   (or, 32 KB in offcial long hand)
          because 15 % 10 = 5 -> 2^5 = 32, and 15 div 10 = 1 -> 'k' (KB)
    """

    powersAbbreviation = ['','k','m','g','t','p','e','z','y']
    powersNames = ['','KB','M', 'GB','Terabyte','Petabyte',
                   'Exabyte','Zettabyte','Yottabyte']

    random.seed(time.gmtime())
    answer = ""
    correct = 0
    wrong = 0
    while answer != "q":
        exponent = random.randint(1, 59)
        question = "(Type q to quit) Question:  2^%d is...?  > " % exponent

        answer = raw_input(question).replace(' ', '')
        if answer == "q":
            return

        solution = divmod(exponent,10)
        qu = solution[0]
        ex = solution[1]
        desired_answer = str(2**ex)+powersAbbreviation[qu]

        if answer == desired_answer:
            if exponent < 9:
                print "You are correct!"
            else:
                print "You are correct!  It's %d or, in short, %d %s" % (
                    2**exponent, 2**ex, powersNames[qu])
            correct += 1
        else:
            wrong += 1
            if exponent < 9: 
                print "Wrong!  2^%d = %s" % (ex, desired_answer)
            else:
                info1 = "Wrong!  2^%d = %s\n"
                info2 = "  since %d mod 10 = %d -> 2^%d = %d"
                info3 = " and (%d div 10) = %d -> %s"
                print  (info1 + info2 + info3) % (
                    exponent, desired_answer, exponent, ex, ex, 2**ex,
                    exponent, qu, powersAbbreviation[qu] +
                    ' ('+powersNames[qu]+')')

        print "Score so far:  Correct:  %d   Wrong:  %d" % (correct, wrong)
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
