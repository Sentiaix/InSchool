#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
/*1. 연산자 우선순위 비교 프로그램
정수 3개(a,b,c)를 입력받고, 다음 두 식의 결과를 비교하는 프로그램
1. (a+b) / c
2. a / (b+c)
*/



int main(){

    int a, b, c;
    printf("Enter 3 integers: ");
    scanf("%d %d %d", &a, &b, &c);

    double result_1, result_2;
    
    result_1 = (a + b) / c;
    result_2 = a / (b + c);

    printf("%f %f\n", result_1, result_2);

    if(result_1 == result_2){
        printf("Same\n");
    } else{
        printf("Not same\n");
    }

    return 0;
}