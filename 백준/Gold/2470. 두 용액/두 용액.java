import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // 두 용액
    // 골드 5

    private static final int MAX = (int)(Math.pow(10, 11));

    public static void main(String[] args) throws IOException{
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];

        for (int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        int left = 0;
        int right = n-1;

        int gap = MAX;
        int[] answer = {arr[left], arr[right]};
        int sum;

        while (left < right) {
            sum = arr[left] + arr[right];

            // 둘이 합한게 이전보다 0에 가까우면 갱신
            if (Math.abs(sum) < gap) {
                gap = Math.abs(sum);
                answer[0] = arr[left];
                answer[1] = arr[right];
            }

            // 둘이 합한게 0보다 크면 왼쪽 움직
            if (sum >= 0) {
                right--;
            }
            // 둘이 합한게 0보다 작으면 오른쪽으로 움직
            else {
                left++;
            }
        }

        System.out.println(answer[0] + " " + answer[1]);
    }

}
