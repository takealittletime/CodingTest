#include <stdio.h>

int main() {
    int t;
    int arr[1000000] = { 0 };
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++)
    {
        int a = 0, b = 0;
        scanf("%d %d", &a, &b);
        arr[i] = a + b;
    }

    for (int i = 0; i < t; i++)
    {
        printf("%d\n", arr[i]);
    }

    return 0;
}