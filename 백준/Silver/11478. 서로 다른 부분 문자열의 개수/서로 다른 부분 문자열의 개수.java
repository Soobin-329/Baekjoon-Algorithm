import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class Main {
    //서로 다른 부분 문자열의 개수
    // 실버 3

    //전역 변수 세팅
    static String input;
    static Set<String> answer = new HashSet<>();
    public static void main(String[] args) throws IOException {
        //입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine();
        
        //하나씩 돌아, 그리고 또 끝까지 달려 거기부터
        for (int i = 0; i<input.length();i++){
            // StringBuilder 활용법 알기!
            StringBuilder str = new StringBuilder();
            for (int j = i; j<input.length();j++){
                str.append(input.charAt(j));
                answer.add(str.toString());
            }
        }

        System.out.println(answer.size());
    }
}