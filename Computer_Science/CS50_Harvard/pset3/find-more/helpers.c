/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
 
bool search(int value, int values[], int n)
{
    int min = 0;
    int max = n - 1;
    
    
    while(min <= max){
        
        int mid = (min + max) / 2;
        
        if(value < values[mid]){
            max = mid - 1;
        }
        
        else if(value > values[mid]){
            min = mid + 1;
        }
        
        else {
            return true;
        }
    }
    
    return false;
}

/**
 * Sorts array of n values.
 */
 
 
void sort(int values[], int n)
{
    
    int limit = 65536;
    int temp [limit];
    
    for(int values_i = 0; values_i < n; values_i++){
        temp[values[values_i]]++;
    }

    int values_i = 0;
    for(int temp_i = 0; temp_i < limit; temp_i++){
        while(temp[temp_i] > 0 && values_i < n){
            values[values_i] = temp_i;
            temp[temp_i]--;
            values_i++;
        }
    }
    
    return;
}