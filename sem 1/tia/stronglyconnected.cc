#include<iostream>
#define GREY 1
#define WHITE 0
#define BLACK 2
#define ms 20
/****************/
/*   ms=maxsize */
/****************/
using namespace std;

struct gnode{
	int id,
	    arr,
	    fin,
	    color,
	    valid;
	int dfs_root,
	    dfs_parent_id,
	    is_dfs_root;
	struct alnode *adj,*in_adj;
};

struct alnode{
	int adj_id;
	struct alnode *n; //next
};

struct alnode* llinsert(alnode *head, int val){
	alnode *temp = new alnode,*temp2;
	temp->adj_id = val;
	temp->n = NULL;
	if(head == NULL){
		head = temp;
	}
	else{
		temp2 = head;
		while(temp2->n != NULL){
			temp2 = temp2->n;
		}
		temp2->n = temp;
	}
	return head;
}

void lltraverse(alnode *head){
	while(head != NULL){
		cout << head->adj_id << " ";
		head = head->n;
	}
	cout << endl;
}

/****************************/
/**because this is not java**/
/****************************/

void lldelete(alnode* head){
	if(head != NULL){
		if(head->n != NULL){
			lldelete(head->n);
			head->n = NULL;
		}
		delete head;
	}
}
void clear(gnode gr[], int V){
	for(int i = 0; i < V; ++i){
		lldelete(gr[i].adj);
		//lldelete(gr[i].in_adj);
	}
}

int dfs(int, gnode[], int, int, int, int);

int main(int argc, char *argv[])
{
	/******************/
	/* Declarations   */
	/******************/

	int V, A_temp, i, st, flag, t, ctr, ctra[ms];
	struct gnode graph[ms];
	
	/******************/
	/*  Taking input  */
	/******************/

	/**************************/
	/**Input format followed:**/
	/**1)Number of nodes*******/
	/**2)Adjacency matrix******/
	/**3)Start node id*********/
	/***Note: id is automatic-*/
	/***ally taken from matrix*/
	/***input order************/
	/**************************/
	
	cin >> V;
	for(i = 0;i < V;++i){
		graph[i].in_adj = NULL;
	}
	for(i = 0;i < V;++i){
		graph[i].id = i;
		graph[i].color = WHITE;
		graph[i].valid = 1;
		graph[i].adj = NULL;
		graph[i].dfs_root = -1;
		graph[i].dfs_parent_id = -1;
		graph[i].is_dfs_root = 0;
		for(int j = 0;j < V;++j){
			cin>>A_temp;
			if(A_temp && ( i!=j )){
				graph[i].adj = llinsert(graph[i].adj,j);
				graph[j].in_adj = llinsert(graph[j].in_adj,i);
			}
		}
	}
	for(i = V;i < ms;++i){
		graph[i].valid = 0;
	}
	cin>>st;
	graph[st].is_dfs_root = graph[st].valid?1:-1;
	graph[st].dfs_parent_id = -1;

	/****************/
	/* Init complete*/
	/****************/

	/************************/
	/*Testing adjacency list*/
	/************************/

	/*for(i = 0;i < V;++i){
		cout << i << ". ";
		lltraverse(graph[i].adj);
		lltraverse(graph[i].in_adj);
	}*/

	/***************/
	/*****dfs*******/
	/***************/

	t = dfs(st, graph, V, 1, st, 1);
	flag = 1;
	while(flag){
		for(i = 0; i < V; ++i){
			if( graph[i].color == WHITE ){
				graph[i].is_dfs_root = 1;
				graph[i].dfs_root = i;
				graph[i].dfs_parent_id = -1;
				t = dfs(i, graph, V, t + 1, i, 1);
			}
			else{
				flag = 0;
			}
		}
	}

	/*******************/
	/******New code*****/
	/*******************/
	
	for(i = 0; i < V; ++i){
		graph[i].color = WHITE;
		graph[i].is_dfs_root = 0;
		graph[i].dfs_root = -1;
		graph[i].dfs_parent_id = -1;
	}
	//selection sort
	int max,pos,index[ms];t=0;
	int tmp;
	for(i = 0; i < ms; ++i){
		if(i < V){
			index[i] = i;
		}
		else{
			index[i] = -1;
		}
	}
	for(i = 0; i < (V - 1); ++i){
		max = graph[index[i]].fin, pos = i;
		for(int j = i + 1; j < V; ++j){
			if(graph[index[j]].fin > max){
				max = graph[index[j]].fin;
				pos = j;
			}
		}
		if(i != pos){
			tmp = index[pos];
			index[pos] = index[i];
			index[i] = tmp;
		}
	}
	/*for(i = 0; i < V; ++i){
		cout<<"selection"<<index[i]<<":"<<graph[index[i]].fin<<endl;
	}*/
	//selection sort end
	for(i = 0; i < V; ++i){
		//cout<<graph[index[i]].id<<":"<<graph[index[i]].color<<":"<<graph[index[i]].dfs_root<<endl;
		if(graph[index[i]].color == WHITE){
			graph[index[i]].is_dfs_root = 1;
			graph[index[i]].dfs_root = index[i];
			graph[index[i]].dfs_parent_id = -1;
			t = dfs(index[i], graph, V, t + 1, index[i], 0);
		}
	}
	/*****************/
	/**New code ends**/
	/*****************/

	/****************/
	/***for output***/
	/****************/

	for(i = 0; i < V; ++i){
		ctra[i] = 0;
	}
	ctr = 0;
	for(i = 0; i < V; ++i){
		if(graph[index[i]].is_dfs_root){
			for(int j = 0; j < V; ++j){
				if(graph[index[j]].dfs_root == graph[index[i]].id)
					++ctra[index[i]];
			}
			if(ctra[index[i]] > 1)
				++ctr;
		}
	}

	/***************/
	/***The output**/
	/***************/

	cout<<"\nThere are "<<ctr<<" strongly connected components in the graph. The number of nodes are: ";
	for(i = 0; i < V; ++i){
		if(ctra[i] > 1)
		cout << ctra[i]<<", ";
	}
	cout<<"\b\b \nThe roots are: ";
	for(i = 0; i < V; ++i){
		if(graph[i].is_dfs_root && ctra[i] > 1)
			cout<<graph[i].id<<", ";
	}
	cout<<"\b\b \n";/*The arrival and finish time of the nodes are: \n";
	for(i = 0; i < V; ++i){
		cout<<i<<": arrival = "<<graph[i].arr<<": finish = "<<graph[i].fin<<endl;
	}*/

	//maintenance
	clear(graph, V);
	return 0;
}
int dfs(int u, gnode graph[], int V, int t, int root, int f){
	//cout<<u<<":";
	graph[u].arr = t;
	graph[u].color = GREY;
	graph[u].dfs_root = root;
	alnode *adj;
        if(f)
		adj = graph[u].adj;
	else
		adj = graph[u].in_adj;
	while(adj != NULL){
		if(graph[adj->adj_id].color == WHITE){
			graph[adj->adj_id].dfs_parent_id = u;
			t = dfs(adj->adj_id, graph, V, t + 1, root, f); 
		}
		adj = adj->n;
	}
	graph[u].fin = ++t;
	graph[u].color = BLACK;
	return t;
}
