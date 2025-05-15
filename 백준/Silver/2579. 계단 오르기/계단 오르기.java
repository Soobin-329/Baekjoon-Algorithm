import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    // 계단 오르기
    // 실버 3

    static Integer[] dp;
    static int[] arr;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        dp = new Integer[n];
        arr = new int[n];

        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        dp[0] = arr[0];
        if(n > 1) {
            dp[1] = arr[0] + arr[1];
        }
        System.out.println(step(n-1));
    }

    private static int step(int i){
        if (i<0){
            return 0;
        }
        // i번째 계단을 무조건 밟는 선에서 얻을 수 있는 최고 점수
        if(dp[i] == null){
            dp[i] = Math.max(step(i-3) + arr[i-1] + arr[i], step(i-2) + arr[i]);
        }

        return dp[i];
    }
}
