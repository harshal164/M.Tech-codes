
#include<bits/stdc++.h>

using namespace std;

int n;

int head=-1,tail=-1;

void insert(int arr[]){
cout<<"enter element to insert\n";
int ele;
if (head==(tail+1)%n){
cout<<"queue is full\n";
return;
}else{
tail=(tail+1)%n;
if (head==-1)
head=0;
cin>>arr[tail];
return;
}


}


int del(int arr[]){
if ( head==-1)
{
cout<<"queue is empty\n";
return -1;
}


else{
int ele;
ele=arr[head];
if (head==tail)
head=tail=-1;
else
head=((head+1)%n);

return ele;
}}


main()
{
cout<<"enter size of array\n";
cin>>n;
int arr[n];


while(1){
int num;
cout<<"1. insert\n 2. delete \n 3. exit\n";

cin>>num;
switch(num){
case 1:
{insert(arr);
break;
}
case 2:
{cout<<del(arr);
break;
}
case 3:
exit(0);
}

};
return 0;
}
