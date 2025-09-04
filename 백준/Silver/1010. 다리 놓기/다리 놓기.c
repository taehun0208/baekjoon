#include<stdio.h>
int main()
{
    int n, a, b, dam;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        dam=1;
        scanf("%d %d",&a, &b);
        for(int j=0; j<a; j++)
        {
            dam*=b-j;
            dam/=1+j;
        }
        printf("%d\n", dam);
    }
}