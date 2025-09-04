#include<stdio.h>
int main(){
    int num1;
    int num2;
    int op;
    int sum =0;
    int diff =0;
    int mul = 0;
    int div = 0;
    printf("Enter the first number : :");
    scanf("%d",&num1);
    printf("Enter the second number : ");
    scanf("%d",&num2);
    printf("Choose Operation:\n 1.Addition\n 2.Subtraction\n 3.Multiply\n 4.Division\n");
    scanf("%d",&op);
    switch (op)
    {
    case 1:
         sum = num1+ num2;
        printf("Sum of these two numbers is :%d\n",sum);
        break;
    case 2:
         diff = num1 - num2;
        printf("Difference of these two numbers is :%d\n",diff);
        break;
    case 3:
         mul = num1 * num2;
        printf("Multiplication of these two numbers is :%d\n",mul);
        break;
    case 4:
         div = (float)num1 / num2;
        printf("Division of these two numbers is :%.2f\n",div);
        break;
    
    default:
        printf("Invalid Operation");
        break;
    }
    return 0;
}