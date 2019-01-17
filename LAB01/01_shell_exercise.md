# Shell Exercise: Parsing text

On your Unix/Linux filesystem, you typically have a dictionary of words (https://en.wikipedia.org/wiki/Words_(Unix)).  On OS X, this is located in /usr/share/dict/words 

This file is missing from our barebones JupyterHub Linux distribution, so I added one to the class repo (2.4 MB).

Let’s use this file for some basic exercises.  For each of these, please document the command you ran and the output, so you can submit.
If you would prefer to wrap everything in a shell script, and submit that, go for it.

You will almost certainly need to google around for tips on how to answer some of these questions.  Use these resources, but if you find an explicit solution, don't just copy/paste, review it and try to understand what is actually happening.

## Inspect `words`
1. The `words` file has no extension. What type of file is this? (Hint: try `man file` to bring up man page on the `file` command)
2. Inspect the file `more words` (hit q to quit).  Should see one word per line.
3. How many words are in this file?
4. How many characters?
5. How big is the file size in bytes? How many bytes are required to store each character?
6. Print the first 3 words. Print the last 3 words (do this with a command, don’t just view or open in text editor and copy/paste)
7. How many characters are in the longest word?  Hint: should be simple one-liner, you don’t need awk for this.
8. Does `words` include the nickname for the UW mascot (if unfamiliar, ask your neighbor)? If so, what line number?
9. How many words end in “ology”?
10. How many end in “ologist”?
11. How many have the same prefix?
    * Hint: replace "ologist" with "ology", then count number of duplicate lines.

## Shell script
Create and run a script to answer the following question:

*How many words begin with each letter of the alphabet (case-insensitive)?*

### Useful references for review
* [http://swcarpentry.github.io/shell-novice/06-script/index.html](http://swcarpentry.github.io/shell-novice/06-script/index.html)

### Requirements:
* Ignore case, so "A" and "a" are considered the same word
* Your script should accept the `words` text file as an input argument (assign to a variable named fn)
* Your script should create a new output file called `words_lettercount.txt`
    * Pro tip: You can use [variable parameter substitution](https://www.tldp.org/LDP/abs/html/parameter-substitution.html) to do this: `out_fn=${fn%.*}_lettercount.txt`
    * The ${fn} construct is a less ambiguous variable reference.  Need this if you wanted to do something like print your filename and add extra characters `echo ${fn}:moretext` (try `echo $fn:moretext` for comparison)
    * The `%.*` can be used to get the first part of the filename string before any . extension ([see SO answer](https://stackoverflow.com/a/965072))
* The output file should include a letter and total count on each line (“a 17096”)

### Instructions:
1. Create a new shell script in your favorite text editor: `nano myawesomescript.sh`
2. Write some code.
3. Save the script.
4. Make it executable: `chmod +x myawesomescript.sh`
5. Run it! `./myawesomescript.sh words`
6. Review the output `more words_lettercount.txt`

## Submission (will discuss procedure in class)
1. Commit everything to your personal repo
2. Push to github
3. Open a pull request
