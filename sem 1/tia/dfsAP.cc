#include<climits>
#include<iostream>
#define s 20
#define WHITE 0
#define GREY 1
#define BLACK 2
using namespace std;
struct gnode{
	int id, aT, low, color, nC, flag;
	struct adj *a;
};
struct adj{
	int id;
	adj *n;
};
void llinsert(adj *&h, int id){
	adj *tmp = new adj, *tmp2;
	tmp->n = NULL;
	tmp->id = id;
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
void takeinput(gnode graph[], int v){
	int A;
	for(int i = 0; i < v; ++i){
		graph[i].id = i;
		graph[i].color = WHITE;
		//graph[i].aT = -1;
		graph[i].flag = 0;
		graph[i].low = INT_MAX;
		graph[i].a = NULL;
		graph[i].nC = 0;		
		for(int j = 0; j < v; ++j){
			cin >> A;
			if(A && i != j){
				llinsert(graph[i].a, j);
			}
		}
	}
}
void printoutput(gnode graph[], int v){
	for(int i = 0; i < v; ++i){
		cout<<graph[i].id<<": flag = "<<graph[i].flag<<endl;
	}
}
int dfsAP(gnode graph[], int v, int u, int t){
	int tmp, retVar;
	tmp = graph[u].low = graph[u].aT = t;
	graph[u].color = GREY;
	adj *a = graph[u].a;
	while(a != NULL){
		if(graph[a->id].color == WHITE){
			graph[u].nC++;
			retVar = dfsAP(graph, v, a->id, t + 1);
			t = retVar + 1;
			if(retVar >= graph[u].low)
				graph[u].flag = 1;
			else if(tmp > retVar)
				tmp = retVar;
		}
		else if(graph[a->id].color == GREY && tmp > graph[a->id].low){
			tmp = graph[a->id].low;
		}
		a = a->n;
	}
	graph[u].color = BLACK;
	if(graph[u].low > tmp)
		graph[u].low = tmp;
	return graph[u].low;
}
void process(gnode graph[], int v, int st){
	dfsAP(graph, v, st, 1);
	if(graph[st].nC > 1)
		graph[st].flag = 1;
}
int main(int argc, char*argv[]){
	gnode graph[s];
	int v, st;
	cin >> v;
	takeinput(graph, v);
	cin >> st;
	process(graph, v, st);
	printoutput(graph, v);
	return 0;
}
