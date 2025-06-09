#include <stdio.h>
#include <stdlib.h>

// 함수 선언
void print(float* s, float* f);

int main(){
	int n;
	float* p;
	
	for(int i = 0; i < 100; i++){
		scanf("%d", &n);
		p = (float*)malloc(4 * n); // float p[n];
		float f;
		// ^^~~~~~~~
		// 메모리 반환형도 구 컴파일러에선 필수였지만, 요즘엔 알아서 처리함
		printf("Size of p is %lu\n", sizeof(p));	
		for(int i = 0; i < n; i++){
			p[i] = i * 10;
		}
		// 포인터 받고 출력해주는 함수 1
		printf("%p ", p);
		print(p, p+n);
		// p = &f; // 오류남, p는 동적, f는 정적변수임
		free(p);
		p = &f; // 이건가능
	}
	
	
	free(p);
	// ^^~~~~~ 메모리 반환도 똑같이 요즘엔 알아서 해주지만 미리 해두는게 좋음
	return 0;
}

// 함수 정의
void print(float* s, float* f){
	// int size = f - s; // size == n
	int k = 1;

	for(float* i = s; i < f; i++){
		printf("%d: %f\n", k, *i);
		k++;
	}
}