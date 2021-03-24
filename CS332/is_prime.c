#include <stdio.h>

/*
Compilation:
gcc -o is_prime is_prime.c
*/

int is_prime(int n)
{
    int m = 2;
    int boo = 0;
    while (n % m != 0 && m < n)
    {
        m++;
        if (m == n)
            boo = 1;
    }
    if (n == 2 || n == 1)
        boo = 1;
    return boo;
}

int main()
{
    //https://www.tutorialspoint.com/c_standard_library/c_function_scanf.htm
    int given_number;
    printf("Need number\n");
    scanf("%d", &given_number);
    char *output = is_prime(given_number) ? "The number is prime" : "The number is not prime";
    printf("%s\n", output);
    return 0;
}