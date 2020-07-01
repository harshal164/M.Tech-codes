#include<iostream>
#include<climits>
#define s 20
using namespace std;
struct gnode{
	int id, pi, marked, d;
	struct adj *a;
};
struct adj{
	int id, w;
	struct adj* n;
};
void llinsert(adj *&h, int id, int w){
	adj *tmp = new adj, *tmp2;
	tmp->n = NULL;
	tmp->id = id;
	tmp->w = w;
	if(h == NULL){
		h = tmp;
	}
	else{
		tmp2 = h;
		while(tmp2->n != NULL){
			tmp2 = tmp2->n;
		}
		tmp2->n = tmp;
	}
}
int min(gnode graph[], int v){
	int m, flag = 1;
	for(int i = 0; i < v; ++i){
		if(flag && !graph[i].marked){
			m = i;
			flag = 0;
		}
		if((!graph[i].marked) && graph[i].d < graph[m].d)
			m = i;
	}
	return m;
}
void takeinput(gnode[], int);
void process(gnode[], int, int);
void printoutput(gnode[], int);
int main(int argc, char* argv[]){
	gnode graph[s];
	int v, st;
	cin >> v;
	takeinput(graph, v);
	cin >> st;
	process(graph, v, st);
	printoutput(graph, v);
	return 0;
}
void takeinput(gnode graph[], int v){
	int W;
	for(int i = 0; i < v; ++i){
		graph[i].id = i;
		graph[i].pi = -1;
		graph[i].marked = 0;
		graph[i].d = INT_MAX;
		graph[i].a = NULL;
		for(int j = 0; j < v; ++j){
			cin >> W;
			if(W && i != j){
				llinsert(graph[i].a, j, W);
			}
		}
	}
}
void process(gnode graph[], int v, int st){
	graph[st].d = 0;
	int u;
	adj* a;
	for(int i = 0; i < v; ++i){
		u = min(graph, v);
		a = graph[u].a;
		while(a != NULL){
			if((!graph[a->id].marked) && graph[a->id].d > a->w){
				graph[a->id].d = a->w;
				graph[a->id].pi = u;
			}
			a = a->n;
		}
		graph[u].marked = 1;
	}
}
void printoutput(gnode graph[], int v){
	for(int i = 0; i < v; ++i){
		cout<<graph[i].id<<": d = "<<graph[i].d<<" parent = "<<graph[i].pi<<endl;
	}
}
