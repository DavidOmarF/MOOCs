#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

string Cipher(string plaintext, string key);
int GetKey (char key);
int checkKey(string key);

int main (int argc, char* argv[]){
    
    if (argc != 2){
        printf("Usage: ./vigenere k\n");
        return 1;
    }
    
    if(checkKey(argv[1])){
        printf("Keyword must only contain letters A-Z and a-z\n");
        return 1;
    }
    
    printf("plaintext: ");
    string plaintext = get_string();

    printf("ciphertext: %s\n", Cipher(plaintext, argv[1]));
    

    return 0;
}

string Cipher(string plaintext, string key){
    
    int n = strlen(key);
    
    for (int j = 0; j < n; j++){
        key[j] = GetKey(key [j]);
    }
    
    for(int i = 0, j = 0, plainLen = strlen(plaintext); i < plainLen; i++){

        if (j == n) j = 0;

        if (plaintext[i] >= 'a' && plaintext[i] <= 'z'){
            plaintext[i] = (plaintext[i] - 'a' + key[j]) % 26 + 'a';
            j++;
        } 
        
        else if (plaintext[i] >= 'A' && plaintext[i] <= 'Z'){
            plaintext[i] = (plaintext[i] - 'A' + key[j]) % 26 + 'A';
            j++;
        }
    }
    
    return plaintext;
}

int GetKey (char key){
    
    if (key >= 'a' && key <= 'z')
            return key - 'a';
            
    if (key >= 'A' && key <= 'Z')
            return key - 'A';

    return key;
}

int checkKey(string key){
    for(int i = 0, n = strlen(key); i < n; i++){
        if(key[i] < 'A' || (key[i] > 'Z' && key[i] < 'a') || key[i] > 'z'){
            return 1;
        }
    }
    
    return 0;
}
