#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h> // strlen 사용

// function declaration
int count_char(char* char_fnder, char value); // str 받고 특정 char 찾기
int count_str(char* str_fnder, char* str_value); // str 받고 특정 str 찾기

int main(){
    char str[128]; //str is &str[0] // 주의! 문자열을 char+배열로 받을 경우, 마지막 칸은 EOF 전용 칸으로 남겨두어야 함.

    scanf("%[^\n]s", str); //standby EOF
    printf("%s\n", str);

    printf("how many %c? %d\n", 'e', count_char(str, 'e'));
    printf("how many %s? %d\n", "foot", count_str(str, "foot"));

    return 0;
}

// define function
int count_char(char* char_fnder, char value){
    int cntr = 0;
    // for 반복문에서 char_fnder[i] 값이 마지막 글자가 아니면 계속 반복
    // char + 배열은 EndOfFile의 약자로 한 문자열(FILE)의 끝남을 알리는 코드임. stdio.h에서 -1의 정수값으로 내장돼있음
    for(int i = 0; char_fnder[i] != '\0'; i++){
        if(char_fnder[i] == value){
            cntr++;
        }
    }

    return cntr;
}

int count_str(char* str_fnder, char* str_value){
    int str_cntr = 0;
    int i = 0;

    while(str_fnder[i]){
        if(str_fnder[i] == str_value[0]){ // 첫글자 파악
            for(int j = 1; str_value[j] != '\0'; j++){
                if(str_fnder[i + j] == str_value[j] && str_value[j] == '\0'){
                    str_cntr++;
                }
            }
        }
        i++;
    }
    
    return str_cntr;
}