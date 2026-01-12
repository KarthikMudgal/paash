
# paash: password wordlist generator
```
 ██▓███   ▄▄▄      ▄▄▄        ██████  ██░ ██  ▐██▌  ▐██▌ 
▓██░  ██▒▒████▄   ▒████▄    ▒██    ▒ ▓██░ ██▒ ▐██▌  ▐██▌ 
▓██░ ██▓▒▒██  ▀█▄ ▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░ ▐██▌  ▐██▌ 
▒██▄█▓▒ ▒░██▄▄▄▄██░██▄▄▄▄██   ▒   ██▒░▓█ ░██  ▓██▒  ▓██▒ 
▒██▒ ░  ░ ▓█   ▓██▒▓█   ▓██▒▒██████▒▒░▓█▒░██▓ ▒▄▄   ▒▄▄  
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ░▀▀▒  ░▀▀▒ 
░▒ ░       ▒   ▒▒ ░ ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░  ░  ░  ░ 
░░         ░   ▒    ░   ▒   ░  ░  ░   ░  ░░ ░    ░     ░ 
               ░  ░     ░  ░      ░   ░  ░  ░ ░     ░    
                                                         
```
## Overview

This project is a Linux command-line password wordlist generator designed for security testing, penetration testing, and password auditing purposes.

This tool create realistic passwrod combinations wordlist by profiling a target using commonly known information such as:

* Names
* Nicknames
* Birthdates
* Pet names
* Favorite things
* Family names

## Key Features:-

* Supports both interactive user input and command-line flags for flexible execution.

* Generates passwords based on real human behavior, not random strings.

* Accepts DDMMYYYY / DDMMYY formats and expands them into commonly used numeric patterns.

* Combines names, nicknames, pets, hobbies, and family names in realistic ways.

* Converts common characters into leet variants (a → @, e → 3, s → $, etc.).

* Adds separators and symbols (_ . @ !) at realistic positions.

* Allows users to filter generated passwords by length constraints.

* Uses efficient data structures to ensure unique password entries.

* Users can define their own set of symbols or use safe defaults.

* Automatically saves the generated passwords to a ready-to-use wordlist file.

* Limits excessive combinations to maintain speed and practical output size.
* Generates the output in the wordlist.txt file after process.

## Installation
* Clone the repository
```bash
git clone https://github.com/KarthikMudgal/paash
cd paash
```


## Usage:-
```bash
python3 paash.py
```
