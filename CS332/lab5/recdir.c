#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <unistd.h>


char *filetype(unsigned char type) {
	char *str;
	switch(type) {
		case DT_BLK: str = "block device"; break;
		case DT_CHR: str = "character device"; break;
		case DT_DIR: str = "directory"; break;
		case DT_FIFO: str = "named pipe (FIFO)"; break;
		case DT_LNK: str = "symbolic link"; break;
		case DT_REG: str = "regular file"; break;
		case DT_SOCK: str = "UNIX domain socket"; break;
		case DT_UNKNOWN: str = "unknown file type"; break;
		default: str = "UNKNOWN";
	}
	return str;
}

void filetraverse(DIR* pd, int indent, char* dname) {
    chdir(dname);
    struct dirent* dnt;
	int count = 1;
	while ((dnt = readdir(pd)) != NULL) {
		int i;for (i = 0; i < indent; i++) {printf("\t");}//cruft to handle indentation, look away

		printf("[%d] %s (%s)\n", count, dnt->d_name, filetype(dnt->d_type));
		if (DT_DIR == dnt->d_type &&
		    strcmp(dnt->d_name, "..") != 0 &&
		    strcmp(dnt->d_name, ".") != 0 &&
	    	pd != NULL) {
		    DIR* child_dir;
		    char* fullpath = dnt->d_name;
		    child_dir = opendir(fullpath);
		    if (child_dir != NULL) {
		        filetraverse(child_dir, indent + 1, dnt->d_name);
		        chdir("..");
		    }
		}
		count++;
	}
	closedir(pd);
}



int main (int argc, char **argv) {
	DIR* parentDir;
	if (argc < 2) {
		printf ("Usage: %s <dirname>\n", argv[0]);
		exit(-1);
	}
	parentDir = opendir(argv[1]);
	if (parentDir == NULL) {
		printf ("Error opening directory '%s'\n", argv[1]);
		exit (-1);
	}
	//https://stackoverflow.com/a/298518/9295513
	char* retval;
	getcwd(retval, sizeof(retval));
	filetraverse(parentDir, 0, argv[1]);
	chdir(retval);
	return 0;
}
