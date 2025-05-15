import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    // 알고리즘 수업 - 피보나치 수 1
    // 브론즈 1

    private static int fib_count = 0;
    private static int dp_count = 0;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 재귀
        fib(n);

        // 동적 프로그래밍
        int[] dp = new int[n+1];
        dp[1] = dp[2] = 1;

        for(int i=3;i <= n;i++){
            dp[i] = dp[i-1] + dp[i-2];
            dp_count++;
        }

        System.out.println(fib_count + " " + dp_count);
    }

    //재귀
    private static int fib(int n){
        if (n == 1 | n == 2) {
            fib_count++;
            return 1;
        } else return (fib(n - 1) + fib(n - 2));
    }

}
