#include <stdio.h>

/*--- 문자열 s 중 가장 앞에 있는 문자 c를 탐색 ---*/
int str_char(const char s[], int c)
{
    int i;

    for (i = 0; s[i] != '\0'; i++)
        if (s[i] == c)
            return i;
    return -1;
}

int main(void)
{
    int no;
    char ch[10];

    printf("Enter the english char : ");
    scanf("%c", ch);

    no = str_char("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  "abcdefghijklmnopqrstuvwxyz", ch[0]);

    if (no >= 0 && no <= 25)
        printf("It is uppercase %dth.\n", no + 1);
    else if (no >= 26 && no <= 51)
        printf("It is lowercase %dth.\n", no - 25);
    else
        printf("It is not english char.\n");

    return 0;
}
