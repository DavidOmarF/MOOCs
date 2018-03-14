#include <cs50.h>
#include <stdio.h>

int TimeToBottles(int minutes);

int main (void){
    printf("Minutes: ");
    printf("Bottles: %i\n", TimeToBottles(get_int()));
}

int TimeToBottles(int minutes){
    return minutes * 12;
}
