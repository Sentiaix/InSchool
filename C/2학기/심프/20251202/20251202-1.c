/* 문자열을 조작하는 다양한 함수 */
#include <stdio.h>

/*--- 문자열 s 중 문자 c의 개수 반환 ---*/
int str_chnum(const char s[], int c)
{
    int i, count = 0;

    for (i = 0; s[i] != '\0'; i++) // '\0' == 0 내부적으로 0의 값을 가짐. 0032 8bits
        if (s[i] == c)
            count++;

    return count;
}

/*--- 문자열 s를 n번 출력 ---*/
void put_stringn(const char s[], int n)
{
    while (n-- > 0)
        printf("%s", s);
}

/*--- 문자열 s의 길이 반환 ---*/
int str_length(const char s[])
{
    int len = 0;

    while (s[len])
        len++;

    return len;
}

/*--- 문자열 s를 거꾸로 출력 ---*/
void put_stringr(const char s[])
{
    int i = str_length(s) - 1;

    if (s[i] == '\0') printf("NULL PRINTED ERROR!!!!!!! >> ");
    while (i >= 0)
        putchar(s[i--]);
}

/*--- 문자열 s의 문자 나열 반전 ---*/
void rev_string(char s[])
{
    int i, len = str_length(s);

    for (i = 0; i < len / 2; i++) {
        char temp = s[i];
        s[i] = s[len - i - 1];
        s[len - i - 1] = temp;
    }
}

int main(void)
{
    char str[256], ch;

    printf("Enter the string : ");
    scanf("%s", str);

    getchar();

    printf("Enter the char : ");
    scanf("%c", &ch);

    printf("str has %d ch.\n", str_chnum(str, ch));

    printf("reverse reading the str : ");
    put_stringr(str);     /* str을 거꾸로 출력 */
    putchar('\n');

    rev_string(str);      /* str 반전 */

    printf("Reversed str. print 5 times.\n");
    put_stringn(str, 5);
    putchar('\n');

    return 0;
}