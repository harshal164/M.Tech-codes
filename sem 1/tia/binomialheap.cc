#include<iostream>
#include<cstdlib>
#include<ctime>
#define maxvalue 20
using namespace std;
int gc = 0;
struct trnode{
	int v,d;//value and degree
	struct trnode *c, *s, *p;//child, sibling and parent pointer
};
void llinsert(trnode *&s, trnode *&ins, trnode *&par){
	if(s == NULL){
		s = ins;
	}
	else{
		ins->s = s;
		s = ins;
	}
	s->p = par;
	par->d = par->d + 1;
}
void merge(trnode *&h1, trnode *h2){
	if(h1 != NULL && h2 != NULL){
		if(h1->v < h2->v){
			if(h1->c != NULL)
				llinsert(h1->c->s,h2,h1);
			else
				llinsert(h1->c,h2,h1);
		}
		else{
			if(h2->c != NULL)
				llinsert(h2->c->s,h1,h2);
			else
				llinsert(h2->c,h1,h2);
			h1 = h2;
		}
	}
}
void rm_arr(trnode *head[], int pos){
	for(int i = pos; i < gc - 1; ++i){
		head[i] = head[i+1];
	}
	gc--;
}
void merge2(trnode *head[], int p){
	int pos = p, fl = 1;
	while(fl){
		fl = 0;
		for(int i = 0; i < gc; ++i){
			if(head[i]->d == head[pos]->d && i != pos){
				merge(head[i],head[pos]);
				fl = 1;
				rm_arr(head,pos);
				pos = i;
			}
		}
	}
}
void insert(trnode *head[], int v){
	trnode *tmp = new trnode;
	tmp->c=tmp->s=tmp->p=NULL;
	tmp->v = v;
	tmp->d = 0;
	head[gc++] = tmp;
	int pos = gc - 1, fl = 1;
	while(fl){
		fl = 0;
		for(int i = 0; i < gc; ++i){
			if(head[i]->d == head[pos]->d && i != pos){
				merge(head[i],head[pos]);
				fl = 1;
				rm_arr(head,pos);
				pos = i;
			}
		}
	}
}
void printtree(trnode *h){
	cout<<h->v<<" ";
	if(h->c!=NULL)
		printtree(h->c);
	if(h->s!=NULL)
		printtree(h->s);
}
int get_min(trnode *head[]){
	int min = head[gc - 1]->v;
	for(int i =0; i < gc; ++i){
		if(min > head[i]->v)
			min = head[i]->v;
	}
	return min;
}
void sort(trnode *head[]){
	int min,pos;
	for(int i = 0; i < gc - 1; ++i){
		min = head[i]->d;
		pos = i;
		for(int j = i+1 ;j < gc; ++j){
			if(head[j]->d < min){
				min = head[j]->d;
				pos = j;
			}
		}
		if(i!=pos){
			trnode *tmp = head[i];
			head[i] = head[pos];
			head[pos] = tmp;
		}
	}
}
int extract_min(trnode* head[]){
	int p=0,min=head[0]->v;
	for(int i = 1; i < gc; ++i){
		if(min>head[i]->v){
			p = i;
			min = head[i]->v;
		}
	}
	trnode *s,*tmp;
	if(head[p]->c != NULL){
		head[gc++] = head[p]->c;
		head[p]->c->p = NULL;
		s = head[p]->c->s;
		head[p]->c->s = NULL;
		while(s!=NULL){
			head[gc++] = s;
			tmp = s->s;
			s->s = NULL;
			s = tmp;
		}
	}
	tmp = head[p];
	rm_arr(head,p);
	delete tmp;
	sort(head);
	/*for(int i = 0; i < gc; ++i){
		merge2(head,i);
	}*/
	return min;
}
int main(int argc, char *argv[]){
	srand(time(0));
	int a[20];
	trnode *head[maxvalue];
	for(int i = 0; i < maxvalue; ++i){
		head[i] = NULL;
	}
	for(int i = 0; i < 20; ++i)
		a[i] = 0;
	for(int i = 0; i <= 12; ++i){
		int tmp = rand()%20;
		while(a[tmp]){
			tmp = rand()%20;
		}
		a[tmp] = 1;
		cout<<"Inserting "<<tmp<<endl;
		insert(head,tmp);
	}
	sort(head);
	cout<<"Binomial Heap is: ";
	for(int i = 0; i < gc; ++i){
		cout<<"||head "<<head[i]->v<<"||";
		printtree(head[i]);
	}
	while(gc > 0){
		cout<<"\nExtracting minimum: "<<extract_min(head)<<" "<<gc<<endl;
	}
	return 0;
}
