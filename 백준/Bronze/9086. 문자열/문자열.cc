#include <stdio.h>
#include <string.h>

int main()
{
    char a[1000];
    int t;
    scanf("%d", &t);
    while(t--)
        {
            scanf("%s", a);
            int k = strlen(a);
            if(k == 1)
                printf("%c%c\n",a[0],a[0]);
            else if(k==2)
                printf("%c%c\n",a[0],a[1]);
            else
                printf("%c%c\n",a[0],a[k-1]);
        }
}