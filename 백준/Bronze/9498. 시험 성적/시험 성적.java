import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException {
        //입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        if (90 <= n) {
            System.out.println("A");
        }
        else if (80 <= n) {
            System.out.println("B");
        }
        else if (70 <= n) {
            System.out.println("C");
        }
        else if (60 <= n) {
            System.out.println("D");
        }
        else {
            System.out.println("F");
        }
    }
}
