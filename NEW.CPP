#include<iostream.h>
#include<conio.h>

void main()
{
int n,t,k,c;
int a[10],b[10];
clrscr();
cout<<"enter the number of arrays";
cin>>t;
cout<<"enter the size of the array";
cin>>n;
cout<<"enter the first array";
for(int i=0; i<n; i++)
{
cin>>a[i];
}
cout<<"enter the second array";
for(int j=0; j<n; j++)
{
cin>>b[j];
}
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(a[i]==b[j])
{
c=j-i;
if(c<0)
{
c=-c;
}
cout<<c;
}
}
}
getch();
}
