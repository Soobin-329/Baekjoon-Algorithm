// 도키도키 간식드리미
// 실버 3
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        Stack<Integer> cur_line = new Stack<Integer>();
        Stack<Integer> spare_line = new Stack<Integer>();


        // 입력 배열 거꾸로 스택에 넣기
        st = new StringTokenizer(br.readLine());
        int[] tmp = new int[n];
        for (int i = 0; i < n; i++){
            tmp[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = n - 1; i >= 0; i--){
            cur_line.push(tmp[i]);
        }

        int standard = 1;

        while (true) {
            if (cur_line.isEmpty()){
                //스페어 라인에서 하나씩 꺼냈을때 순서가 맞으면 Nice
                while (!spare_line.isEmpty()){
                    int cur = spare_line.pop();
                    if (cur != standard) {
                        System.out.println("Sad");
                        return;
                    }
                    standard++;
                }
                System.out.println("Nice");
                return;
            }

            Integer cur = cur_line.peek();

            if (cur.equals(standard)){
                standard++;
                cur_line.pop();
                continue;
            }
            else if (!spare_line.isEmpty()){
                Integer spare_cur = spare_line.peek();
                if (spare_cur.equals(standard)){
                    standard++;
                    spare_line.pop();
                    continue;
                }
            }
            // 둘 다 맞지 않으면 cur에 있는거를 스페어로 옮겨야겠지!
            spare_line.push(cur_line.pop());
        }
    }
}