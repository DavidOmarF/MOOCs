#include <stdio.h>
#include <stdlib.h>
#define ARRSIZE 6

int* scanFile();
void sort(int* arr, int min, int max, long long* inversions);
void printArray(int* arr);

int main (void){
    long long inversions = 0;
    int* integerArray = scanFile();
    printArray(integerArray);
    sort(integerArray, 0, ARRSIZE - 1, &inversions);
    printArray(integerArray);

    printf("Inversions = %d\n", inversions);
    return 0;
}

void sort(int* arr, int min, int max, long long* inversions){
    // one number is already sorted
        if(max == min) return;

    int mid = (max + min) / 2;
    // sort left and right parts of the array
    sort(arr, min, mid, inversions);
    sort(arr, mid + 1, max, inversions);
    
    // temp array to merge to arrays
    int* temp = malloc((max-min + 1) * sizeof(int));

    // Merge two sorted arrays
    for(int i = 0, m = 0, n = 0; i <= max - min; i++){
        // concatenate whole right array if left array has no left numbers
        if(m > mid - min){
            for(; i <= max - min; i++){
                temp[i] = arr[mid + 1 + n]; n++;
            }
            break;
        }

        // concatenate whole left array if right array has no left numbers
        if(n > max - mid - 1){
            for(; i <= max - min; i++){
                temp[i] = arr[min + m]; m++;
            }
            // *inversions += (max - mid - i);
            break;
        }

        // concatenate the lower number in the "first" pos between both arrays
        if(arr[min + m] < arr[mid + 1 + n]){
            temp[i] = arr[min + m]; m++;
        } else {
            temp[i] = arr[mid + 1 + n]; n++;
            *inversions += (max - min - i);
        }
    }
    
    // copy temp array to original array
    for(int i = 0; i <= max - min; i++){
        arr[min + i] = temp[i];
    }

    free(temp);

return;
}

int* scanFile(){
    FILE *fp = fopen("integerArray.txt", "r");
    int *myVar = malloc(ARRSIZE * sizeof(int));
    int i = 0;
    while(!feof(fp)){
        fscanf(fp, "%d", &myVar[i]);
        i++;
    }
    return myVar;
}
void printArray(int* arr){
    printf("[");
    for(int i = 0; i < ARRSIZE; i++){
        printf("%d", arr[i]);
        if(i + 1 < ARRSIZE){
            printf(", ");
        }
    }
    printf("]\n");
}