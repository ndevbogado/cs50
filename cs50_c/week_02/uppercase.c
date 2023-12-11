#include<stdio.h>
#include<string.h>

int main(void)
{
    char s[20];
    printf("Before: ");
    scanf("%s", s);

    printf("After: ");

    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i]-=32;
    }

    printf("%s\n", s);
}
