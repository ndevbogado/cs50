#include<stdio.h>
#include<string.h>

void memory_scan(int memory, char s[]);
void process(int memory, char s[], char repeat);

int main(void)
{
    char *s = "Hello There!";

    int memory;
    char repeat;
    process(memory, s, repeat);
}

void process(int memory, char s[], char repeat)
{
    printf("Scan memory until position: ");
    scanf("%i", &memory );

    memory_scan(memory, s);
    printf("Continue scannig memory? ");
    scanf("%1s", &repeat);

    if (repeat == 'y' )
        process(memory, s, repeat);
}

void memory_scan(int memory, char s[])
{
    for (int i = 0; i >-memory; i-- )
            printf("%c", *(s+i));
    printf("\n");
}
