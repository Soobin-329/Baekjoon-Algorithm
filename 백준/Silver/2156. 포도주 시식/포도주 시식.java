import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    // 포도주 시식
    // 실버 1

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n+1];
        int[] dp = new int[n+1];

        for(int i=1;i<=n;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        for(int i=1;i<=n;i++){
            if(i == 1){
                dp[1] = arr[1];
            }
            else if(i == 2){
                dp[2] = arr[1] + arr[2];
            } else {
                dp[i] = Math.max(dp[i - 1], Math.max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2]));
            }
        }

        System.out.println(dp[n]);
    }
}
