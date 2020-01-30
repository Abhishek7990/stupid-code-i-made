#include <stdio.h>

int a;
int b;
char action;
int yeet;

int main() {
printf("First number: ");
gets ( a );

printf("Action (add): ");
gets ( action );

printf("Second number: ");
gets ( b );

if (action == "add") {
yeet = a + b;
}

printf("Output: %d", yeet);
}
