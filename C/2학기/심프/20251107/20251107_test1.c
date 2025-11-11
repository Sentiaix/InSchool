#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void test(/* cpp는 여기서 인자가 없으면 안됨. */);

int main(){
    test(10);

    return 0;
}

void test(int a){
    printf("%d", a);
}