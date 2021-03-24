CS 433 Homework 1 "uab_sh"
A basic shell implemented in C
Author: John Robertson
Help from the following sources:
	https://stackoverflow.com/a/7021750/9295513
	https://stackoverflow.com/a/612176/9295513
	https://linux.die.net/man/3/getcwd
	http://man7.org/linux/man-pages/man2/chdir.2.html
	"help" text is verbatim from assignment pdf
To compile:
	make
Or try:
	gcc -c -I -Wall shell.c
	gcc shell.o fib.o hello.o help.o history.o list.o change_d.o -o shell
Dependencies:

Sample test cases:
	enter "hello"
	enter "hellp"
	enter "help"
	enter "fibonacci" then an integer
	enter "fibonacci" then nonsense
	enter "fibonacci 14"
	enter "fibonacci carrot"
	enter "list"
	enter "cd .."
	enter "list" again
	enter a newline
	enter quit

Sample session:

```
$ ./shell
uab_sh > fibonacci
How many elements do you want to display?12
0 1 1 2 3 5 8 13 21 34 55 89
uab_sh > fibonacci 12
0 1 1 2 3 5 8 13 21 34 55 89
uab_sh > history
hLol I'm not a grad student.
uab_sh > hello
Invalid command. Try 'help' for help.
uab_sh > hello
Hello World!
uab_sh > help
hello -print 'Hello World!'
fibonacci <int> -Print fibonacci numbers up to <int>. Without args, will ask for the int.
list –list all the files in the current directory.
cd <directory> –change the current directory to the <directory>. The default directory would be the directory where the shell program was invoked.
help –display the internal commands and a short description on how to use them.
quit –quit the shell program.
history –display all the previous command entered into the shell program.
uab_sh > quit
~{0.08}~{jprob@vulcan13:~/cs433/hw1}~~
$ nano shell.c
~{0.05}~{jprob@vulcan13:~/cs433/hw1}~~
$ ./shell
uab_sh > history
Lol I'm not a grad student.
uab_sh > sedes be like
Invalid command. Try 'help' for help.
uab_sh > cd ..
You are now in the .. directory.
uab_sh > cd ..
You are now in the .. directory.
uab_sh > cd .
You are now in the . directory.
uab_sh > list
.
..
.bash_history
.cache
.config
.dbus
.esd_auth
.ICEauthority
.local
.pki
.ssh
.viminfo
cs330
cs332
cs433
uab_sh > cd cs330
You are now in the cs330 directory.
uab_sh > list
.
..
a8
a9
assignment_one
assignment_seven
assignment_six
assignment_three
assi_5
imprimis
lab4
lab6
lab7
lab8
uab_sh > cd a9
You are now in the a9 directory.
uab_sh > list
.
..
asNine
asNine.s
bonus
bonus.s
labNine
labNine.s
	labNine2
	labNine2.s
	labNine3
	labNine3.s
	uab_sh > quit
```

Contact author at jprob@uab.edu
