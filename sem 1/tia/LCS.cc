#include<iostream>
#include<cstring>
#define MAX_SIZE 100
#define UP 2
#define DIAG 1
#define SLIDE 3
using namespace std;
void printlcs(int t[][MAX_SIZE],char a[], int m, int n){
	if(m == 0 || n == 0)
		return;
	if(t[m-1][n-1]==DIAG){
		printlcs(t,a,m-1,n-1);
		cout<<a[m-2];
	}
	else if(t[m-1][n-1]==UP)
		printlcs(t,a,m-1,n);
	else if(t[m-1][n-1] == SLIDE)
		printlcs(t,a,m,n-1);
}
void LCS(char a[], char b[]){
	int m = strlen(a);
	int n = strlen(b);
	int l[m+1][n+1],
		track[MAX_SIZE][MAX_SIZE],
		i;
	for(i = 0; i <= m; ++i){
		for(int j = 0; j <= n; ++j){
			if(i==0 || j==0)
				l[i][j] = 0;
			else if(a[i-1] == b[j-1]){
				l[i][j] = l[i-1][j-1] + 1;
				track[i][j] = DIAG;
			}
			else if(l[i-1][j] >= l[i][j-1]){
				l[i][j] = l[i-1][j];
				track[i][j] = UP;
			}
			else{
				l[i][j] = l[i][j-1];
				track[i][j] = SLIDE;
			}
		}
	}
	for(i = 0; i <= m; i++){
		for(int j = 0; j <= n; ++j){
			if(track[i][j] == UP){
				cout<<"UP\t";
			}
			else if(track[i][j] == DIAG){
				cout<<"DIAG\t";
			}
			else if(track[i][j] == SLIDE)
				cout<<"SLIDE\t";
			else
				cout<<"\t";
		}
		cout<<endl;
	}
	cout<<"LCS Length = "<<l[m][n]<<endl;
	printlcs(track,a,m+1,n+1);
}
int main(int argc, char* argv[]){
	char a[MAX_SIZE],b[MAX_SIZE];
	cin>>a>>b;
	a[MAX_SIZE-1]='\0';//to avoid overflow
	b[MAX_SIZE-1]='\0';//to avoid overflow
	LCS(a,b);
	return 0;
}
