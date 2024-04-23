#include <stdio.h>
#include <stdlib.h>

void colors(){
    printf("\x1b[43;37m");
}
void laters(int i){
    printf("later %c\n",(char)i+65);

}
void numbers(int i){
    printf("number %d\n",i);

}
void stops(){
    int i=0;
    i=i+1;
}

int main(){
    int i=0;
    for(i=0;i<10;i++){
        colors();
        numbers(i);
        laters(i);
        stops();
    }
    return 0;

}
