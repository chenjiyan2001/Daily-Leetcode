class Solution {
public:
    // [题解]1. O(n) t:12ms(95%) O(1) m:11.4M(22%) 递归
    vector<int> ans;
    vector<int> preorder(Node* root) {
        dfs(root, ans);
        return ans;
    }

    void dfs(const Node* root, vector<int> &ans) {
        if (root == nullptr) return ;
        ans.emplace_back(root->val);
        for (auto &node : root->children){
            dfs(node, ans);
        }
    }

    // [题解]2. O(n) t:16ms(75%) O(n) m:11M(93%) 迭代
    vector<int> preorder(Node* root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        stack<Node *> st;
        st.emplace(root);
        while (!st.empty()) {
            Node *node = st.top();
            st.pop();
            ans.emplace_back(node->val);
            for (auto it = node->children.rbegin(); it != node->children.rend(); it++) {
                st.emplace(*it);
            }
        }
        return ans;
    }
};