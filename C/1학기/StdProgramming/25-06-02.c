  #define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct book{
	char title[64];
	double score;
} BOOK;

//function declaration
void print_BOOK(BOOK* bk); // BOOK 구조체의 내용 출력
BOOK get_BOOK(); // BOOK에 들어갈 정보를 받음
void sort_BOOK(BOOK* s, BOOK* f); // sort value by score

int main(){
	// (반환대상) = (반환하고 싶은 자료형 포인터)malloc(배열의 크기)
	// 예: int *p;            ( 여기서 n은 배열의 칸수임 )
	//		p = (int* p)malloc( n * sizeof(int));

	BOOK bk = {"Harry Potter", 3.5};
	print_BOOK(&bk);
	
	printf("How many books? ");
	int n;
	
	scanf("%d", &n); // 받을 변수의 수
	BOOK* ptr;
	ptr = (BOOK*)malloc( n * sizeof(BOOK));
	printf("%p %lu\n", ptr, sizeof(BOOK) * n);	
	
	for(int i = 0; i < n; i++){
		ptr[i] = get_BOOK();
	}
	sort_BOOK(ptr, ptr + n); // p[0].. p[n-1] sort by score
	
	for(int i = 0; i < n; i++){
		printf("book(%d): ", i);
		print_BOOK(ptr + i);
	}
	
	free(ptr);
	return 0;
}

//define function
void print_BOOK(BOOK* bk){
	printf("%s %lf\n", bk->title, bk->score);
}

BOOK get_BOOK(){
	BOOK bk;
	scanf("%[^\n]s", bk.title);
	scanf("%lf", &bk.score);
	return bk;
}

void sort_BOOK(BOOK* s, BOOK* f){
	// s is start value, f is last value
	// bubble sort pointer version
	for(BOOK* pt = s; pt < f; pt++){
		for(BOOK* pt2 = pt; pt2 < f - 1; pt2++){
			if( pt2->score < (pt2 + 1)->score){
				BOOK temp = *pt2;
				*pt2 = *(pt2 + 1);
				*(pt2 + 1) = temp;
			}
		}
	}
}   