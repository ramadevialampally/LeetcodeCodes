class Solution {
    public int[] searchRange(int[] nums, int target) {
        
       HashMap<Integer,Integer> h=new HashMap<>();
       for(int i=0;i<nums.length;i++){
        if(nums[i]==target){
            h.put(nums[i],i);
        }
       }
       int[] a={-1,-1};
       if (nums.length==0){
        return a;
       }
       int st=-1;
       for(int i=0;i<nums.length;i++){
            if(nums[i]==target){
                st=i;
                break;
            }
       }
       if(st>-1){
            a[0]=st;
            a[1]=h.get(target);

       }
       
       return a;
    }
}