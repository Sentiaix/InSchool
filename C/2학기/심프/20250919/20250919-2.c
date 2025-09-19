#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

/*학생의 점수(0~100)을 입력받아 다음 기준에 따라 학점을 계산할 것.
90점 이상 : A
80 ~ 89 : B
70 ~ 79 : C
60 ~ 69 : D
0 ~ 59 : F
단, 학점이 A B C인 경우 학점 뒤에 + -까지 표기할 것 (예: 97 > A+, 82 > B-, 70 > C)
+는 구간 상위 7 이상 (97, 88, 79)
-는 하위 2 이하 (91, 81, 70)*/

// function declaration
void add_function(int score); // 일의 자리 판단하는 함수.

int main(){
    int score;

    printf("Enter the score: ");
    scanf("%d", &score);

    // 직관성 있도록 점수를 숫자 자체로 구간을 나누고
    // 일의 자리 수를 판단하는 함수를 만들고 호출함.
    if (score == 100){ // 특수 케이스 제외
        printf("A+\n");
    } else if (score >= 90){ // A
        printf("A");
        add_function(score);
    } else if (score >= 80){ // B
        printf("B");
        add_function(score);
    } else if (score >= 70){ // C
        printf("C");
        add_function(score);
    } else if (score >= 60){ // D
        printf("D");
    } else if (score >= 0){ // F
        printf("F");
    } else { // 음숫값, 또는 100을 초과하는 경우
        printf("Out of Range. Please enter a valid score (0-100).");
    }
    
    printf("\n");

    return 0;
}

// define function
void add_function(int score){
    int degree = score % 10;
    // printf("****%d\n", degree); // test case1
    switch(degree){
            case 9:
            case 8:
            case 7:
                printf("+");
                break;
            case 6:
            case 5:
            case 4:
            case 3:
                break;
            case 2:
            case 1:
            case 0:
                printf("-");
                break;
        }
}