import java.util.*;

class Solution {
    // 14:16 ~ 15:16 다시하기
    // 17:06 ~ 
    // 물웅덩이가 좌표가 반대라니 미친거 아닐까?
    
    // 인덱스 1에서 시작
    public int solution(int m, int n, int[][] puddles) {
        // int answer = 0;
        
        int[][] dp = new int[n][m];
        
        //물웅덩이가 있는 곳은 dp < -1
        for(int i=0;i<puddles.length;i++){
            int px = puddles[i][1] - 1;
            int py = puddles[i][0] - 1;
            dp[px][py] = -1;
        }
        
        // 행과 열이 0인 곳 1로 초기화 하기
        // 여긴 물웅덩이 만나면 없어짐
        for(int i=1;i<n;i++){
            if(dp[i][0] == -1){
                break;
            }
            dp[i][0] = 1;
        }
        for(int i=1;i<m;i++){
            if(dp[0][i] == -1){
                break;
            }
            dp[0][i] = 1;
        }
        
        for(int cx=1;cx<n;cx++){
            for(int cy=1 ; cy<m; cy++){
                // 물웅덩이를 만나면 뛰어넘기
                if(dp[cx][cy] == -1){
                    continue;
                }
             
                // 위와 왼쪽을 더하기
                if(dp[cx - 1][cy] != -1){
                    dp[cx][cy] += dp[cx - 1][cy];
                }
                if(dp[cx][cy - 1] != -1){
                    dp[cx][cy] += dp[cx][cy - 1];
                }
                dp[cx][cy] %= 1000000007;
            }
        }
        
        // System.out.println();
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<m;j++){
        //         System.out.print(dp[i][j]+" ");
        //     }
        //     System.out.println();
        // }
        // System.out.print(dp[n-1][m-1]);
                
        return dp[n-1][m-1];
    }
}