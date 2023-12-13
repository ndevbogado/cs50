#include<stdio.h>

int main(void)
{
    int SIZE = 10;
    int numbers[SIZE];

    for (int i = 0; i < SIZE; i++)
    {
        printf("Number_%i: ", i);
        scanf("%i", &numbers[i]);
    }

    int max = numbers[0];
    int steps  = 0;

    int length = sizeof(numbers) / sizeof(numbers[0]);
    for (int i = 0; i < length; i++)
    {
        if (numbers[i] > max )
            max = numbers[i];
        else
            steps++;
    }

    printf("Max=%i found in %i steps!\n", max, steps);
}
