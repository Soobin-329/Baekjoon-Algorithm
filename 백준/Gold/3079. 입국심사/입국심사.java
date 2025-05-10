import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    // 입국심사
    // 골드 5

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        int max = -1;

        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(br.readLine());
            max = Math.max(max, arr[i]);
        }

        long start = 1;
        long end = max * m;
        long mid = 0;
        long answer = end;

        while(start <= end){
            mid = (start + end)/2;

            long processed = process_people(mid, arr, m);

            if (processed >= m){
                end = mid - 1;
                answer = mid;
            }
            else {
                start = mid + 1;
            }
        }
        System.out.println(answer);
    }

    private static long process_people(long num, int[] arr, long m){
        long result = 0;

        // arr 원소 하나씩 나눈 몫을 더해서 반환
        for (int i=0;i<arr.length;i++){
            result += num/arr[i];
            //TODO: 안해주면 오버플로 남..?!
            if (result >= m){
                break;
            }
        }
        return result;
    }
}
