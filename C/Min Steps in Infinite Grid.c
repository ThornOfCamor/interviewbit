#include <stdio.h>
#include <stdlib.h>

int dist(int x1, int y1, int x2, int y2){

    if(x1==x2)
        if(y1>y2)
            return y1-y2;
        else
            return y2-y1;
    if(y1==y2)
        if(x1>x2)
            return x1-x2;
        else
            return x2-x1;

    if(x1>=x2 && y1>=y2){
        if(x1-x2 == y1-y2)
            return x1-x2;
        else if(x1-x2 >= y1-y2)
            return x1-x2;
        else if(y1-y2 > x1-x2)
            return y1-y2;
    }
    else if(x2>=x1 && y1>=y2){
        if(x2-x1 == y1-y2)
            return x2-x1;
        else if(x2-x1 >= y1-y2)
            return x2-x1;
        else if(y1-y2 > x2-x1)
            return y1-y2;
    }
    else if(x1>=x2 && y2>=y1){
        if(x1-x2 == y2-y1)
            return x1-x2;
        else if(x1-x2 >= y2-y1)
            return x1-x2;
        else if(y2-y1 > x1-x2)
            return y2-y1;
    }
    else if(x2>=x1 && y2>=y1){
        if(x2-x1 == y2-y1)
            return x2-x1;
        else if(x2-x1 >= y2-y1)
            return x2-x1;
        else if(y2-y1 > x2-x1)
            return y2-y1;
    }
}

int coverPoints(int* A, int n1, int* B, int n2) {
    int i, j;
    int ans = 0;
    for(i=0; i<n1-1 ; i++)
        ans += dist(A[i], B[i], A[i+1], B[i+1]);
    return ans;
}

int main(){
    int *A, *B;
    A = (int*)malloc(2*sizeof(int));
    B = (int*)malloc(2*sizeof(int));
    A[0] = 4;
    A[1] = 8;
    B[0] = 4;
    B[1] = -15;
    printf("%d\n", coverPoints(A, 2, B, 2));
    return 0;
}
