#include<stdio.h>
#include<string.h>

typedef struct
{
    char name[20];
    char power[20];
    char metal[20];
}
alomancer;


int main (void)
{
    int SIZE = 2;
    alomancer alomancers[SIZE];

    for (int i = 0; i < SIZE; i++)
    {
        printf("Character's name: ");
        scanf("%s", alomancers[i].name);

        printf("Power source: ");
        scanf("%s", alomancers[i].power);

        printf("Primary metal: ");
        scanf("%s", alomancers[i].metal);
    }

    for (int i = 0; i < SIZE; i++)
    {
        printf("%s, named %s. Primary metal source: %s\n", alomancers[i].power, alomancers[i].name, alomancers[i].metal);
    }
    
}

