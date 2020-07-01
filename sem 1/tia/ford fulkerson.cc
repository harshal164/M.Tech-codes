#include<iostream>
#include<climits>
#include<stack>
#define ms 10
using namespace std;
int fordfulkerson(int g[ms][ms], int v, int src, int d){
	int F = 0, i, vis[ms], min, f, pi[ms];
	//DFS
	stack<int> s;
	while(1){
		for(i = 0; i < ms; ++i){
			if(i < v)
			vis[i] = 0;
			else
			vis[i] = -1;
			pi[i] = -1;
		}
		s.push(src);
		min = INT_MAX;
		f = 0;
		while(!s.empty() && !f){
			i = s.top();
			s.pop();
			for(int j = 0; j < v; ++j){
				if(g[i][j] != 0 && vis[j] == 0 && i != j){
					vis[j] = 1;
					pi[j] = i;
					if(j == d){
						f = 1;
						s.push(j);
					}
					if(f)
						continue;
					s.push(j);
				}
			}
			vis[i] = 2;
		}
		while(!s.empty()){
			s.pop();
		}
		i = d;
		if(vis[d]){
			while(pi[i]!=-1){
				if(min > g[pi[i]][i])
					min = g[pi[i]][i];
				i = pi[i];
			}
			i = d;
			while(pi[i]!=-1){
				g[pi[i]][i]-= min;
				g[i][pi[i]]+= min;
				i = pi[i];
			}
			F+= min;
		}
		else
			break;
	}
	return F;
}
int main(int argc, char * argv[]){
	int Graph[ms][ms], V, src, snk;
	cin >> V;
	for(int i = 0; i < V; ++i){
		for(int j = 0; j < V; ++j){
			cin >> Graph[i][j];
		}
	}
	cin >> src >> snk;
	cout << fordfulkerson(Graph,V,src,snk) << endl;
	return 0;
}
