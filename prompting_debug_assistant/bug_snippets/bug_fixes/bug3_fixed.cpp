#include <iostream>
using namespace std;

int main() {
    int numerator = 10;
    int denominator = 0;  // This will cause division by zero

    // Type: Runtime Error
    // Intended Behavior: Perform division and print the result.
    // Issue: Division by zero when denominator is 0.
    // Notes: Should check if denominator is zero before dividing.
    if (denominator != 0) {
        double result = static_cast<double>(numerator) / denominator;
        cout << "Result: " << result << endl;
    } else {
        cout << "Error: Division by zero is not allowed." << endl;
    }

    return 0;
}