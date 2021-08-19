// Write a program that declares a double, an int, and char variables. Next declare and initialize a pointer to each of the three variables. Your program should then print the address of, and value stored in.
#include<iostream>
using namespace std;

int main(){

    int a = 10;
    char b = 'a';
    double c = 152.93;

    int *aa = &a;
    char *bb = &b;
    double *cc = &c;

    cout << "int Value: " << *aa << " Address: " << aa << endl;
    b = 'c';
    cout << "char Value: " << *bb << " Address: " << bb << endl;
    cout << "double Value: " << *cc << " Address: " << cc << endl;
}



