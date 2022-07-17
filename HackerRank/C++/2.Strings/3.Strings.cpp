#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin>>a>>b;
    cout<<a.size()<<" "<<b.size()<<endl;
    cout<<a+b<<endl;

//    Logic-1
//    char c=a[0];
//    a[0]=b[0];
//    b[0]=c;

//	Logic-2
	swap(a[0],b[0]);
	
    cout<<a<<" "<<b;
    return 0;
}
