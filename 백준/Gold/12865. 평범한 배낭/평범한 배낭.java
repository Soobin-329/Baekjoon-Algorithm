import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    // 평범한 배낭
    // 골드 5

    static Integer[][] dp;
    static int[] w;
    static int[] v;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        dp = new Integer[n][k+1];
        w = new int[n];
        v = new int[n];

        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());

            w[i] = Integer.parseInt(st.nextToken());
            v[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(knapsack(n-1, k));
    }

    private static int knapsack(int i, int j){
        if(i < 0){
            return 0;
        }

        if(dp[i][j] == null){
            if(w[i] > j){
                dp[i][j] = knapsack(i-1, j);
            }
            else{
                dp[i][j] = Math.max(knapsack(i-1, j), v[i]+knapsack(i-1, j-w[i]));
            }
        }
        return dp[i][j];
    }
}
