#include <bits/stdc++.h>
using namespace std;

struct Node
{
  Node *links[26];
  bool flag;
  Node()
  {
    for (int i = 0; i < 26; ++i)
      links[i] = nullptr;
    flag = false;
  }
  bool containskey(char ch) { return links[ch - 'a'] != nullptr; }
  void put(char ch, Node *node) { links[ch - 'a'] = node; }
  Node *get(char ch) { return links[ch - 'a']; }
  void setend() { flag = true; }
  bool isend() { return flag; }
};

class Trie
{
private:
  Node *root;

public:
  Trie() { root = new Node(); }

  void insert(const string &word)
  {
    Node *node = root;
    for (char c : word)
    {
      if (!node->containskey(c))
        node->put(c, new Node());
      node = node->get(c);
    }
    node->setend();
  }

  bool search(const string &word)
  {
    Node *node = root;
    for (char c : word)
    {
      if (!node->containskey(c))
        return false;
      node = node->get(c);
    }
    return node->isend();
  }

  bool startsWith(const string &prefix)
  {
    Node *node = root;
    for (char c : prefix)
    {
      if (!node->containskey(c))
        return false;
      node = node->get(c);
    }
    return true;
  }
};

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  Trie trie;
  int Q;
  if (!(cin >> Q))
    return 0;

  // Operations:
  // 1 word      -> insert(word)
  // 2 word      -> search(word)       -> prints "true"/"false"
  // 3 prefix    -> startsWith(prefix) -> prints "true"/"false"
  while (Q--)
  {
    int type;
    string s;
    cin >> type >> s;

    // ensure lowercase a-z for this implementation
    // (remove this transform if you already guarantee lowercase)
    for (char &c : s)
      c = tolower(c);

    if (type == 1)
    {
      trie.insert(s);
    }
    else if (type == 2)
    {
      cout << (trie.search(s) ? "true" : "false") << "\n";
    }
    else if (type == 3)
    {
      cout << (trie.startsWith(s) ? "true" : "false") << "\n";
    }
  }
  return 0;
}
