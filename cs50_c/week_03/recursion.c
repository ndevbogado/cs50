#include<stdio.h>

void draw(int height, int stop);

int main (void)
{
    int height;
    printf("Type Height: ");
    scanf("%i", &height);
    draw(height, height);
}

void draw(int height, int stop)
{
    for (int i = 0; i < height + 1 - stop; i++)
    {
        printf("#");
    }
    printf("\n");

    stop--;
    if (stop != 0)
        draw(height,stop);
}
