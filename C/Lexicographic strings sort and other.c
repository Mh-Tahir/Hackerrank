// sort the strings in lexicographically non-decreasing order.
// sort the strings in lexicographically non-increasing order.
// sort the strings in non-decreasing order of the number of distinct characters present in them. 
// If two strings have the same number of distinct characters present in them, then the lexicographically smaller string should appear first.
// sort the strings in non-decreasing order of their lengths. 
// If two strings have the same length, then the lexicographically smaller string should appear first.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(b, a);
}

#define CHARS   26
int distinct_chars(const char *a)
{
    int dist = 0;
    int chars[CHARS] = {0};

    while (*a != '\0') {
        int chr = (*a++) - 'a';
        if (chr < CHARS)
            chars[chr]++;
    }
    
    for (int i = 0; i < CHARS; i++)
        if (chars[i])
            dist++;

    return dist;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int res = distinct_chars(a) - distinct_chars(b);
    return (res) ? res : lexicographic_sort(a, b);
}

int sort_by_length(const char* a, const char* b) {
    int res = strlen(a) - strlen(b);
    return (res) ? res : lexicographic_sort(a, b);
}

void string_sort(char** arr, const int len,int (*cmp_func)(const char* a, const char* b)) {
    int sorted = 0;
    int top = len - 1;
    while (!sorted) {
        sorted = 1;
        for (int i = 0; i < top; i++) {
            if (cmp_func(arr[i], arr[i + 1]) > 0) {
                char *tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
                sorted = 0;
            }
        }
        top--;
    }
}

int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
