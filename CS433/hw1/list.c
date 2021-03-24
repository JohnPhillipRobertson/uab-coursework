#include <stdio.h>
#include <dirent.h>
#include <stdlib.h>

void list() {
    //https://stackoverflow.com/a/612176/9295513
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir (".")) != NULL) {
        while ((ent = readdir (dir)) != NULL) {
            printf ("%s\n", ent->d_name);
        }
        closedir (dir);
    }
    else {
        perror ("");
        exit(1);
    }
}
