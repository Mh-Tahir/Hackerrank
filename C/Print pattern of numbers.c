/*
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
*/
#include <stdio.h>

int main() 
{
    int n;
    scanf("%i", &n);
  	for (int row = 0; row < 2 * n - 1; row++) 
    {
        for (int col = 0; col < 2 * n - 1; col++) 
        {
            int min = row < col ? row : col;
            min = min < 2 * n - 1 - row ? min : 2 * n - 1 - row - 1;
            min = min < 2 * n - 1 - col - 1 ? min : 2 * n - 1 - col - 1;
            printf("%i ", n - min);
        }
        printf("\n");
    }
    return 0;
}
