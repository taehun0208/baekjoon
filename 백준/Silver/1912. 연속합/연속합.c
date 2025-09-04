#include<stdio.h>

int main(){
    int n[100001], d;
    scanf("%d", &d);
    for(int i=0; i<d; i++){
        scanf("%d", &n[i]);
    }
    int max = n[0];
    for(int i=1; i<d; i++){
        if(n[i-1]>0 && n[i-1] + n[i] > 0){
            n[i]+=n[i-1];
        }
        if(max<n[i]){
            max = n[i];
        }
    }
    
    printf("%d", max);

    return 0;
}