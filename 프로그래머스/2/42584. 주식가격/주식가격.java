class Solution {    
    
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        
        for (int i=0;i<n-1 ; i++){
            for (int j=i; j < n-1; j++){
                if (prices[j] >= prices[i]){
                    answer[i] += 1;
                }
                else{
                    break;
                }
            }
        }
        
        answer[n-1] = 0;
        
        
        return answer;
    }
}