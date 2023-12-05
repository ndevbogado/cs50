#include <stdio.h>

int main(void)
{
    int size;
    bool continue_loop = true;
    
    do
    {
        printf("Type the size of the block: ");
        scanf("%d", &size);

        if (size >= 0)
        {
            continue_loop = false;
        } else 
        {
            printf("Bad value input! - ");
        }

    } while (continue_loop);

    for (int i = 0; i < size; i++)
    {
        for ( int j = 0; j < size; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
