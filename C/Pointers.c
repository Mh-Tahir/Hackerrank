// Reads two integers as argument, and sets a with the sum of them, and b with the absolute difference of them.
#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    *a = *a + *b;
    *b = abs(*a - *b - *b);    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
