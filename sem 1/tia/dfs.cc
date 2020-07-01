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
	struct alnode *adj;
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
	}
}

int dfs(int, gnode[], int, int, int);

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
	}*/

	/***************/
	/*****dfs*******/
	/***************/

	t = dfs(st, graph, V, 1, st);
	flag = 1;
	while(flag){
		for(i = 0; i < V; ++i){
			if( graph[i].color == WHITE ){
				graph[i].is_dfs_root = 1;
				graph[i].dfs_root = i;
				graph[i].dfs_parent_id = -1;
				t = dfs(i, graph, V, t + 1, i);
			}
			else{
				flag = 0;
			}
		}
	}

	/****************/
	/***for output***/
	/****************/

	ctr = 0;
	for(i = 0; i < V; ++i){
		if(graph[i].is_dfs_root){
			ctra[ctr] = 0;
			for(int j = 0; j < V; ++j){
				if(graph[j].dfs_root == i)
					++ctra[ctr];
			}
			++ctr;
		}
	}

	/***************/
	/***The output**/
	/***************/

	cout<<"\b\b \nThere are "<<ctr<<" dfs trees in the dfs forest.\nThe number of nodes in each tree (in order) are: ";
	for(i = 0; i < ctr; ++i){
		cout << ctra[i]<<", ";
	}
	cout<<"\b\b \nThe roots are: ";
	for(i = 0; i < V; ++i){
		if(graph[i].is_dfs_root)
			cout<<i<<", ";
	}
	cout<<"\b\b \nThe arrival and finish time of the nodes are: \n";
	for(i = 0; i < V; ++i){
		cout<<i<<": arrival = "<<graph[i].arr<<": finish = "<<graph[i].fin<<endl;
	}

	//maintenance
	clear(graph, V);
	return 0;
}
int dfs(int u, gnode graph[], int V, int t, int root){
	cout<<u<<", ";
	graph[u].arr = t;
	graph[u].color = GREY;
	graph[u].dfs_root = root;
	alnode *adj = graph[u].adj;
	while(adj != NULL){
		if(graph[adj->adj_id].color == WHITE){
			graph[adj->adj_id].dfs_parent_id = u;
			t = dfs(adj->adj_id, graph, V, t + 1, root); //recursive call.. think about stack implementation later
		}
		adj = adj->n;
	}
	graph[u].fin = ++t;
	graph[u].color = BLACK;
	return t;
}
