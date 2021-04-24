#include <stdio.h>
#include "functions.h"

int main(){
   print_hello();
   printf("\n");
   int num = 5;
   printf("Factorial of %d is %d",num, factorial(num)); 
   return 0;
}
