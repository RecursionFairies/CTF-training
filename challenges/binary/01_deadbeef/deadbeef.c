#include <stdio.h>
#include <stdlib.h>

int main(){
    long val=0x41414141;
    char buf[20];

    printf("Give me your name, please: ");
    scanf("%24s",&buf); //Ouch!

    printf("buf: %s\n",buf);
    printf("val: 0x%08x\n",val);

    if(val==0xdeadbeef){
        printf("Well done\n");
        exit(0);
    }
    else {
        printf("No way man!\n");
        exit(1);
    }

    return 0;
}
