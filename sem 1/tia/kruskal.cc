#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
class set{
	public:
	struct set *p;
	int rank;
	int val;
	set(int val){
		this->p = this;
		this->rank = 0;
		this->val = val;
	}
};
void link(set *x, set *y){
	if(x->rank > y->rank)
		y->p = x;
	else
		x->p = y;
	if(x->rank == y->rank)
		y->rank = y->rank + 1;
}
set* findSet(set *x){
	if(x!=x->p)
		x->p = findSet(x->p);
	return x->p;
}
void _union(set *x, set *y){
	link(findSet(x),findSet(y));
}
struct edge{
	int u,v,w;
};
int main(int argc, char* argv[]){
	int n,A_ij, ctr = 0, mstctr = 0;
	edge edges[100],mst[100];
	cin>>n;
	set *a[n];
	for(int i = 0; i < n; ++i)
		a[i] = new set(i);
	for(int i = 0; i < n; ++i){
		for(int j = 0; j < n; ++j){
			cin>>A_ij;
			if(A_ij){
				edges[ctr].u = i;
				edges[ctr].v = j;
				edges[ctr++].w = A_ij;
			}
		}
	}
	cout<<ctr<<endl;
	int pos,min;
	for(int i = 0; i < ctr - 1; ++i){
		pos = i, min = edges[i].w;
		for(int j = i + 1; j < ctr; ++j){
			if(edges[j].w < min){
				pos = j;
				min = edges[j].w;
			}
		}
		if(pos!=i){
			edge t = edges[i];
			edges[i] = edges[pos];
			edges[pos] = t;
		}
	}
	for(int i = 0; i < ctr; ++i){
		cout<<edges[i].w<<" ";
	}
	cout<<endl;
	for(int i = 0; i < ctr; ++i){
		if(findSet(a[edges[i].u]) != findSet(a[edges[i].v])){
			_union(a[edges[i].u],a[edges[i].v]);
			mst[mstctr++] = edges[i];
		}
	}
	for(int i = 0; i < mstctr; ++i){
		cout<<mst[i].u<<"-"<<mst[i].w<<"->"<<mst[i].v<<"\n";
	}
}
