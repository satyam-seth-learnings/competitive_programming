#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    set<int> s;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int op,val;
        cin>>op>>val;
        switch(op)
        {
            case 1:
               s.insert(val) ;
               break;
            case 2:
                s.erase(val);
                break;
            case 3:
                auto fval=s.find(val);
                if(fval!=s.end())
                    cout<<"Yes"<<endl;
                else
                    cout<<"No"<<endl;
                break;
        }
    }
    return 0;
}




