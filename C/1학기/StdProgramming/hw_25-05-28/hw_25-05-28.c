#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct student{
	char name[64];
	int id;
	float grade;
} STUDENT;

void save_student(const char* txtName, STUDENT a);
void print_student(STUDENT a);
STUDENT load_student(const char* txtName);
void save_arr(const char* txtName, STUDENT arr[3], int n);
void load_arr(const char* txtName, STUDENT myclass[3], int n);


int main(){
// FILE*, fopen, fclose, EOF, fprintf, fscanf, fread, fwrite

	printf("*******************\n");
	STUDENT arr[3] = {{"Harry", 12345, 3.9},
						 {"Potter", 458, 3.0},
						 {"Jake", 128, 3.6}};
	save_arr("students.txt", arr, 3);
	STUDENT myclass[3];
	load_arr("students.txt", myclass, 3);
	print_student(myclass[0]);
	print_student(myclass[1]);
	print_student(myclass[2]);
	printf("*******************\n");

	STUDENT a = {"Harry", 12345, 3.9};
	print_student(a);
	save_student("harry.txt", a);
	STUDENT mage = load_student("harry.txt");
	printf("Mage is ");
	print_student(mage);

	// FILE 구조체를 fp라는 포인터 매개변수로 불러낸다.
	FILE* fp = NULL; // 포인터 초기화는 NULL 추천
	// w: write(overwrite), r: read, a: append
	fp = fopen("file.txt", "w"); // fp에 "file.txt"을 "*mode"로 연다고 저장한다.

	fprintf(fp, "Good night\n");
	fprintf(fp, "he likes to roam\n");
	fclose(fp); // fp = NULL;
	
	fp = fopen("file.txt", "r");
	char buffer[128];
	// fscanf(fp, "%[^\n]s", buffer);
	char c;
	int i = 0;
	// EOF is -1
	while(fscanf(fp, "%c", &c) != EOF){
		buffer[i] = c;
		i++;
	}
	buffer[i] = '\0';
	printf("%s", buffer);
	fclose(fp);
	
	return 0;
}

void save_student(const char* txtName, STUDENT a){
	FILE* fp = NULL;
	
	fp = fopen(txtName , "w");
	
	fprintf(fp, "%s %d %f\n", a.name, a.id, a.grade);
	
	fclose(fp);
}

void print_student(STUDENT a){
	printf("%s %d %f\n", a.name, a.id, a.grade); 
}

STUDENT load_student(const char* txtName){
	STUDENT x;
	
	FILE* fp = NULL; // fp 초기화
	
	fp = fopen(txtName, "r");
	fscanf(fp, "%s %d %f", x.name, &x.id, &x.grade);
	
	fclose(fp);
	
	return x;	
}

void save_arr(const char* txtName, STUDENT arr[3], int n){
	FILE* fp = NULL;
	
	fp = fopen(txtName, "w");
	
	for(int i = 0; i < n; i++){
		fprintf(fp, "%s %d %f\n", arr[i].name, arr[i].id, arr[i].grade);	
	}

	fclose(fp);
}
void load_arr(const char* txtName, STUDENT myclass[3], int n){
	FILE* fp = NULL;

	fp = fopen(txtName, "r");

	for(int i = 0; i < n; i++){
		fscanf(fp, "%s %d %f", myclass[i].name, &myclass[i].id, &myclass[i].grade);
	}

	fclose(fp);

}