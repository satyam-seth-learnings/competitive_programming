#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    map<string,int> records;
//    int n;
//    cin>>n;
//    for(int i=0;i<n;i++)
//    {
        int type,marks;
        string name;
        cin>>name;
        if(type==1)
        {
                cin>>marks;
                records[name]=marks;
		}
		else if(type==2)
            records.erase(name);
        else    
			cout<<records[name]<<endl;
    return 0;
}




