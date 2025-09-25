#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int n1, n2, n3;
    scanf("%d %d %d", &n1, &n2, &n3);

    if ((n1 <= n2 && n2 <= n3) || (n3 <= n2 && n2 <= n1)){
        printf("%d\n", n2);
    }
    if ((n2 <= n1 && n1 <= n3) || (n3 <= n1 && n1 <= n2)){
        printf("%d\n", n1);
    }
    if ((n1 <= n3 && n3 <= n2) || (n2 <= n3 && n3 <= n1)){
        printf("%d\n", n3);
    }



    // for(int i = 0; i < 3; i++){
    //     for(int j = 0; j < 3 - i; j++){
    //         if(arr[j] > arr[j + 1]){
    //             int temp = arr[j];
    //             arr[j] = arr[j + 1];
    //             arr[j + 1] = temp;
    //         }
    //     }
    // }

    return 0;
}