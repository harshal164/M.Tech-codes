#include<iostream>
#define WHITE 0
#define GREY 1
#define BLACK 2
#define ms 20
/****************/
/**ms = maxsize**/
/****************/

using namespace std;

/*************************/
/***struct declarations***/
/*************************/

struct gnode{
	int id,
	    color,
	    bfs_parent,
	    is_bfs_root,
	    bfs_root;
	struct alist *adj;
};

struct alist{
	int id;
	struct alist *n;
};

/***************/
/***functions***/
/***************/

struct alist *ginsert(alist *head, int v){
	alist *temp = new alist, *temp2;
	temp->id = v;
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

void lltraverse(alist *head){
	while(head != NULL){
		cout << head->id<<", ";
		head = head->n;
	}
	cout<<"\b\b \b\n";
}

/*******************************/
/***for manupalting the queue***/
/*******************************/

void qins(alist *&head, alist *&tail, int v){
	alist *temp = new alist;
	temp->id = v;
	temp->n = NULL;
	if(head == NULL){
		head = tail = temp;
	}
	else{
		temp->n = tail;
		tail = temp;
	}
}
int qdel(alist *&head, alist *&tail){
	alist *temp;
	int retVar = -1;
	if(head == NULL || tail == NULL){
		head = tail = NULL;
	}
	else{
		temp = tail;
		if(temp == head){
			retVar = temp->id;
			tail = head = NULL;
			delete temp;
		}
		else{
			while(temp->n != head){
				temp = temp->n;
			}
			head = temp;
			temp = temp->n;
			retVar = temp->id;
			head->n = NULL;
			delete temp;
		}
	}
	return retVar;
}
int qempty(alist *head, alist *tail){
	return (head == NULL || tail == NULL);
}

/***************************************/
/**auxiliary memory clearing functions**/
/***************************************/

void lldelete(alist *head){
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

int bfs(int, gnode[], int, int);

int main(int argc, char *argv[]){
	
	/********************************/
	/**Declaring, priming and input**/
	/********************************/

	/**************************/
	/**Input format followed:**/
	/**1)Number of nodes*******/
	/**2)Adjacency matrix******/
	/**3)Start node id*********/
	/***Note: id is automatic-*/
	/***ally taken from matrix*/
	/***input order************/
	/**************************/
	int i, V, st, adj, t, flag;
	gnode graph[ms];

	cin >> V;
	for(i = 0; i < V; ++i){
		graph[i].id = i;
		graph[i].color = WHITE;
		graph[i].bfs_parent = -1;
		graph[i].is_bfs_root = 0;
		graph[i].bfs_root = -1;
		graph[i].adj = NULL;
		for(int j = 0; j< V; ++j){
			cin >> adj;
			if( adj ){
				graph[i].adj = ginsert(graph[i].adj, j);
			}
		}
	}
	cin >> st;
	graph[st].is_bfs_root = 1;
	graph[st].bfs_parent = -1;
	
	/************************/
	/*Testing adjacency list*/
	/************************/

	/*for(i = 0;i < V;++i){
		cout << i << ". ";
		lltraverse(graph[i].adj);
	}*/
	
	/****************************/
	/*************BFS************/
	/****************************/

	bfs(st, graph, V, st);
	flag = 1;
	while(flag){
		for(i = 0; i < V; ++i){
			if(graph[i].color == WHITE){
				graph[i].bfs_parent = -1;
				graph[i].is_bfs_root = 1;
				bfs(i, graph, V, i);
			}
			else
				flag = 0;
		}
	}

	/******************************/
	/***because this is not java***/
	/******************************/
	
	clear(graph,V);
	return 0;
}

int bfs(int u, gnode graph[], int V, int root){
	/************************************************/
	/***This is non recursive queue implementation***/
	/************************************************/

	graph[u].bfs_root = root;
	alist *head,*tail,*trav;
	int cur;
	head = tail = NULL;
	qins(head, tail, u);
	
	while(!qempty(head,tail)){
		cur = qdel(head, tail);
		graph[cur].color = GREY;
		cout << cur << ", "; //bfs order output
		trav = graph[cur].adj;
		while(trav!=NULL){
			if(graph[trav->id].color == WHITE){
				qins(head, tail, trav->id);
				graph[trav->id].color = GREY;
				graph[trav->id].bfs_parent = cur;
			}
			trav = trav->n;
		}
		graph[cur].color = BLACK;
	}
	cout<<"\b\b \b\n";
}
