// 1. O(logn) t:117ms(64%) O(n) m:91.4M(74%) 哈希表+红黑树
class StockPrice {
    int maxTimestamp;
    HashMap<Integer, Integer> timePriceMap;
    TreeMap<Integer, Integer> prices;

    public StockPrice() {
        maxTimestamp = 0;
        timePriceMap = new HashMap<Integer, Integer>();
        prices = new TreeMap<Integer, Integer>();
    }
    
    public void update(int timestamp, int price) {
        maxTimestamp = Math.max(maxTimestamp, timestamp);
        if (timePriceMap.containsKey(timestamp)){
            int old = timePriceMap.get(timestamp);
            int cnt = prices.get(old);
            if (cnt == 1) prices.remove(old);
            else prices.put(old, cnt - 1);
        }
        timePriceMap.put(timestamp, price);
        prices.put(price, prices.getOrDefault(price, 0) + 1);
    }
    
    public int current() {
        return timePriceMap.get(maxTimestamp);
    }
    
    public int maximum() {
        return prices.lastKey();
    }
    
    public int minimum() {
        return prices.firstKey();
    }
}

// 2. O(logn) t:71ms(91%) O(n) m:91.9M(47%) 哈希表+双优先队列
class StockPrice {
    int maxTimestamp;
    HashMap<Integer, Integer> timePriceMap;
    PriorityQueue<int[]> pqMax;
    PriorityQueue<int[]> pqMin;

    public StockPrice() {
        maxTimestamp = 0;
        timePriceMap = new HashMap<Integer, Integer>();
        pqMax = new PriorityQueue<int[]>((a, b) -> b[0] - a[0]);
        pqMin = new PriorityQueue<int[]>((a, b) -> a[0] - b[0]);
    }
    
    public void update(int timestamp, int price) {
        maxTimestamp = Math.max(maxTimestamp, timestamp);
        timePriceMap.put(timestamp, price);
        pqMax.offer(new int[]{price, timestamp});
        pqMin.offer(new int[]{price, timestamp});
    }
    
    public int current() {
        return timePriceMap.get(maxTimestamp);
    }
    
    public int maximum() {
        while (true) {
            int[] priceTime = pqMax.peek();
            int price = priceTime[0], timestamp = priceTime[1];
            if (timePriceMap.get(timestamp) == price) {
                return price;
            }
            pqMax.poll();
        }
    }
    
    public int minimum() {
        while (true) {
            int[] priceTime = pqMin.peek();
            int price = priceTime[0], timestamp = priceTime[1];
            if (timePriceMap.get(timestamp) == price) {
                return price;
            }
            pqMin.poll();
        }
    }
}
