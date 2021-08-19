// Demonstrate pointer arithmetic by assigning pointer “ptr” to variable “a” which is having value as 100 in it.Perform increment operation on pointer ptr like ptr=ptr+2 and display which address that pointer ptr hold

#include<iostream>
using namespace std;

int main() {
    int a = 100;
    int *ptr = &a;
    cout << "pointer arithmatics" << end;
    cout << ptr << " and " << ptr + 1 << endl;
}