#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int sum = 0;
    int n = sizeof(arr) / sizeof(arr[0]);

    // Intended to calculate the sum of the array
    // Bug: Logical error - using multiplication instead of addition
    for(int i = 0; i < n; i++) {
        sum *= arr[i];  // Should be sum += arr[i]
    }

    printf("Sum of array elements: %d\n", sum);
    return 0;
}