/* Sample program to read a comma separated file into a structure and
   display the array of structures */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINESIZE 1024

struct listing {
	int id, host_id, minimum_nights, number_of_reviews, calculated_host_listings_count,availability_365;
	char *host_name, *neighbourhood_group, *neighbourhood, *room_type;
	float latitude, longitude, price;
};

struct listing getfields(char* line){
	struct listing item;

	/* Note: you have to pass the string to strtok on the first
	   invocation and then pass NULL on subsequent invocations */
	item.id = atoi(strtok(line, ","));
	item.host_id = atoi(strtok(NULL, ","));
	item.host_name = strdup(strtok(NULL, ","));
	item.neighbourhood_group = strdup(strtok(NULL, ","));
	item.neighbourhood = strdup(strtok(NULL, ","));
	item.latitude = atof(strtok(NULL, ","));
	item.longitude = atof(strtok(NULL, ","));
	item.room_type = strdup(strtok(NULL, ","));
	item.price = atof(strtok(NULL, ","));
	item.minimum_nights = atoi(strtok(NULL, ","));
	item.number_of_reviews = atoi(strtok(NULL, ","));
	item.calculated_host_listings_count = atoi(strtok(NULL, ","));
	item.availability_365 = atoi(strtok(NULL, ","));

	return item;
}

void displayStruct(struct listing item) {
	printf("%d,  ", item.id);
	printf("%d, ", item.host_id);
	printf("%s, ", item.host_name);
	printf("%s, ", item.neighbourhood_group);
	printf("%s, ", item.neighbourhood);
	printf("%f, ", item.latitude);
	printf("%f, ", item.longitude);
	printf("%s, ", item.room_type);
	printf("%f, ", item.price);
	printf("%d, ", item.minimum_nights);
	printf("%d, ", item.number_of_reviews);
	printf("%d, ", item.calculated_host_listings_count);
	printf("%d\n", item.availability_365);
}

int main(int argc, char* args[]) {
	struct listing list_items[22555];
	char line[LINESIZE];
	int i, count;

	FILE *fptr = fopen("listings.csv", "r");
	if(fptr == NULL){
		printf("Error reading input file listings.csv\n");
		exit (-1);
	}

	count = 0;
	while (fgets(line, LINESIZE, fptr) != NULL){
		list_items[count++] = getfields(line);
	}
	fclose(fptr);

	for (i=0; i<count; i++)
		displayStruct(list_items[i]);

	return 0;
}
