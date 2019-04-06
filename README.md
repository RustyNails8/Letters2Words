# Letters2Words
For a set of letters, find all possible Words

## Welcome to SD Projects

I use the [editor on GitHub](https://github.com/RustyNails8/SAPonAIXandOracle/edit/master/README.md) to maintain and preview the content for your website in Markdown files. Whenever I commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## PreRequisites:
1. CPP complier g++. Get from [HERE](https://filehippo.com/download_dev-c/)
2. Python Interpreter version 3.7. Get from [HERE](https://www.python.org/)
3. Install the enchant Python PyPi Package. Get from [HERE](https://pypi.org/project/pyenchant/)

```markdown
# Letters2Words
# Sumit Das
# Created 2019 04 06


1. Run the 3-RunMe.cmd with the letters as arguments
2. Your possible words would be displayed rightaway
3. Additinally 2 more files like WORDS.exe and WORD.TXT are created.

- ** Remove g++ compile step after first run ** 
- ** ONLY remove/comment this line from 3-RunMe.cmd file AFTER you have 1 SUCCESSFUL run of 3-RunMe.cmd **

```batch script ahead
```

```batch
REM Complie your CPP program
REM You can remove this once the WORDS.exe file is created
g++ 1-MakeWordList4mLetters.cpp -o WORDS.exe

```

- ** Above should be changed TO Below : **

```batch
REM Complie your CPP program
REM You can remove this once the WORDS.exe file is created
REM g++ 1-MakeWordList4mLetters.cpp -o WORDS.exe
```

### Jekyll Themes

My Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/RustyNails8/SAPonAIXandOracle/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
