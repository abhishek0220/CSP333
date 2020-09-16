#include<bits/stdc++.h>
#define MAX_N 101
using namespace std;
int distance_bwt[MAX_N][MAX_N];
bool visited[MAX_N];
stack<int> path;
stack<int> path_selected;
int MIN_DIS = INT_MAX;

void dfs(int curr, int dist, int N , int final){
    visited[curr] = true;
    path.push(curr);
    if(curr == final){
        if(dist < MIN_DIS){
            MIN_DIS = dist;
            path_selected = path;
        }
        return;
    }
    else{
        for(int i=1; i<=N; i++){
            if(visited[i]) continue;
            dfs(i,dist + distance_bwt[curr][i],N, final);
        }
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
    int N, tem, pos_start, pos_end;
    cin>>N;
    for(int i=1; i<N; i++){
        for(int j=i+1; j<=N; j++){
            cin>>tem;
            distance_bwt[i][j] = tem;
            distance_bwt[j][i] = tem;
        }
    }
    cin>>pos_start>>pos_end;
    dfs(pos_end, 0, N, pos_start);
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