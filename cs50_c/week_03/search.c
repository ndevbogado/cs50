#include<stdio.h>

void load_array(int size, int array[]);

int get_length(int array[]);

int get_max(int size, int array[]);

int main(void)
{
    int SIZE = 5;
    int numbers[SIZE];

    load_array(SIZE, numbers);
   
    int max = get_max(SIZE, numbers);

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

int get_max(int size, int array [])
{
    int max = array[0];

    for (int i = 0; i < size; i++)
   {
        if (array[i] > max )
            max = array[i];
    }

    return max;
}
