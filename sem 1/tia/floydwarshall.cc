#include<iostream>
#include<climits>
#define s 10
using namespace std;
void fw(int A[s][s], int v){
	for(int i = 0; i < v; ++i){
		for(int j = 0; j < v; ++j){
			for(int k = 0; k < v; ++k){
				for(int l = 0; l < v; ++l){
					if(A[j][k] > A[j][l] + A[l][k]){
						A[j][k] = A[j][l] + A[l][k];
					}
				}
			}
		}
	}
}
int main(int argc, char* argv[]){
	int A[s][s], v, i ,j;
	cin >> v;
	for(i = 0; i < v; ++i){
		for(j = 0; j < v; ++j){
			cin >> A[i][j];
			if(A[i][j] == 0 && i != j)
				A[i][j] = 5555;
		}
	}
	fw(A,v);
	for(i = 0; i < v; ++i){
		for(j = 0; j < v; ++j){
			cout<<A[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
