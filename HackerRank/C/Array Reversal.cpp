#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
	/* Write the logic to reverse the array. */
	int *rev_arr;
	rev_arr = (int*) malloc(num * sizeof(int));
	for(int i=0;i<num;i++)
		*(rev_arr+i)=*(arr+num-i-1);
	free(arr);
	arr=rev_arr;
    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}
