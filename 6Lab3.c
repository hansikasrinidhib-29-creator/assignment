#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node *next;
};
struct node *top=NULL;

void push(){
    struct node *newnode;
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("enter the data:");
    scanf("%d",&newnode->data);
    newnode->next=NULL;
}
