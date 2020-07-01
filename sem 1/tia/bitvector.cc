#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;
struct set{
	int id,
	    b[8]; //elements from 0 to 255
};
void output(set s[], int n){
	for(int i = 0; i < n; ++i){
		cout<<s[i].id<<": ";
		for(int j = 0; j < 256; ++j){
			if(s[i].b[j/32] & (1 << (j%32)))
				cout<<j<<" ";
		}
		cout<<endl;
	}
}
void _union(set *s,int &n,int i1,int i2, int &max, int &ids){
	int i, pos1, pos2;
	set *tmp;
	for(i = 0; i < n; ++i){
		if(s[i].id == i1)
			pos1 = i;
		if(s[i].id == i2)
			pos2 = i;
	}
	if(n >= max){
		max = 2 * max;
		tmp = new set[max];
		for(i = 0; i < n; ++i){
			tmp[i].id = s[i].id;
			for(int j = 0; j < 8; ++j){
				tmp[i].b[j] = s[i].b[j];
			}
		}
		delete [] s;
		s = tmp;
	}
	s[n].id = ids++;
	for(i = 0; i < 8; ++i){
		s[n].b[i] = s[pos1].b[i] | s[pos2].b[i];
	}
	n++;
}
void _inter(set *s,int &n,int i1,int i2, int &max, int &ids){
	int i, pos1, pos2;
	set *tmp;
	for(i = 0; i < n; ++i){
		if(s[i].id == i1)
			pos1 = i;
		if(s[i].id == i2)
			pos2 = i;
	}
	if(n >= max){
		max = 2 * max;
		tmp = new set[max];
		for(i = 0; i < n; ++i){
			tmp[i].id = s[i].id;
			for(int j = 0; j < 8; ++j){
				tmp[i].b[j] = s[i].b[j];
			}
		}
		delete [] s;
		s = tmp;
	}
	s[n].id = ids++;
	for(i = 0; i < 8; ++i){
		s[n].b[i] = s[pos1].b[i] & s[pos2].b[i];
	}
	n++;
}
void diff(set *s,int &n,int i1,int i2, int &max, int &ids){
	int i, pos1, pos2;
	set *tmp;
	for(i = 0; i < n; ++i){
		if(s[i].id == i1)
			pos1 = i;
		if(s[i].id == i2)
			pos2 = i;
	}
	if(n >= max){
		max = 2 * max;
		tmp = new set[max];
		for(i = 0; i < n; ++i){
			tmp[i].id = s[i].id;
			for(int j = 0; j < 8; ++j){
				tmp[i].b[j] = s[i].b[j];
			}
		}
		delete [] s;
		s = tmp;
	}
	s[n].id = ids++;
	for(i = 0; i < 8; ++i){
		s[n].b[i] = s[pos1].b[i] & ~(s[pos2].b[i]);
	}
	n++;
}
void merge(set *s,int &n,int i1,int i2){
	int i, pos1, pos2;
	if(i1 == i2)
		return;
	for(i = 0; i < n; ++i){
		if(s[i].id == i1)
			pos1 = i;
		if(s[i].id == i2)
			pos2 = i;
	}
	for(i = 0; i < 8; ++i){
		s[pos1].b[i] = s[pos1].b[i] | s[pos2].b[i];
	}
	for(i = pos2; i < (n - 1); ++i){
		s[i].id = s[i + 1].id;
		for(int j = 0; j < 8; ++j){
			s[i].b[j] = s[i + 1].b[j];
		}
	}
	n--;
}
int main(int argc, char* argv[]){
	int n = 0, el, i, max = 8, ids;
	string L;
	set *s = new set[max], *tmp;
	if(argc < 2){
		cout<<"Supply file name in commandline argument";
		return -1;
	}
	ifstream fin(argv[1]);
	////////////////////
	////////Input///////
	////////////////////
	while(getline(fin,L)){
		stringstream LS(L);
		if(n >= max){
			max = 2 * max;
			tmp = new set[max];
			for(i = 0; i < n; ++i){
				tmp[i].id = s[i].id;
				for(int j = 0; j < 8; ++j){
					tmp[i].b[j] = s[i].b[j];
				}
			}
			delete [] s;
			s = tmp;
		}
		for(i = 0; i < 8; ++i){
			s[n].b[i] = 0;
		}
		s[n].id = n;
		while(LS >> el){
			s[n].b[el/32] = ((s[n].b[el/32]) | (1 << (el%32)));
		}
		++n;
	}
	fin.close();
	ids = n;
	int c = 0;
	while(c != 7){
		cout<<"1.Check membership\n2.Union\n3.Intersection\n4.Difference\n5.Merge\n6.Print sets\n7.Exit\t";
		cin >> c;
		switch(c){
			case 1: cout<<"Enter set id, and element: ";cin>>i>>el;
				if(s[i].b[el/32] & (1 << el%32))
					cout<<"Yes";
				else
					cout<<"No";
				cout<<endl;
				break;
			case 2: cout<<"Enter set ids: ";cin>>i>>el;
				_union(s,n,i,el,max,ids);
				break;
			case 3: cout<<"Enter set ids: ";cin>>i>>el;
				_inter(s,n,i,el,max,ids);
				break;
			case 4: cout<<"Enter set ids in order: ";cin>>i>>el;
				diff(s,n,i,el,max,ids);
				break;
			case 5: cout<<"Enter set ids in order: ";cin>>i>>el;
				merge(s,n,i,el);
				break;
			case 6: output(s,n);
				break;
			case 7:break;
			defeault:break;
		}
	}
	delete [] s;
	return 0;
}
