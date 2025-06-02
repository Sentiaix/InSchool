    #include <stdio.h>
    // replit.com

    typedef struct book{
        char title[128];
        char author[128];
        int page;
        int price;
    } BOOK;

    int main(){
        BOOK lib[64];
        int num;
        char cmmd[128];

        printf("Save book or Load book S/L? "); // 가능한 input: save,Save,s,S,l,L, etc..
        scanf("%s", cmmd);

        if( cmmd[0]=='s' || cmmd[0]=='S'){

            printf("How many books? ");
            scanf("%d", &num);

            //?? coding here
            for(int i = 0; i < num; i++){
                printf("Enter title author page price: ");
                scanf("%s %s %d %d", lib[i].title, lib[i].author, &lib[i].page, &lib[i].price);
            }

            printf("Enter save name: ");
            char save_name[128];
            scanf("%s", save_name);
            //?? coding here
            FILE *fp = fopen(save_name, "wb");
            fwrite(lib, sizeof(BOOK), num, fp); // lib의 size는 264 * 64, BOOK의 size는 128 + 128 + 4 + 4 = 264

            fclose(fp);

        }

        else{

            printf("How many books? ");
            scanf("%d", &num);

            char load_name[128];

            printf("Enter load name: ");
            scanf("%s", load_name);

            // ?? coding here
            FILE *fp = fopen(load_name, "rb");
            printf("debug? file open: %p\n", fp);
            fread(lib, sizeof(BOOK), num, fp);
            fclose(fp);

            for(int i = 0; i < num; i++){
                printf("%s %s %d %d\n", lib[i].title, lib[i].author, lib[i].page, lib[i].price);
            }

        }

    }