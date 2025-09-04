#include<stdio.h>

int main()
{
    int n, m;
    int fibo[41] = { 0 , 1 };
    scanf("%d",&n);
    
    for(int i=2; i<=40;i++) fibo[i] = fibo[i-2] + fibo[i-1];
    for(int i=0; i<n; i++){
        scanf("%d",&m);
        if(m==0) printf("1 0\n");
        else printf("%d %d\n",fibo[m-1], fibo[m]);
    }
}