#include <cmath>
#include <cstdio>
#include <vector>
#include<bits/stdc++.h>
using namespace std;
int cookies(int k, vector<int> A) {
    /*
     * Write your code here.
     */
    priority_queue<int,vector<int>,greater<int>> min_heap(A.begin(),A.end());
    int count=0;
    while(min_heap.top()<k && min_heap.size())
    {
        int first=min_heap.top();
        min_heap.pop();
        int second=min_heap.top();
        min_heap.pop();
        min_heap.push(first+2*second);
        count++;
    }
    if(min_heap.top()>=k)
        return count;
    return -1;
}

int main() {
	vector<int> v;
	v.push_back(1);
//	v.push_back(1);
//	v.push_back(1);
//	v.push_back(9);
//	v.push_back(10);
//	v.push_back(12);
    cout<<cookies(10,v);
    return 0;
}
