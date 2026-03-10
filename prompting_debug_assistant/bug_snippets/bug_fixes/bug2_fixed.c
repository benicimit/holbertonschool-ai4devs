#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int sum = 0;
    int n = sizeof(arr) / sizeof(arr[0]);

    // Type: Logical Error
    // Intended Behavior: Calculate the sum of all elements in the array.
    // Issue: Using multiplication assignment instead of addition.
    // Notes: Should accumulate with += rather than *=.
    for(int i = 0; i < n; i++) {
        sum += arr[i];  // Fixed: changed *= to +=
    }

    printf("Sum of array elements: %d\n", sum);
    return 0;
}