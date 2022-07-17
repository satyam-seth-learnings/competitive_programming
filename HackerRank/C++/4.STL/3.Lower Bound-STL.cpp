#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin>>n;
    vector<int> v; 
    for(int i=0;i<n;i++)
    {
        int ele;
        cin>>ele;
        v.push_back(ele);
    }
    int q;
    cin>>q;
    for(int i=0;i<q;i++)
    {
        int query;
        cin>>query;
        auto pos=lower_bound(v.begin(),v.end(),query);
        if (v[pos-v.begin()]==query)
           cout<<"Yes "<<(pos-v.begin()+1)<<endl;
        else
           cout<<"No "<<(pos-v.begin()+1)<<endl;
   }
    return 0;
}

