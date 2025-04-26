import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        
        for(int i=0;i<scoville.length;i++){
            queue.add(scoville[i]);
        }
        
        while (queue.size() > 1){
            int first = queue.poll();
            int second = queue.poll();
            
            if(first >= K){
                break;
            }
            
            queue.add(first + second*2);
            answer++;
        }
        
        //만들수 없으면 -1을 return 하라는데에
        if (queue.size() == 1){
            int last = queue.poll();
            if (last < K){
                return -1;
            }
        }
        
        return answer;
    }
}