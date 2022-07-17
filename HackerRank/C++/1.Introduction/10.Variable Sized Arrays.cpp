#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,q;
    cin>>n>>q;
    vector <vector <int> > vect;
    for(int i=0;i<n;i++)
    {
        int s;
        cin>>s;
        vector <int> temp;
        for(int j=0;j<s;j++)
        {
            int value;
            cin>>value;
            temp.push_back(value);
        }
        vect.push_back(temp);
    }
    for(int i=0;i<q;i++)
    {
        int r,c;
        cin>>r>>c;
        cout<<vect[r][c]<<endl;
    }
    return 0;
}

