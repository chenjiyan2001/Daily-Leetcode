class Solution {
    // [题解]1. O(n) t:0ms(100%) O(1) m:42.1M(22%) 递归
    List<Integer> ans = new ArrayList<>();
    public List<Integer> preorder(Node root) {
        dfs(root);
        return ans;
    }

    void dfs(Node root) {
        if (root == null) return ;
        ans.add(root.val);
        for (Node node : root.children) dfs(node);
    }
    
    // [题解]2. O(n) t:9ms(10%) O(n) m:42.3M(8%) 迭代
    public List<Integer> preorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        Deque<Object[]> d = new ArrayDeque<>();
        d.addLast(new Object[]{root, 0});
        while (!d.isEmpty()) {
            Object[] poll = d.pollLast();
            Node t = (Node)poll[0]; Integer cnt = (Integer)poll[1];
            if (t == null) continue;
            if (cnt == 0) ans.add(t.val);
            if (cnt < t.children.size()) {
                d.addLast(new Object[]{t, cnt + 1});
                d.addLast(new Object[]{t.children.get(cnt), 0});
            }
        }
        return ans;
    }
}