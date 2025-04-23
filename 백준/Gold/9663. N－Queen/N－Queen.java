import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    // N-Queen
    // 골드 4

    // 전역 변수 설정
    static int n;
    static int answer = 0;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        int[] queens = new int[n];

        dfs(0, queens);

        System.out.println(answer);
    }

    
    private static void dfs(int x, int[] queens){
        if (x == n){
            answer++;
            return;
        }

        // x 행에서 퀸을 어디 열에 놓을지 반복문
        for (int y = 0; y < n; y++){
            boolean flag = true;

            //이때까지의 queens 돌기
            for (int row=0; row < x; row++){
                if (!flag) {
                    break;
                }
                // 같은 열에 있으면 안되고
                if (queens[row] == y) {
                    flag = false;
                    break;
                }

                // 대각선도 고려
                if (Math.abs(y - queens[row]) == Math.abs(x - row)) {
                    flag = false;
                    break;
                }
            }

            if (flag){
                queens[x] = y;
                dfs(x + 1, queens);
            }
        }
    }
}
