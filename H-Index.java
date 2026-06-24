//this one is not so interesting its just the first medium level i solved with java...
class Solution {
    public int hIndex(int[] citations) {
        int max = 0;
        int l = citations.length;
        
        Arrays.sort(citations);
        for (int i = l - 1; i >= 0; i--){
            if (citations[i] <= l - i && citations[i] > max){
                return citations[i];
            }
            else if (citations[i] > l - i){
                if (l - i > max){
                    max = l - i;
                }
            }
        }

        return max;

    }
}
