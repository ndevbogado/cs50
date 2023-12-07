#include <stdio.h>

float average(int numbers[], int SIZE);

int main(void)
{
    int SIZE = 3;
    int score[SIZE];

    for  (int i = 0; i < SIZE; i ++)
    {
        printf("Type the number %i: ",i);
        scanf("%i", &score[i]);
    }

    printf("Average %f\n", average(score, SIZE));

}

float average(int numbers[], int SIZE)
{
    int total = 0;

    for (int i = 0; i < SIZE; i++)
    {
        total += numbers[i];
    }

    return total / (float)SIZE;
}
