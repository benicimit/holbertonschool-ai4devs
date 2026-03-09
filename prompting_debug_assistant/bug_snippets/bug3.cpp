#include <iostream>

using namespace std;

int main() {
    int numerator = 10;
    int denominator = 0;

    // Type: Runtime Exception
    // Intended Behavior: Divide two integers and print the result safely.
    // Issue: Division by zero occurs because denominator is 0.
    // Notes: Must check denominator before dividing.
    int result = numerator / denominator;

    cout << "The result of division is: " << result << endl;

    return 0;
}