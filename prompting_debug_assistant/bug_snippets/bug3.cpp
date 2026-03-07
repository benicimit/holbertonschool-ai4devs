#include <iostream>

using namespace std;

int main() {
    int numerator = 10;
    int denominator = 0;

    // Intended to perform division and print the result
    // Bug: Runtime exception - division by zero
    int result = numerator / denominator;

    cout << "The result of division is: " << result << endl;

    return 0;
}