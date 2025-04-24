import java.util.Set;
import java.util.HashSet;


class Solution {
    
    /*
    1. 숫자를 조합(문자열 -> int)
    2. 소수 판별
    3. 정답 저장(HashSet)
    */
    
    public boolean[] isPrime;
    
    public void isPrime_fun(int n){ 
        isPrime = new boolean[n+1];
        
        for(int i = 0; i < isPrime.length; i++){
            isPrime[i] = true;
        }
        
        isPrime[0] = isPrime[1] = false; 
        
        for(int i = 2; i <= Math.sqrt(n); i++){ 
            if(isPrime[i]){
                // i의 배수는 소수가 아니다
                for(int j = i*i; j <= n; j += i){
                    isPrime[j] = false;
                }
            }
        }
    } 
    
    
    public Set<Integer> combis = new HashSet<>();
    
    // n개를 골라 조합을 만들어주는 거
    public void combination(int depth, boolean[] visited, String str, int n, String input){
        if(depth == n) {
            combis.add(Integer.parseInt(str));
            return;
        }
        
        for (int i = 0; i < input.length(); i++){
            if (visited[i]){
                continue;
            }
            visited[i] = true;
            combination(depth + 1, visited, str + input.charAt(i), n, input);
            visited[i] = false;
        }
    } 
    
    
    public int solution(String numbers) {
        int answer = 0;
        int n = numbers.length();
        
        // 1. 숫자를 조합(문자열 -> int)        
        boolean[] visited = new boolean[n];
        
        for (int i=1;i <= n; i++){
            combination(0, visited, "", i, numbers);
        }
        
        // 2. 소수 판별
        isPrime_fun(9999999);
        
        Integer[] arr = combis.toArray(new Integer[0]);
        
        for (int i=0;i < arr.length;i++){
            if(isPrime[arr[i]]){
                answer++;
            }
        }        
        
        return answer;
    }
}