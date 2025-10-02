#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int no;

    printf("몇 개의 *를 출력할까요?: ");
    scanf("%d", &no);

    if (no > 0){
        int i;
        int rem = no % 5;
        for(int i = 0; i < no / 5; i++){
            puts("*****");
        }
        if (rem > 0){
            for(int i = 0; i < rem; i++){
                putchar("*");
            }
            printf("\n");
        }
    }

    return 0;
}