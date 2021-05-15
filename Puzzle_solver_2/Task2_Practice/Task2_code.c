#include <stdio.h>
 #include <string.h>
int D1[12],D2[4][2],i=0,j,k;
 
 void puzzle()
 {
 	
 	
 	
 	
 	
 }
 
 
 int main()
 
 {
 
 
 char str3[20]=".txt";
 for(k=0;k<3;k++)
 {
char str1[20]="Test_input";
 str1[10]=k+48;
 strcat(str1,str3);
 	printf("%s",str1);
 	
 FILE* in_file = fopen( str1, "r"); // read only  
         
          if (! in_file ) // equivalent to saying if ( in_file == NULL ) 
             {  
                printf("oops, file can't be read\n"); 
             return 0;
             } 
 
          // attempt to read the next line and store 
          // the value in the "number" variable 
          for (i = 0; i < 12; i++)
    {
        fscanf(in_file, "%d", &D1[i]);
       
    }
j=0;
i=0;
          while ( fscanf(in_file, "%d", & D2[i][j] ) == 1 )  
             { 
               
			   if(j==1)
			   {
			   	i++;j=0;
				} 
				else
				j++;
             }
             
             puzzle();
         }
             return 0;
}			 

