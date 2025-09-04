#include<stdio.h>

int main(){
    int plus[11] = {0, 1, 2, 4};
    int n, c;
    for(int i=4; i<11; i++){
        plus[i] = plus[i-3] + plus[i-2] + plus[i-1];
    }
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &c);
        printf("%d\n", plus[c]);
    }
}