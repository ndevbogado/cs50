#include<stdio.h>

void load_array(int size, int array[]);

int main(void)
{
    int SIZE = 10;
    int numbers[SIZE];

    int max = numbers[0];
    load_array(SIZE, numbers);

    int length = sizeof(numbers) / sizeof(numbers[0]);
    for (int i = 0; i < length; i++)
    {
        if (numbers[i] > max )
            max = numbers[i];
    }

    printf("Max=%i found!\n", max);
}

void load_array(int size, int array[])
{
     for (int i = 0; i < size; i++)
    {
        printf("Number_%i: ", i);
        scanf("%i", &array[i]);
    }
}
