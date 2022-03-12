class Solution {
    // 1. O(n) t:3ms(37%) O(n) m:42.5M(5%) 迭代
    public List<Integer> postorder(Node root) {
        Deque<Node> stack = new ArrayDeque<>();
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;
        stack.addLast(root);
        while (!stack.isEmpty()) {
            Node node = stack.pollLast();
            if (node == null) continue;
            for (Node n : node.children) {
                stack.addLast(n);
            }
            ans.add(node.val);
        }
        Collections.reverse(ans);
        return ans;
    }
}