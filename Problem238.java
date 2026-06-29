// this problem is weird btw
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int l = nums.length - 1;
        int[] right = new int[l + 1];
        int[] left = new int[l + 1];
        int sum = 1;
        for (int i = l; i >= 0; i --){
            sum *= nums[i];
            left[i] = sum;
        }
        sum = 1;
        for (int i = 0; i <= l; i ++){
            sum *= nums[i];
            right[i] = sum;
        }
        int[] answer = new int[l + 1];
        sum = 1;
        
        for (int i = 0; i <= l; i ++){
            if (i == 0){
                sum = left[1];
            }
            else if (i == l){
                sum = right[l - 1];
            }
            else {
                sum = right[i - 1] * left[i + 1];
            }

            answer[i] = sum;


        }

    return answer;
}
}
