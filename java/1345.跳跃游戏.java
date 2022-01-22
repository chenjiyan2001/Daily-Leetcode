class Solution {
    // 1. O(n) 83ms(5%) O(n) 52.9M(57%)
    public int minJumps(int[] arr) {
        Map<Integer, List<Integer>> idxMap = new HashMap<>();
        int n = arr.length;
        int step = 0;
        for (int i = 0; i < arr.length; i++){
            List<Integer> list = idxMap.getOrDefault(arr[i], new ArrayList<>());
            list.add(i);
            idxMap.put(arr[i], list);
        }
        Deque<Integer> queue = new ArrayDeque();
        Set<Integer> walked = new HashSet<>();
        queue.addLast(0);
        while (!queue.isEmpty()){
            int size = queue.size();
            for (int j = 0; j < size; j++){
                int idx = queue.pollFirst();
                walked.add(idx);
                if (idx == n - 1) return step;
                List<Integer> list = idxMap.getOrDefault(arr[idx], new ArrayList<>());
                for (int m: list){
                    if (walked.contains(m)) continue;
                    queue.addLast(m);
                }
                idxMap.remove(arr[idx]);
                if (idx - 1 >= 0 && !walked.contains(idx - 1)){
                    queue.addLast(idx - 1);
                }
                if (idx + 1 < n && !walked.contains(idx + 1)){
                    queue.addLast((idx + 1));
                }
            }
            step++;
        }
        return -1;
    }
}