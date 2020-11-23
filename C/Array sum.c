// inputs the elements of the array and prints the sum of the elements
#include <stdio.h>

int main() {
    int n;
    scanf("%i", &n);
    int a[n];
    int s = 0;
    for (int i; i < n; i++)
    {
        scanf("%i ", &a[i]);
        s += a[i];
    }
    printf("%i\n", s);
}
