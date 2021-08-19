// Demonstrate addition of two floating type numbers by using call by address

#include<iostream>
using namespace std;


double sumd(double *x, double *y) {
    double sum = *x + *y;
    return sum;
}


int main() {
    double a = 10.5, b = 5.2, sum;
    sum = sumd(&a, &b);
    cout << "sum of " << a << " and " << b << " is " << sum;
}