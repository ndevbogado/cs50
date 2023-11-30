#include <stdio.h>

int main(void)
{
    int max;

    printf("Type max rep, to count-up: ");
    scanf("%d", &max);

    for(int i = 0; i < max; i++)
    {
        printf("%d",i);
        printf("\n");
    }
}

