// Write a C program to compute sum of diagonal elements of an array

#include<stdio.h>

int main() {

    int arr[3][3] = {
        {1, 2, 3},
        {4, 2, 1},
        {5, 4, 2}
    };

    int x = sizeof(arr[0]) / sizeof(int);
    int s = 0;
    for(int i = 0; i < x; i++) {
        for (int j =0; j < x; j++) {
            if (i == j) {
                s += arr[i][j];
            }
        }
    }

    printf("Sum of diagonal ele is %d", s);
}
