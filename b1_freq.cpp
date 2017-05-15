#include<stdlib.h> //System() Function
#include<iostream>  //cout , cin
#include<string>    //string
#include <time.h>

using namespace std;
long long int fact(int num);
void matmul();
int main()
{
int option=1;
string frq;
string command;

while(option!=4)
{

cout <<  "1.  Press 1 to set the Beagle Board CPU Frequency\n";
cout <<  "2.  Press 2 to get the current CPU Frequency\n";
cout <<  "3.  Press 3 to execute Function and check time\n";
cout <<	 "4.  To Exit\n";
cin >>  option;
float st;

switch(option)
        {
        case 1:
                cout << "Please Enter the frequency in range 100-1000 (MHz)\n";
                cin >>  frq;
                command="cpufreq-set -f "+frq+"MHz";

                if(system(command.c_str()))
                	cout << "\nCannot Set the Frequency. Make sure logged in as ROOT\n";



        case 2:
                        system("cpufreq-info | tail -2");
                        break;

        case 3:
                cout<<"Frequency is:\t";
                system("cpufreq-info | tail -2");

                st=clock();

                long long int f=fact(50);

                cout<<"\nTime required=\t"<<((float)clock()-st)/1000000<<" seconds\n";

                break;

        case 4:	cout<<"Exiting...\n";
        	break;
        }
        }
}
long long int fact(int num)
{
        
        if(num==1||num==0)
		return 1;
	else if(num > 0)
		return (num * fact(n-1))		
	
}
void matmul()
{
	int a[50*50],b[50*50],c[50*50];
	int n=50;
	
	for (int i=0;i<n*n;i++)
		a[i]=rand()%10;	
	for (int i=0;i<n*n;i++)
		b[i]=rand()%10;	
	for (int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			c[i*n+j]=0;
			for(int k=0;k<n;k++)
				c[i*n+j] += a[i*n+k]*b[k*n+j];
		}
}

