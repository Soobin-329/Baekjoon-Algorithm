import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    // 창문 닫기
    // 실버 5

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int count = 0;
        int n = Integer.parseInt(br.readLine());
        int i = 1;

        while((int)Math.pow(i, 2) <= n){
            count++;
            i++;
        }
        System.out.println(count);
    }
}
