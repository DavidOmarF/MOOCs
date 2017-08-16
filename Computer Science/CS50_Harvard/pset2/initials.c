#include <stdio.h>
#include <cs50.h>
#include <string.h>

char Mayus(char letter);

int main (void){

    string fullName = get_string();
    
    if(fullName [0] != ' ')
        printf("%c", Mayus(fullName[0]));
    for(int i = 1; i < strlen(fullName); i++){
        if(fullName[i] == ' '){
            continue;
        } else if(fullName[i - 1] == ' '){
            printf("%c", Mayus(fullName[i]));
        }
        
    }
    
    printf("\n");
    return 0;
}

char Mayus(char letter){
    if(letter >= 97 && letter <= 122)
        return letter - 32;
    return letter;
}
