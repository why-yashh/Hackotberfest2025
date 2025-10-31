#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> constructadj(int V, vector<vector<int>> &edges){
    
    vector<vector<int>> adj(V);
    for(auto it:edges){
        adj[it[0]].push_back(it[1]);
        adj[it[1]].push_back(it[0]);
    }
    return adj;
}
// Function to check if the graph is Bipartite using BFS
bool isBipartite(int V, vector<vector<int>> &edges) {

    // Vector to store colors of vertices.
    // Initialize all as -1 (uncolored)
    vector<int> color(V, -1);
    
    //create adjacency list
    vector<vector<int>> adj = constructadj(V,edges);
    // Queue for BFS
    queue<int> q;
    
    // Iterate through all vertices to handle disconnected graphs
    for(int i = 0; i < V; i++) {

        // If the vertex is uncolored, start BFS from it
        if(color[i] == -1) {

            // Assign first color (0) to the starting vertex
            color[i] = 0;
            q.push(i);
            
            // Perform BFS
            while(!q.empty()) {
                int u = q.front();
                q.pop();
                
                // Traverse all adjacent vertices
                for(auto &v : adj[u]) {

                    // If the adjacent vertex is uncolored,
                    // assign alternate color
                    if(color[v] == -1) {
                        color[v] = 1 - color[u];
                        q.push(v);
                    }

                    // If the adjacent vertex has the same color,
                    // graph is not bipartite
                    else if(color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
    }
    
    // If no conflicts in coloring, graph is bipartite
    return true;
}

int main() {
    int V = 4;
    vector<vector<int>> edges = {{0, 1}, {0, 2}, {1, 2}, {2, 3}};
    if(isBipartite(V, edges))
        cout << "true";
    else
        cout << "false";
    
    return 0;
}
