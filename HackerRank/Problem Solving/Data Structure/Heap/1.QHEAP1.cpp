#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    set<int> heap;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
    	set<int>::iterator it;
        int choice,val;
        cin>>choice;
        switch(choice)
        {
            case 1:
                cin>>val;
                heap.insert(val);
                break;
            case 2:
                cin>>val;
                it=heap.find(val);
                heap.erase(it);
                break;
            case 3:
                cout<<*heap.begin()<<endl;
                break;
        }
    }
    return 0;
}
