#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int sum=0;
    for(int i=1;i<6;i++)
    {
        sum+=(n%10);
        n=n/10;
	}
    printf("%d",sum);
    return 0;
}
