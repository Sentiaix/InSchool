#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>

// 2147483647
// 4294967295

/*---- declare function ----*/
int int_bits();
int count_bits(unsigned x);
void print_bits(unsigned x);
unsigned lrotate(unsigned x, int n);
unsigned rrotate(unsigned x, int n);
unsigned set(unsigned x, int pos);
unsigned reset(unsigned x, int pos);
unsigned inverse(unsigned x, int pos);

int main(){
    unsigned int x, n;

    printf("Enter an integer: ");
    scanf("%u", &x);
    printf("Enter number of bits to rotate: ");
    scanf("%u", &n);

    printf("Bits (0,1): ");
    print_bits(x);
    putchar('\n');

    printf("The number of bits were entered: %d\n", count_bits(x));
    printf("Left rotate by %u: ", n);
    print_bits(lrotate(x, n));
    putchar('\n');
    printf("Right rotate by %u: ", n);
    print_bits(rrotate(x, n));
    putchar('\n');

    return 0;
}

/*---- define function ----*/

// 비트 수 반환
int int_bits(){
    return count_bits(~0u); // ~0u: 모든 비트가 1인 부호 없는 정수
}

// 정수 n의 비트 수 세기
int count_bits(unsigned x){
    int bits = 0; // 비트 수 저장
    while(x){
        if (x & 1U) bits++; // x의 비트와 ..001 (1u)와 AND 연산 후 1이면 비트 수 증가
        x >>= 1; // n을 오른쪽으로 1비트 시프트. (0111 -> 0011)
    }

    return bits;
}

void print_bits(unsigned x){
    int i;
    for (i = int_bits() - 1; i >= 0; i--){
        putchar(((x >> i) & 1U) ? '1' : '0');
    }
}

// x를 n비트 왼쪽 회전
unsigned lrotate(unsigned x, int n){
    if (n < 9){
        int bits = int_bits();
        n %= bits;
        return n ? (x >> n) | (x << (bits - n)) : x;
    }
}

// x를 n비트 오른쪽 회전
unsigned rrotate(unsigned x, int n){
    if (n < 9){
        int bits = int_bits();
        n %= bits;
        return n ? (x << n) | (x >> (bits - n)) : x;
    }
}

// x의 pos 비트를 1로 설정
unsigned set(unsigned x, int pos){
    return x | (1U << pos);
}

// x의 pos 비트를 0으로 설정
unsigned reset(unsigned x, int pos){
    return x & ~(1U << pos);
}

// x의 pos 비트를 반전 (xor gate)
unsigned inverse(unsigned x, int pos){
    return x ^ (1U << pos);
}