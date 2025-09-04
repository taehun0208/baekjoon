#include<stdio.h>

int dp[2001][2001];

int main()
{
    int N, M;
    scanf("%d", &N);
    int arr[N+1], a, b;
    for(int i=1; i<=N; i++)
    {
        scanf("%d", &arr[i]);
        dp[i][i] = 1;
        if(i>1 && arr[i] == arr[i-1]) dp[i-1][i] = 1; 
    }

    for(int len=2; len<N; len++)
        for(int a=1; (b=len+a) <= N; a++)
            if(arr[a]==arr[b] && dp[a+1][b-1]) dp[a][b] = 1;

    scanf("%d", &M);
    for(int i=0; i<M; i++)
        {
            scanf("%d %d", &a, &b);
            printf("%d\n", dp[a][b]);
        }

}