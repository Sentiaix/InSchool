#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int no, width;

    printf("How much print? ");      scanf("%d", &no);
    printf("\\n? "); scanf("%d", &width);

    if (no > 0){
        int i, j;
        int rem = no % width;
        int wid = width / 2;
        int odd = width % 2;
        for(i = 0; i < no / width; i++){
            for(j = 0; j < wid; j++){
                printf("+-");
            }
            printf("\n");
            for(j = 0; j < wid; j++){
                printf("-+");
            }
            printf("\n");
        }
        if (no / width %2){
        for(j = 0; j < wid; j++){
            printf("+-");
        }
        printf("\n");
        }
        if (rem > 0){
            switch (no / width % 2){
                case 0 :
                    for(j = 0; j < rem / 2; j++){
                        printf("+-");
                    }
                    if (rem % 2) putchar('+');
                    break;
                case 1 :
                    for(j = 0; j < rem / 2; j++){
                        printf("-+");
                    }
                    if (rem % 2) putchar('-');
                    break;
            }
            printf("\n");
        }
    }


    return 0;
}