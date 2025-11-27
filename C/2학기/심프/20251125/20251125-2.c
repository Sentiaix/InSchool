/* 문자열 배열을 읽어 들여 출력 */
#include <stdio.h>
#include <string.h>
#define NUM 10      /* 문자열 개수 */

int main(void)
{
    int i, no;
    char s[NUM][128];
    char stop_str[] = "$$$$$";

    no = NUM;
    printf("%d개의 문자열을 입력하라(\"$$$$$\"로 중단).\n", NUM);

    for (i = 0; i < NUM; i++) {
        printf("s[%d] : ", i);
        scanf("%s", s[i]);

        if (!strcmp(s[i], stop_str)) { // strcmp은 char 한개씩 비교하며, 같으면 0을 반환
        // strcmp 함수는 두 개의 C 스타일 문자열을 비교하여, 첫 번째 문자열이 두 번째 문자열보다 작으면 음수, 같으면 0, 크면 양수를 반환
            no = i;
            break;
        }
    }

    for (i = 0; i < no; i++)
        printf("s[%d] = \"%s\"\n", i, s[i]);

    return 0;
}