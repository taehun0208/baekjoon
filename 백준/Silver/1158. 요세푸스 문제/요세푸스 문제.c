#include<stdio.h>
#include<stdlib.h>

typedef struct list* LINK;
typedef struct list {
    int data;
    LINK next;
} list;

LINK newlist(int data) {
    LINK new = malloc(sizeof(list));
    new->data = data;
    new->next = new;
    return new;
}

void add(LINK* yose, int data) {
    LINK new = newlist(data);
    if(*yose == NULL) {
        *yose = new;
        return;
    }
    LINK temp = *yose;
    while(temp->next != *yose) {
        temp = temp->next;
    }
    temp->next = new;
    new->next = *yose;
}

void yosepus(LINK* yose, int num, int move) {
    LINK temp = *yose;
    LINK prev = temp;
    while(prev->next != temp) {
        prev = prev->next;
    }
    printf("<");
    for(int i=0; i<num; i++) {
        for(int j=0; j<move-1; j++) {
            prev = temp;
            temp = temp->next;
        }
        if(i!=0) printf(", ");
        printf("%d",temp->data);
        if(temp == temp->next) {
            free(temp);
            break;
        }
        prev->next = temp->next;
        LINK curr = temp;
        temp = temp->next;
        free(curr);
    }
    printf(">\n");
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    LINK yose = NULL;
    for(int i=1; i<=N; i++) {
        add(&yose, i);
    }
    yosepus(&yose, N, K);
}