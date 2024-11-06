import java.util.*;

class Solution {
    public List<String> sortStrings(List<String> list) {
        list.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2); // 오름차순 정렬
            }
        });
        return list;
    }
}


list.sort((o1, o2) -> o1.compareTo(o2));
