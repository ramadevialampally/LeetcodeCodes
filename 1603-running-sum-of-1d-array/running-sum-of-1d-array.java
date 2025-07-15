class Solution {
    public int[] runningSum(int[] nums) {
        int[] a=new int[nums.length];
        int s=0;
        int j=0;
        for(int i:nums){
            s+=i;
            a[j]=s;
            j+=1;

        }
        return a;
        
    }
}