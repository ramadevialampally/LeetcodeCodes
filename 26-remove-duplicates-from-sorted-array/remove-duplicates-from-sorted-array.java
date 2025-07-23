class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length==1){
            return nums.length;
        }
        int c=0;
        ArrayList<Integer> a=new ArrayList<>();
        a.add(nums[0]);
        for(int i=1;i<nums.length;i++){
            if(nums[i]>=nums[i-1]+1){
                a.add(nums[i]);
                c+=1;
            }
            
        }
       
        for(int i=0;i<a.size();i++){
            nums[i]=a.get(i);
        }
          return c+1;
        
    }
  
}