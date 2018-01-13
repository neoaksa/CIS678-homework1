"""
The main entry class

library: os
Author: Jie Tao
Time: 2018-01-12
"""
from project import FKCalcu as FKC
import os


def main():
    with open('txtbook.txt',"r") as gradefile:          # read the file into string
        text = gradefile.read()
    aFKCalcu = FKC.FKCalcu(text)                        # new calculation instance
    aFKCalcu.calFKGrade()                               # calculation
    print("total words num:"+str(aFKCalcu.totalWords),flush=True)               # export words num by printing
    print("total sentence num:"+str(aFKCalcu.totalSentence))                    # export sentence num by printing
    print("total syllable num:"+str(aFKCalcu.totalSyllables))                   # export syllable num by printing
    print("avgerage words:"+str(round(aFKCalcu.avgword,2)))                     # export average words num by printing
    print("avergae syllabes:"+str(round(aFKCalcu.avgSyllables,2)))              # export average syllable by printing
    print("Grade:"+str(round(aFKCalcu.grade,2)))                                # export grade by printing

if __name__ == '__main__':
    main()

