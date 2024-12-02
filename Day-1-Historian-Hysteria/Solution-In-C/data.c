#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>

#define MAXCHAR 1000

int main()
{
    FILE *fp;
    char row[MAXCHAR];
    char *token;

    fp = fopen("../test.txt","r");
    if (fp == NULL) 
    {
        printf("The file is not opened. The program will "
               "now exit.");
        exit(0);
    }
    else {
        while (fgets(row, 50, fp) != NULL) {
            // printf("%s", row);
        
            char *token = strtok(row, "   "); // Split the row using comma as delimiter
    
            char *arr1 = strdup(token);
            row[strcspn(row, "\n")] = 0;
            // printf("%s\n", row);
            printf("%s\n", arr1);
        }
        fclose(fp);
    }
    return 0;

}

