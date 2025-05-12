import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    // K번째 수
    // 골드 1

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        long start = 1;
//        int end = Math.min(1000000000, n*n);
        long end = k;

        while (start < end){
            long mid = (start+end)/2;

            long order = 0;
            for(int i=1;i<=n;i++){
                order += Math.min(mid / i, n);
            }

            if (order >= k){
                //TODO: 왜 end = mid - 1; 은 안되는거임?
                end = mid;
            }
            else{
                start = mid + 1;
            }
        }

        System.out.println(start);
    }
}
