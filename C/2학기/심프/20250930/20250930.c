#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int no, temp;
    int digits; // 자릿수

    do{
        printf("Enter the positive Integer: ");
        scanf("%d", &no);
        if (no <= 0){
            printf("\nPlease enter the positive integer.\n");
        }
    } while (no <= 0);

    // no는 0보다 큼
    temp = no;
    digits = 0;
    
    while (temp > 0){
        temp /= 10;
        digits++;
    }
    printf("%d is %d자리입니다.\n", no, digits);

    return 0;
}