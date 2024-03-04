#include <stdio.h>

// Define Higher / Declare Higher

void Bar();     // Forward Declaration

void Foo()
{
    printf("\nFoo");
    Bar();
}

void Bar()
{
    printf("\nBar");
}

int main()
{
    printf("\nMain");
    Foo();
    return 0;
}