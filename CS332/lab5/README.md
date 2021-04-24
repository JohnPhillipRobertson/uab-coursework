To compile:
	"gcc recdir.c"
To run:
	"./a.out <dir_name>"
Description:
	Recursive program to print names of every file in the named directory, including the files inside directories contained inside the directories.
Test Case:
	Try "./a.out ." with orange.txt and the test directory in the same directory where you are running. It should list recdir.c, orange.txt, test, and grape.txt, which is inside test.
Sources:
	Dr. Bangalore's example program "readdir_v2.c"
	https://stackoverflow.com/a/298518/9295513 for help with finding what directory the program is currently in
Problems:
	Spent most of my time figuring out how to look for directories in a relative manner. Eventually I found the "hack" solution of changing what directory the program is in and then returning to the original directory when finished.
