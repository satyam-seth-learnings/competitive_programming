#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    vector<int> v;
    int n,num;
    cin>>n;
    for(int i=0;i<n;i++)
    {
    	cin>>num;
    	v.push_back(num);
	}
	int r1,r2,r3;
	cin>>r1;
	cin>>r2>>r3;
	v.erase(v.begin()+r1-1);
	v.erase(v.begin()+r2-1,v.begin()+r3-1);
	cout<<v.size()<<endl;
	for(int i=0;i<v.size();i++)
    	cout<<v.at(i)<<" ";
    return 0;
}
