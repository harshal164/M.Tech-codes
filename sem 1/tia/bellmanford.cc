#include<iostream>
#include<climits>
#define s 20
using namespace std;
struct edge{
	int u, v, w;
};
int find(edge[], int, int, int);
int takeinput(int [], int[], int[], edge[], int);
void process(int[], int[], int[], edge[], int, int, int);
void printoutput(int[], int[], int[], edge[], int, int);
int main(int argc, char* argv[]){
	int id[s], pi[s], d[s];
	int v, st, es;
	edge e[s];
	cin >> v;
	es = takeinput(id, pi, d, e, v);
	cin >> st;
	process(id, pi, d, e, v, es, st);
	printoutput(id, pi, d, e, es, v);
	return 0;
}
int find(edge e[], int es, int u, int v){
	for(int i = 0; i < es; ++i){
		if((e[i].u == u && e[i].v == v) || (e[i].u == v && e[i].v == u))
		return 1;
	}
	return 0;
}
int takeinput(int id[], int pi[], int d[], edge e[], int v){
	int W, i, ctr = 0;
	for(i = 0; i < v; ++i){
		pi[i] = -1;
		d[i] = INT_MAX;
		for(int j = 0; j < v; ++j){
			cin >> W;
			if(W && i != j && !find(e,ctr,i,j)){
				e[ctr].u = i;
				e[ctr].v = j;
				e[ctr++].w = W;
			}
		}
	}
	return ctr;
}
void process(int id[], int pi[], int d[], edge e[], int v, int es, int st){
	d[st] = 0;
	for(int i = 0; i < v; ++i){
		for(int j = 0; j < es; ++j){
			if(d[e[j].v] > d[e[j].u] + e[j].w){
				d[e[j].v] = d[e[j].u] + e[j].w;
				pi[e[j].v] = e[j].u;
			}
		}
	}
}
void printoutput(int id[], int pi[], int d[], edge e[], int es, int v){
	for(int i = 0; i < v; ++i){
		cout<<i<<": d = "<<d[i]<<" parent = "<<pi[i]<<endl;
	}
}
