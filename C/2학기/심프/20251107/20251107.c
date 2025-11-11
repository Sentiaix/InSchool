#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// 알쏭달송 180제 7-10
// 정수 x 안의 세트된 비트 수 반환
int count_bits(unsigned x){
    int bits = 0;
    while(x){
        if (x & 1U) bits++;
        x >>= 1;
    }

    return bits;
}

// unsigend 형의 비트 수 반환
int int_bits(){
    return count_bits(~0u);
}

// unsgied 형의 비트 출력
void print_bits(unsigned x){
    int i;
    for (i = int_bits() - 1; i >= 0; i--){
        putchar((x & (1u << i)) ? '1' : '0'); // x의 i번째 비트가 1이면 '1' 출력, 아니면 '0' 출력
    }
}

// x를 왼쪽으로 n비트 시프트한 값 반환
unsigned lsht(unsigned x, int n){
    return (n <= 0 || n >= int_bits()) ? x : (x << n);
}

// x의 pos비트째부터 n비트를 1로 한 값 반환
unsigned set_n(unsigned x, int n, int pos){
    return x | lsht(~lsht(~0, n), pos);
}

// x의 pos비트째부터 n비트를 0으로 한 값 반환
unsigned reset_n(unsigned x, int n, int pos){
    return x & ~lsht(~lsht(~0, n), pos);
}

// x의 pos비트째부터 n비트를 반전한 값 반환
unsigned inverse_n(unsigned x, int n, int pos){
    return x ^ lsht(~lsht(~0, n), pos);
}

int main(){
    unsigned x, pos, n;

    printf("부호 없는 정수 x의 pos 비트로부터 pos + n - 1 비트까지 조작합니다.\n");
    printf("x   : "); scanf("%u", &x);
    printf("pos : "); scanf("%u", &pos);
    printf("n   : "); scanf("%u", &n);

    printf("\nx                    = "); print_bits(x);
    printf("\nset_n(x, %u, %u)       = ", n, pos); print_bits(set_n(x, n, pos));
    printf("\nreset_n(x, %u, %u)     = ", n, pos); print_bits(reset_n(x, n, pos));
    printf("\ninverse_n(x, %u, %u)   = ", n, pos); print_bits(inverse_n(x, n, pos));
    putchar('\n');

    return 0;
}