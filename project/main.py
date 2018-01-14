"""
The main entry class

library: os
Author: Jie Tao
Time: 2018-01-12
"""
from project import FKCalcu as FKC
import codecs


def main():
    filename = "sciencekids.txt"
    with codecs.open('testfiles/'+filename,encoding="utf-8", mode="r") as gradefile:          # read the file into string
        text = gradefile.read()
    aFKCalcu = FKC.FKCalcu(text)                        # new calculation instance
    aFKCalcu.calFKGrade()                               # calculation
    print(gradefile.name)
    print("total words num:"+str(aFKCalcu.totalWords),flush=True)               # export words num by printing
    print("total sentence num:"+str(aFKCalcu.totalSentence))                    # export sentence num by printing
    print("total syllable num:"+str(aFKCalcu.totalSyllables))                   # export syllable num by printing
    print("avgerage words:"+str(round(aFKCalcu.avgword,2)))                     # export average words num by printing
    print("avergae syllabes:"+str(round(aFKCalcu.avgSyllables,2)))              # export average syllable by printing
    print("Grade:"+str(round(aFKCalcu.grade,2)))                                # export grade by printing

if __name__ == '__main__':
    main()

