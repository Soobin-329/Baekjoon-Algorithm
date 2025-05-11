import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    //구간 합 구하기 4
    // 실버 3

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] nums = new int[n+1];
        for(int i=1;i<=n;i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // 누적합 구하기
        // arr
        // 0 1 2 3  4  5
        // 0 5 9 12 14 15
        int[] arr = new int[n+1];

        for(int i=1;i<=n;i++){
            arr[i] = arr[i-1] + nums[i];
        }

        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            System.out.println(arr[b] - arr[a-1]);
        }

    }
}
