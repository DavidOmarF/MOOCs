#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int StringToInt(string argv);
string Cipher(string plaintext, int key);

int main (int argc, char* argv[]){
    
    if (argc != 2){
        printf("Usage: ./caesar k\n");
        return 1;
    }
    
    int key = StringToInt(argv[1]);

    printf("plaintext: ");
    string plaintext = get_string();

    printf("ciphertext: %s\n", Cipher(plaintext, key));
    

    return 0;
}

string Cipher(string plaintext, int key){
    for(int i = 0, len = strlen(plaintext); i < len; i++){
       
        if(plaintext[i] >= 'A' && plaintext[i] <= 'Z'){
            plaintext[i] = (plaintext[i] + key - 65) % 26 + 65;
        } 
        
        else if (plaintext[i] >= 'a' && plaintext[i] <= 'z'){
            plaintext[i] = (plaintext[i] + key - 97) % 26 + 97;
        }
    }
    return plaintext;
}

int StringToInt(string argv){
    
    int numericValue = 0;
    
    for (int i = strlen(argv) - 1, j = 1; i >= 0; i--, j *= 10){
        numericValue += (argv[i] - 48) * j;
    }

    return numericValue;
}
