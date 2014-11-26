//John Feehley
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main (int argc, char* argv[]) {if (argc < 3) {return 1;}int x; x = strcmp(argv[1], argv[2]);if (x > 0){return 1;}else if(x < 0){return 1;} else{return 0;}}
