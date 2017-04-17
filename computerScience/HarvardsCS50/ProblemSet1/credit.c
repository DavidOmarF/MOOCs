#include <cs50.h>
#include <stdio.h>
#include <math.h>

void CardNumberToString(long long cardNumber, int* numbers, int numDigits);
int CardSum(int* numbers, int numDigits);
void CardProvider(int first, int second);
int FindNumDigits(long long lowerBound, long long cardNumber);

int main (void){
    
    printf("Credit card number: ");
    long long cardNumber = get_long_long(), lowerBound = pow(10, 13);
    
    int numDigits = FindNumDigits(lowerBound, cardNumber);
    
    if (numDigits < 13 || numDigits > 16){
        printf("INVALID\n");
        return 1;
    }

    int* numbers;
    numbers = malloc(numDigits * sizeof(int));
    
    CardNumberToString(cardNumber, numbers, numDigits);
    
    int cardSum = CardSum(numbers, numDigits);
    
    if(cardSum % 10 == 0){
        CardProvider(numbers[numDigits - 1], numbers[numDigits - 2]);
        printf("\n");
        return 0;
    } 
    
    printf("INVALID\n");
    return 0;

}


void CardProvider(int first, int second){
    
    if(first == 4){
        printf("VISA");
        return;
    } else if(first == 3 && (second == 4 || second == 7)){
        printf("AMEX");
        return;
    } else if( first * 10 + second >= 51 && first * 10 + second <= 55){
        printf("MASTERCARD");
    } else {
        printf("INVALID\n");
    }
}


void CardNumberToString(long long cardNumber, int* numbers, int numDigits){
    
    long long base = 1;
    long long restante = 0;
    
    for (int j = 0; j < numDigits; base *= 10, j++){
        
        for (int i = 0; i <= 9; i++){
            
            if ((cardNumber - i * base) % (base * 10) == restante){
                numbers[j] = i;
                restante += numbers[j] * base;
            }
            
        }
        
    }
}


int CardSum(int* numbers, int numDigits){
    int lastSum = 0;
    
    for (int i = 1; i < numDigits; i += 2){
        
        if(numbers[i] < 5) {
            lastSum += numbers[i] * 2;            
        } 
        
        else {
            lastSum += 1 + (numbers[i] * 2 % 10);
        }
        
    }
    
    for(int i = 0; i < numDigits; i += 2){
        lastSum += numbers[i];
    }
    
    return lastSum;
}


int FindNumDigits(long long lowerBound, long long cardNumber){
    
    int numDigits = 13;
    for (; numDigits < 16; lowerBound *= 10, numDigits++){
        if(cardNumber % lowerBound == cardNumber){
            break;
        }
    }    
    
    return numDigits;
}
