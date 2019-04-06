@echo off
cd C:\Users\in10c2\Documents\MEGAsync\Letters2Words

g++ WORDS.cpp -o WORDS.exe
WORDS.exe > WORDS.TXT
python WORDS.py