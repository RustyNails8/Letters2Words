@echo off

REM Sumit Das
REM 2019-04-06

REM REM your path to master    cd C:\Users\in10c2\Documents\MEGAsync\Letters2Words
REM Provide the series of letters without any space

REM Complie your CPP program
REM You can remove this once the WORDS.exe file is created
REM g++ 1-MakeWordList4mLetters.cpp -o WORDS.exe

REM Run the compiled CCP program to get list of works
WORDS.exe %1 > WORDS.TXT

REM run the Python script to generate words from the list using enchant
python 2-MakeWords4mLists.py