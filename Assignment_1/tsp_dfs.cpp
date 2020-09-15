#include<bits/stdc++.h>
#define MAX_N 101
using namespace std;
int distance_bwt[MAX_N][MAX_N];
bool visited[MAX_N];
stack<int> path;
stack<int> path_selected;
int MIN_DIS = INT_MAX;

void dfs(int curr, int dist, int N ){
    visited[curr] = true;
    path.push(curr);
    bool con = true;
    for(int i=1; i<=N; i++){
        if(visited[i]) continue;
        con = false;
        dfs(i,dist + distance_bwt[curr][i],N);
    }
    if(con && (dist+distance_bwt[curr][1] < MIN_DIS)){
        MIN_DIS = dist+distance_bwt[curr][1];
        path_selected = path;
        path_selected.push(1);
    }
    visited[curr] = false;
    path.pop();
}

int main(){
    #ifndef ONLINE_JUDGE
        // for getting input from input.txt
        freopen("input.txt", "r", stdin);
        // for writing output to output.txt
        freopen("output_dfs.txt", "w", stdout);
    #endif
    
    time_t start, end;
    time(&start);

    ios_base::sync_with_stdio(false);
    memset(visited, false, sizeof(MAX_N));
    int N, tem;
    cin>>N;
    for(int i=1; i<N; i++){
        for(int j=i+1; j<=N; j++){
            cin>>tem;
            distance_bwt[i][j] = tem;
            distance_bwt[j][i] = tem;
        }
    }
    dfs(1, 0, N);
    while(!path_selected.empty()){
        cout<<path_selected.top()<<" -> ";
        path_selected.pop();
    }
    cout<<"\nMIN Distance : "<<MIN_DIS<<"\n";
    time(&end);
    double time_taken = double(end - start);
    cout << "Time taken by program is : " << fixed << time_taken << setprecision(5); 
    cout << " sec " << endl; 
    return 0;
}