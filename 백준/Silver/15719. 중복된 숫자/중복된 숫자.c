#include<stdio.h>

int main()
{
    int N, num;
    unsigned long long sum=0;
    scanf("%d", &N);
    for(int i=0; i<N; i++)
    {
        scanf("%d", &num);
        sum+=num;
        sum-=i;
    } 
    printf("%llu", sum);
}