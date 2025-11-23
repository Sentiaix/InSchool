#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

enum month {
  January = 1, February, March, April, May, June,
  July, August, September, October, November, December  
};

// 계절 출력
void print_season(enum month month) {
    switch (month) {
        case March:
        case April:
        case May:
            printf("Spring");
            break;
        case June:
        case July:
        case August:
            printf("Summer");
            break;
        case September:
        case October:
        case November:
            printf("Autumn");
            break;
        case December:
        case January:
        case February:
            printf("Winter");
            break;
        default:
            printf("Invalid month");
            break;
    }
}

// 월 선택
enum month select_month() {
    int tmp;
    
    do {
        printf("Select month (1-12): ");
        scanf("%d", &tmp);
    } while (tmp < January || tmp > December);
    return (enum month)tmp;
}

int main(){
    enum month your_month;

    printf("Select your birth month.\n");
    your_month = select_month();

    printf("You were born in ");
    print_season(your_month);
    printf(".\n");

    return 0;
}