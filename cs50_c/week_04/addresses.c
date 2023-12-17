#include<stdio.h>
#include<stdbool.h>

int main(void)
{
    int N = 50;
    int *n = &N;
    printf("%p\n",n);

    char my_string[20];
    printf("Type something: ");
    scanf("%19s", my_string);

    char *s = &my_string[0];
    printf("-- my_string = %s --\n", my_string);
    printf("-- &my_string= %p -- should equal to &my_string[0]\n",s);
    for (int i = 0; i < 10; i++)
        {
            if (s == &my_string[i])
            {
                printf("-> True: %p\n", &my_string[i]);
            }
            else
            {
                printf("-> False: %p\n",&my_string[i]);
            }
        }


}
