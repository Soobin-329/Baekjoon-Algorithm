import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    // 연속합
    // 실버 2

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n];
        dp[0] = arr[0];

        for(int i=1; i<n; i++){
            dp[i] = arr[i];
            if(dp[i-1] > 0){
                dp[i] += dp[i - 1];
            }
        }

        int answer = -1001;
        // dp의 맥스 값 찾기
        for(int i = 0; i<n;i++){
            answer = Math.max(answer, dp[i]);
        }

        System.out.println(answer);
    }
}