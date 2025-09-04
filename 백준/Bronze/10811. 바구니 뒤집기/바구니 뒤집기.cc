#include <stdio.h>

int main()
{
    int arr[101] = {0};
    int n, m, a, b, ck = 0;
    scanf("%d %d", &n,&m);
    for(int i=1; i<=n; i++)
        {
            arr[i] = i;
        }
    for(int i=0; i<m; i++)
        {
            scanf("%d %d", &a, &b);
            for(int k=a; k<b; k++)
                {
                    ck = arr[k];
                    arr[k] = arr[b];
                    arr[b] = ck;
                    b--;
                }
        
        }
    for(int i=1; i<=n; i++)
        {
           printf("%d ",arr[i]);
        }
}