#include <stdio.h>
typedef char BYTE; // 자료형 이름

// 메모리 공유함
union my_data{
	double d;
	char s[8];
};

// 각자 다른 메모리에 할당함
typedef struct my_data_struct{
	double d;
	char s[8];
} dlb_str; //< 바꾸고자 하는 이름

// enum은 배열처럼 숫자가 오르는데,
// 시작 번호와 끝번호, 변수처럼 개별값 할당도 가능하다
enum my_days{sun = 100, mon = 110, tue, wed, thu, fri, sat};
// for( enum my_days i = sun; i <= sat; i++) 이런식으로
// 출력한다면, 100>110까지도 하나씩 출력하고, 115가 마지막 값이 된다

// 위 enum my_days는 이제 enum my_days라고 부르지 않고 days로도 부를 수 있다.
typedef enum my_days days;

days f1(dlb_str a, dlb_str b, BYTE* c);
union my_data f2(dlb_str* b, BYTE c, int d, double e);
void f3(double* x, char* str, days enum_val);

int main(){

	printf("enum numbers: ");
	for( days i = sun; i <= sat; i++){
		printf("%d ", i);
	}
	printf("\n");

	struct my_data_struct a;
	dlb_str b;
	BYTE c; // same as 'char c'
	
		
	days k = f1(a, b, &c);
	
	union my_data e = f2(&b, c, 88, 3.14);

    f3(&b.d, b.s, k);
	
	// union my_data a;
	
	// scanf("%s", a.s);
	// printf("%s %lf %dBYTES\n", a.s, a.d, (int)sizeof(a));
	// scanf("%lf", &a.d);
	// printf("%s %lf %luBYTES\n", a.s, a.d, sizeof(a));

}

days f1(dlb_str a, dlb_str b, BYTE* c){
	days d;
	
	return d;
}

union my_data f2(dlb_str* b, BYTE c, int d, double e){
	union my_data x;
	
	return x;
}

void f3(double* x, char* str, days enum_val){

}