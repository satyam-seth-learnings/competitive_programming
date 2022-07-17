#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int mand=0,mor=0,mxor=0;
  for(int i=1;i<n;i++)
  	for(int j=i+1;j<=n;j++)
  	{
  		int a=i&j;
		int o=i|j;
		int x=i^j;
		if(a<k && a>mand)
			mand=a;
		if(o<k && o>mor)
			mor=o;
		if(x<k && x>mxor)
			mxor=x;
	}
	printf("%d\n%d\n%d\n",mand,mor,mxor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
