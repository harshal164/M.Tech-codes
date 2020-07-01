#include<iostream>
#include<cstring>
#define MAX_SIZE 100
using namespace std;
int editDistance(char a[], char b[]){
	int a_l = strlen(a);
	int b_l = strlen(b);
	int D[a_l+1][b_l+1];
	for(int i = 0; i <= a_l; ++i){
		for(int j = 0; j <= b_l; ++j){
			if(i == 0)
				D[i][j] = j;
			else if(j == 0)
				D[i][j] = i;
			else if(a[i-1] == b[j-1])
				D[i][j] = D[i-1][j-1];
			else{
				int min = D[i-1][j-1];
				if(min > D[i-1][j])
					min = D[i-1][j];
				if(min > D[i][j-1])
					min = D[i][j-1];
				D[i][j] = 1 + min;
			}
		}
	}
	return D[a_l][b_l];
}
int main(int argc, char* argv[]){
	char a[MAX_SIZE], b[MAX_SIZE];
	cin>>a>>b;
	cout<<editDistance(a,b);
	return 0;
}
