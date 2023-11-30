#include <stdio.h>

int main(void)
{
    int max;

    printf("Type max rep, to count-up: ");
    scanf("%d", &max);


    int i = 0;
    while (i < max) 
    {
        printf("%d",i);
        printf("\n");
        i++;
    }
}

