class Solution {
    public int maxSubArray(int[] nums) {
        
       int n=Integer.MIN_VALUE;
       int sum=0;
       for(int i=0;i<nums.length;i++){
        sum+=nums[i];
        n=Math.max(sum,n);
        if(sum<0){
            sum=0;
        }
        
            

       }
       return n;
    }
}