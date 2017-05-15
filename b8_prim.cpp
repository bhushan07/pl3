#include<iostream>
#include <omp.h>
using namespace std;

#define infinity 9999
#define MAX 20

int G[MAX][MAX],spanning[MAX][MAX],n;

int prims();

int main()
{
    int i,j,total_cost;
    cout<<"Enter no. of vertices:";
    cin>>n;

    cout<<"\nEnter the adjacency matrix:\n";

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            cin>>G[i][j];

	
    total_cost=prims();
    cout<<"\nspanning tree matrix:\n";

    for(i=0;i<n;i++)
    {
        cout<<"\n";
        for(j=0;j<n;j++)
         {
         if(spanning[i][j]==0)
         	cout<<"\t--";
         	else 
           cout<<"\t"<<spanning[i][j];
         }
    }

    cout<<"\n\nTotal cost of spanning tree="<<total_cost<<"\n";
    return 0;
}

int prims()
{
    int cost[MAX][MAX];
    int u,v,min_distance,distance[MAX],from[MAX];
    int visited[MAX],no_of_edges,i,min_cost,j;

    //create cost[][] matrix,spanning[][]
    cout<<"\n---------------creation of cost matrix-----------\n";
    for(i=0;i<n;i++)
    {
        #pragma omp parallel num_threads(n)
        {
            int k=omp_get_thread_num();
            
            cout<<"\nusing thread id: "<<k<<" ";
            if(G[i][k]==0)
                cost[i][k]=infinity;
            else
                cost[i][k]=G[i][k];
                spanning[i][k]=0;
            
        }
    }

    
    distance[0]=0;              //initialise visited[],distance[] and from[]
    visited[0]=1;
    
    cout<<"\n-----------initialising distance,from,vis-----------\n";
    #pragma omp parallel num_threads(n-1)
    {
    
        int i=omp_get_thread_num()+1;
         cout<<"\nusing thread id: "<<i-1;
        distance[i]=cost[0][i];
        from[i]=0;
        visited[i]=0;
    }

    min_cost=0;                 //cost of spanning tree
    no_of_edges=n-1;            //no. of edges to be added

    while(no_of_edges>0)
    {
                                //find the vertex at minimum distance from the tree
        min_distance=infinity;
        cout<<"\n-----------finding minimum distance-----------\n";
        #pragma omp parallel num_threads(n-1)
        {
            int i=omp_get_thread_num()+1;
             cout<<"\nusing thread id: "<<i-1;
            if(visited[i]==0&&distance[i]<min_distance)
            {
                v=i;
                min_distance=distance[i];
            }
        }
        u=from[v];

        
        spanning[u][v]=distance[v];     //insert the edge in spanning tree
        spanning[v][u]=distance[v];
        no_of_edges--;
        visited[v]=1;

                                        //updated the distance[] array
        #pragma omp parallel num_threads(n-1)
        {
            int i=omp_get_thread_num()+1;
            if(visited[i]==0&&cost[i][v]<distance[i])
            {
                distance[i]=cost[i][v];
                from[i]=v;
            }
        }

        min_cost=min_cost+cost[u][v];
    }

    return(min_cost);
}

