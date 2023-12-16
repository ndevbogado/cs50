#include<stdio.h>
void draw(int height);


int main(void)
{
    int height;
    printf("Height: ");
    scanf("%i", &height);
    
    draw(height);
}

void draw(int height)
{
    for(int i = 1; i < height + 1; i++)
    {
        for(int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
