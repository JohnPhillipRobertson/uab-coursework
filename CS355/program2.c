/*
Simulate a pond with algae AND FISH and growth therein
John Phillip Robertson
04/11/2020
Note: the Python version of this,
without even fish logic,
took 178146.402 seconds,
nearly 50 hours.
I tried to rewrite it to .cpp,
but moat wouldn't accept it because of the
<random> library,
which was the only C++ feature I was using.
To compile:
	Go to moat (or your Linux terminal of choice)
	with this file and "gcc program2.c"
To run:
	./a.out
*/
/*Sources:
https://www.geeksforgeeks.org/generating-random-number-range-c/
https://stackoverflow.com/a/3025106/9295513
https://www.tutorialspoint.com/how-do-i-generate-random-floats-in-cplusplus
*/

#include <stdlib.h>
#include <stdio.h>

#define true 1
#define false 0

typedef struct {
	int alga;
	int fish[2];
} fishalg;

fishalg lake[100][100][100];
//https://stackoverflow.com/a/3025106/9295513
#define alg_die 0.1
#define alg_reproduce (0.2 + alg_die)
#define alg_survive (0.1 + alg_reproduce)
int fish_count = 1000000;  //Alternate 1000000

void populate() {
    int fi, fj, fk;
    for (fi = 0; fi < 100; fi++) {
    	for (fj = 0; fj < 100; fj++) {
    		for (fk = 0; fk < 100; fk++) {
    			lake[fi][fj][fk] = (fishalg) {2, {0, 0}};
    		}
    	}
    }
}

int fish_and_alga_stuff(fishalg* l) {
    //https://www.tutorialspoint.com/how-do-i-generate-random-floats-in-cplusplus
    //Once again, this would otherwise be a library call.
    float chance = (((float)rand()/(float)RAND_MAX) * 1);

	//Fish logic
	l->fish[1] -= 1;
	if (l->fish[0] != 0 && l->fish[1]/l->fish[0] < 5) { //feeding logic
		if (l->alga >= 1 && chance > 0.5) {
			l->alga -= 1;
			l->fish[1] += 3;
			if (l->fish[0] != 0 && l->fish[1]/l->fish[0] > 5.0) { //satiety logic
				l->fish[1] = 5 * l->fish[0];
			}
		}
	}
    if (l->alga > 0) {
	//Now it's the alga's turn just because here is where a return can happen.
	    int alga = l->alga;
    	if (chance < alg_die) {
    		l->alga -= 1;
    		if (alga >= 5) {
    			l->alga = 4;
    		}
    	}
    	else if (alg_die < chance && chance < alg_reproduce) {
    		l->alga += 1;
    	}
    	else if (alg_survive < chance) {
    		l->alga -= 1;
    		return true;  // Our flag to know if the algae should migrate...
    	}
    	return false; // ...or not.
    }
    return false;
}

int valid_migration(int i, int j, int k) {
    if (i < 100 && i >= 0 && j < 100 && j >= 0 && k < 100 && k >= 0) {
        return true;
    }
	return false;
}

void cycle(int generations) {
    unsigned int count[] = {0, 0, 0, 0, 0};
	int step, i, j, k, f;
    for (i = 0; i < fish_count; i++) {
        //https://www.geeksforgeeks.org/generating-random-number-range-c/
        //Math formulas aren't intellectual property,
        //and if you could simply download Clang++ on moat,
        //this would just be a call to a library someone else wrote.
    	int* cache = lake[(rand() % (99 - 0 + 1)) + 0][(rand() % (99 - 0 + 1)) + 0][(rand() % (99 - 0 + 1)) + 0].fish;
    	cache[0] += 1;
    	cache[1] += 2;
    }
	for (step = 0; step < generations; step++) {
	    count[0] = 0;
	    count[1] = 0;
	    count[2] = 0;
	    count[3] = 0;
	    count[4] = 0;
		for (i = 0; i < 100; i++) {
			for (j = 0; j < 100; j++) {
				for (k = 0; k < 100; k++) {
					int result = fish_and_alga_stuff(&lake[i][j][k]);
					fishalg kalga = lake[i][j][k];
					int ip = i + (rand() % (1 - -1 + 1)) + -1;
					int jp = j + (rand() % (1 - -1 + 1)) + -1;
					int kp = k + (rand() % (1 - -1 + 1)) + -1;
					if (result) {
						if (valid_migration(ip, jp, kp)) {
							fishalg kalgap = lake[ip][jp][kp];
							kalgap.alga += 1;
							if (kalgap.alga >= 5) {
								kalgap.alga = 4;
							}
						}
					}

					if (kalga.alga == 0) {
						count[0] += 1;
					}
					else if (kalga.alga == 1) {
						count[1] += 1;
					}
					else if (kalga.alga == 2) {
						count[2] += 1;
					}
					else if (kalga.alga == 3) {
						count[3] += 1;
					}
					else if (kalga.alga == 4) {
						count[4] += 1;
					}

					//Begin fish counting
					int curr_fish = kalga.fish[0];
					for (f = 0; f < curr_fish; f++) {
						if (kalga.fish[0] > 0 && kalga.fish[1]/kalga.fish[0] < 0.0) {
							fish_count -= 1;
							continue;
						}
						ip = i + (rand() % (1 - -1 + 1)) + -1;
						jp = j + (rand() % (1 - -1 + 1)) + -1;
						kp = k + (rand() % (1 - -1 + 1)) + -1;
						if (valid_migration(ip, jp, kp)) {
							fishalg kfishp = lake[ip][jp][kp];
							kfishp.fish[0] += 1;
							fish_count += 1;
							kfishp.fish[1] += 2;
							kalga.fish[1] -= 2;
						}
					}
					if (kalga.fish[0] >= 2) {
						kalga.fish[0] += 1;
						fish_count += 1;
					}
				}
			}
		}
		printf("Generation %d: %d Fish, %u Algae (%u of 0, %u of 1, %u of 2, %u of 3, %u of 4)\n", step + 1, fish_count, count[1] + count[2] + count[3] + count[4], count[0], count[1], count[2], count[3], count[4]);
	}
}

int main() {
    populate();
	cycle(1000);
	return 0;
}
