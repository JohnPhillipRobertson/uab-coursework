#include <stdio.h>

int main(){
	int myarr[5] = {19, 10, 8, 17, 9};
    int min;
    int i;
    int mal = sizeof(myarr)/sizeof(*(myarr));
    for (i = 0; i < mal; i++) {
        if (i == 0) {
            min = *(myarr + i);
        }
        else {
            if (min > *(myarr + i)) {
                min = *(myarr + i);
            }
        }
    }
    return min;
}