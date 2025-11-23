// #define _CRT_SECURE_NO_WARNINGS
// #include <stdio.h>
// #define alert2() (printf("\a\a"))
// #define puts_alert2(str) ( alert2(), puts(str) )


// int main(){
//     int n;

//     printf("Enter the integer: ");
//     scanf("%d", &n);

//     if (n){
//         puts_alert2("This number is not 0.");
//     }
//     else {
//         puts_alert2("This number is 0.");
//     }

//     return 0;
// }

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define NUMBER 5

void bsort(int a[], int n) {
    int i, j;

    for(i = n; i > 0; i--){
        for(j = 1; j < i; j++){
            if (a[j-1] > a[j]) {
                int temp = a[j];
                a[j] = a[j - 1];
                a[j - 1] = temp;
            }
        }
    }
}

void bsort_d(int a[], int n) {
    int i, j;
    
    for(i = n; i > 0; i--){
        for(j = 1; j < i; j++){
            if (a[j-1] < a[j]) {
                int temp = a[j];
                a[j] = a[j - 1];
                a[j - 1] = temp;
            }
        }
    }
}

int main(){
    int i;
    int height[NUMBER];

    printf("Enter the number of %d students's height.\n", NUMBER);
    for(i = 0; i < NUMBER; i++){
        printf("No.%2d : ", i + 1);
        scanf("%d", &height[i]);
    }

    bsort(height, NUMBER);

    puts("Ascending Sorted.");
    for (i = 0; i < NUMBER; i++) {
        printf("No.%2d : %d\n", i + 1, height[i]);
    }

    bsort_d(height, NUMBER);

    puts("Descending Sorted.");
    for (i = 0; i < NUMBER; i++) {
        printf("No.%2d : %d\n", i + 1, height[i]);
    }

    return 0;
}