import java.util.*;

class Solution {
    // key = genre
    // value = [[index, plays], ...]
    
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        HashMap<String, ArrayList<int[]>> map = new HashMap<>();
        HashMap<String, Integer> sum_map = new HashMap<>();
        
        // 해시맵에 넣기 + 재생횟수 장르별로 더하기
        for(int i=0;i<genres.length;i++){
            String cur = genres[i];
            // 없으면 초기화하고 추가
            // 있으면 그냥 추가
            if(!map.containsKey(cur)){
                map.put(cur, new ArrayList<>());
                sum_map.put(cur, 0);
            }
            map.get(cur).add(new int[]{i, plays[i]});          
            sum_map.replace(cur, sum_map.get(cur) + plays[i]);
        }
        
        // plays는 더 많게(내림), i는 더 작게(오름) 으로 정렬
        for(String key:map.keySet()){
            ArrayList<int[]> arr = map.get(key);

            arr.sort((o1, o2) -> {
                if(o1[1] - o2[1] == 0){
                    return o1[0] - o2[0];
                }
                return o2[1] - o1[1];
            });
        }
        
        int prev_max = Integer.MAX_VALUE;
        int cur_max = -1;
        String cur_genre = "";
        
        for(int i=0;i<sum_map.size();i++){
            // 장르를 하나씩 돌면서 이전 Max보다 작고 가장 큰거를 고른다
            for(String key:sum_map.keySet()){
                int cur = sum_map.get(key);
                if(cur < prev_max){
                    if(cur_max < cur){
                        cur_max = cur;
                        cur_genre = key;
                    }
                }
            }
            
            // 해당 장르에서 첫번째와 두번째 노래를 받아온다.
            // 길이가 1 이상이면 두번째 노래를 받아온다
            answer.add(map.get(cur_genre).get(0)[0]);
            if(map.get(cur_genre).size() > 1){
                answer.add(map.get(cur_genre).get(1)[0]);
            }
            
            prev_max = cur_max;
            cur_max = -1;
            cur_genre = "";
        }
        
        
        int[] answer_arr = new int[answer.size()];
        for(int i=0;i<answer.size();i++){
            answer_arr[i] = (int) answer.get(i);
        }
        
        return answer_arr;
    }
}