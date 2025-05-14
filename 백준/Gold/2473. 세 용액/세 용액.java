import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    
    // 세 용액
    // 골드 3
  

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        long[] arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        long min = Long.MAX_VALUE;
        long a1 = 0, a2 = 0, a3 = 0;

        // i=0~n-3 : 가장 오른쪽 인덱스
        for(int i=0;i < n-2; i++){
            int left = i+1;
            int right = n-1;

            while(left < right){
                long sum = arr[i]+arr[left]+arr[right];

                //갱신
                if (Math.abs(sum) < Math.abs(min)){
                    a1 = arr[i];
                    a2 = arr[left];
                    a3 = arr[right];
                    min = sum;
                }

                if (sum == 0){
                    break;
                }
                else if (sum < 0){
                    left++;
                }
                else {
                    right--;
                }
            }
        }
        System.out.println(a1+" "+a2+" "+a3);
    }
}
