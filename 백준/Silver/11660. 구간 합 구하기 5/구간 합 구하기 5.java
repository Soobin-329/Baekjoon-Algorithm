import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // 구간 합 구하기 5
    // 실버 1

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][n];

        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 누적합 구하기
        int[][] prefix = new int[n][n];

        prefix[0][0] = arr[0][0];

        // x=0, y=0 행열 채워주기
        for(int i=1;i<n;i++){
            prefix[i][0] = prefix[i-1][0] + arr[i][0];
            prefix[0][i] = prefix[0][i-1] + arr[0][i];
        }

        // 그 다음 안쪽 채워주기
        for(int x=1;x<n;x++){
            for(int y=1;y<n;y++){
                prefix[x][y] = arr[x][y] + prefix[x-1][y] + prefix[x][y-1] - prefix[x-1][y-1];
            }
        }

//        //누적합 출력
//        for(int i=0;i<n;i++){
//            for(int j=0;j<n;j++){
//                System.out.print(prefix[i][j]+" ");
//            }
//            System.out.println();
//        }
//        System.out.println();

        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            // 인덱스가 1부터 시작하니까 1 빼주고 시작
            int x1 = Integer.parseInt(st.nextToken()) - 1;
            int y1 = Integer.parseInt(st.nextToken()) - 1;
            int x2 = Integer.parseInt(st.nextToken()) - 1;
            int y2 = Integer.parseInt(st.nextToken()) - 1;

            int result = prefix[x2][y2];

            if (x1 != 0){
                result -= prefix[x1-1][y2];
            }
            if (y1 != 0){
                result -= prefix[x2][y1-1];
            }
            if (x1 != 0 & y1 != 0){
                result += prefix[x1-1][y1-1];
            }

//            System.out.println(prefix[x2][y2] +"-"+prefix[x1-1][y2]+"-"+prefix[x2][y1-1]+"+" prefix[x1-1][y1-1]);
            System.out.println(result);
//            System.out.println();
        }
    }
}
