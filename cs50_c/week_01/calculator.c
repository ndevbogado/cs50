#include <stdio.h>

int main(void)
{
    int result;
    int numbers[] = {0,0};

    for (int i = 0; i < 2; i++)
    {
        printf("Type %i number: ", i+1);
        scanf("%d", &numbers[i]);

        result += numbers[i];
    }
    
    printf("The result is: %d \n", result);
}

