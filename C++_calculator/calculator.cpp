
#include <iostream>
#include <iomanip>  // for formatting output
#include <limits>   // for input validation

using namespace std;

int main() {
    char operation;
    double num1, num2;

    cout << "=====================================\n";
    cout << "        Simple C++ Calculator      \n";
    cout << "=====================================\n";
    cout << "Operations available: +  -  *  /\n";
    cout << "Type 'q' anytime to quit.\n";

    while (true) {
        cout << "\nEnter operation (+, -, *, /) or q to quit: ";
        cin >> operation;

        // Exit condition
        if (operation == 'q' || operation == 'Q') {
            cout << "\nThank you for using the calculator. Goodbye! \n";
            break;
        }

        // Check valid operation
        if (operation != '+' && operation != '-' && operation != '*' && operation != '/') {
            cout << "  Invalid operation! Please use +, -, *, or /.\n";
            continue;
        }

        cout << "Enter two numbers: ";
        cin >> num1 >> num2;

        // Validate numeric input
        if (cin.fail()) {
            cout << "Invalid input! Please enter numeric values only.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        cout << fixed << setprecision(2); // show results with 2 decimal places
        double result;

        switch (operation) {
            case '+':
                result = num1 + num2;
                cout << " Result: " << result << endl;
                break;
            case '-':
                result = num1 - num2;
                cout << " Result: " << result << endl;
                break;
            case '*':
                result = num1 * num2;
                cout << " Result: " << result << endl;
                break;
            case '/':
                if (num2 == 0) {
                    cout << " Error: Division by zero is not allowed.\n";
                } else {
                    result = num1 / num2;
                    cout << " Result: " << result << endl;
                }
                break;
        }
    }

    return 0;
}
