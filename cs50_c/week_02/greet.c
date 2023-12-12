#include<stdio.h>

int main (int argc, char *argv[])
{
    printf("argc=%i\n",argc);
    printf("exe name argv[0]=%s\n", argv[0]);
    if (argc >= 2)
        for (int i = 1; i < argc; i++)
            printf("argv[%i]=%s\n", i,argv[i]);

}
