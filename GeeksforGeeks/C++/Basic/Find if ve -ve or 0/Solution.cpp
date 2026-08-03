#include <iostream>
using namespace std;

int main() {
    // Take a as input
    int a;
    cin >> a;
    if (a == 0){
        cout << "Zero";
    }
    else if (a > 0){
        cout << "Positive";
    }
    else{
        cout <<"Negative";
    }
    return 0;
}