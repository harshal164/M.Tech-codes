#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#define ds 1000
/***************/
/*ds = datasize*/
/***************/

using namespace std;

void init(){
	srand(time(0));
}
int randno(int mod){
	return rand()%mod;
}
int cal_dig(int n){
	int d = 0;
	do{
		n/=10;
		++d;
	}while(n);
	return d;
}
void randomise(int arr[], int s){
	int *indices = new int[s], ctr = s, i, j;
	for(i = 0; i < s; ++i){
		indices[i] = 1;
	}
	while(ctr > 1){
		i = j = randno(s);
		while(i == j){
			j = randno(s);
		}
		if(indices[i]&&indices[j]){
			arr[i] = arr[i]^arr[j];
			arr[j] = arr[i]^arr[j];
			arr[i] = arr[i]^arr[j];
			indices[i] = indices[j] = 0;
			ctr-=2;
		}
	}
	delete [] indices;
}
void swap(int &a, int &b){
	if(&a != &b){
		a = a ^ b;
		b = a ^ b;
		a = a ^ b;
	}
}
//*-*-*-*-*-*-*-*-*-*-*-*-*//
void quicksort(int [], int);
void quick_sort(int [], int, int);
int partition(int [], int, int);

int main(int argc, char* argv[]){
	int d[ds], s, i, c=0;
	init();
	cin >> s;
	if(s > ds){
		cout << "Datasize too big";
		return -1;
	}
	for(i = 0; i < s; ++i){
		cin >> d[i];
	}
	/*randomise(d,s);
	for(i = 0; i < s; ++i){
		cout << d[i] << ", ";
	}
	cout << "\b\b \b\n";*/
	
	/**************/
	/*****Menu*****/
	/**************/

	while(c!=4){
		cout << "1. Quick sort \n\
			\r2. Randomize data \n\
			\r3. View data \n\
			\r4. Exit \n";
		cin >> c;
		switch(c){
			case 1:quicksort(d,s);break;
			case 2:randomise(d,s);break;
			case 3:for(i = 0; i < s; ++i){
					cout << d[i] << ", ";
				}
				cout << "\b\b \b\n";
			default:;
		}
	}
	return 0;
}
void quicksort(int arr[], int s){
	quick_sort(arr, 0, s - 1);
}
void quick_sort(int arr[], int l, int r){
	int p;
	if(l < r){
		p = partition(arr, l, r);
		quick_sort(arr, l, p - 1);
		quick_sort(arr, p + 1, r);
	}
}
int partition(int arr[], int l, int r){
	int i = l + randno(r - l + 1), p = l - 1;
	swap(arr[i], arr[r]);
	for(i = l; i < r; ++i){
		if(arr[i] <= arr[r]){
			++p;
			swap(arr[i], arr[p]);
		}
	}
	++p;
	swap(arr[p], arr[r]);
	return p;
}
