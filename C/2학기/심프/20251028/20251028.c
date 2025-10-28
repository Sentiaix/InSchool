#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stddef.h>

int main(){
    int n;

    printf("sizeof 1             = %u\n", (unsigned)(sizeof 1)); // int 형의 크기 = 4
    printf("sizeof+1             = %u\n", (unsigned)(sizeof+1)); // int 형의 크기
    printf("sizeof-1             = %u\n", (unsigned)(sizeof-1)); // int 형의 크기
    printf("sizeof(unsigned)-1   = %u\n", (unsigned)(sizeof(unsigned)-1)); // unsigned 형의 크기(4) - 1 = 3
    printf("sizeof(double)-1     = %u\n", (unsigned)(sizeof(double)-1)); // double 형의 크기(8) - 1 = 7
    printf("sizeof((double)-1)   = %u\n", (unsigned)(sizeof((double)-1))); // (double형 - int형)의 크기 = double형 크기 = 8
    printf("sizeof n+2           = %u\n", (unsigned)(sizeof n+2)); // n의 크기 + 2 = 4 + 2 = 6
    printf("sizeof(n+2)          = %u\n", (unsigned)(sizeof(n+2))); // (n+2)의 크기 = int형의 크기 = 4
    printf("sizeof(n+2.0)        = %u\n", (unsigned)(sizeof(n+2.0))); // n + 2.0(double형)의 크기 = 결괏값은 double로 됨 >> 8

    return 0;
}