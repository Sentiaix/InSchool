#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    
    int a, b, diff;

    puts("Enter 2 integers.");
    printf("Integer A : "); scanf("%d", &a);
    printf("Integer B : "); scanf("%d", &b);

    // 코딩 할 부분
    int max, min;

    if(a == b){
        printf("Two integers are same.\n");
    } else if (a < b){
        min = a;
        max = b;
        printf("Min is %d, Max is %d.\n", min, max);
    } else{
        min = b;
        max = a;
        printf("Min is %d, Max is %d.\n", min, max);
    }

    return 0;
}