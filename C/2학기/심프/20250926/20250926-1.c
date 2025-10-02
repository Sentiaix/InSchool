#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// while은 조건문이 true일 때 반복
// do-while;은 한 번 실행 후, 조건문 확인 후 참이면 반복

int main(){
    int no;

    printf("Enter the positive integer: ");
    scanf("%d", &no);

    // if (no >= 0) {
    //     while (no >= 0){ // while은 조건문이 true일 때 반복
    //         printf("%d", no);
    //         no--;
    //     }
    //     printf("\n");
    // }

    if (no >= 1) {
        while (no >= 1){
            printf("%d ", no--);
        }
        printf("\n");
    }

    return 0;
}