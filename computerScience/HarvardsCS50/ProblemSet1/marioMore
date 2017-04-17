#include <cs50.h>
#include <stdio.h>

int main (void){
    printf("Height: ");
    int height = get_int();
    while (height > 23 || height < 0){
        printf("Height: ");
        height = get_int();
    }

    for (int i = 1; i <= height; i++){
        for (int spaces = 0; spaces < height - i; spaces++){
            printf(" ");
        }
        for (int hash = height; hash > height - i; hash--){
            printf("#");
        }
        
        printf("  ");
        
        for (int hash = height; hash > height - i; hash--){
            printf("#");
        }
        
        printf("\n");
        
    }
}
