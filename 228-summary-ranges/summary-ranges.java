class Solution {
    public List<String> summaryRanges(int[] nums) {
        
        List<String> s=new ArrayList<>();
        if (nums.length==0){
            return s;
        }
        int st=nums[0];
        int i;
        int l=0;
        for(i=1;i<nums.length;i++){
            if(nums[i-1]+1==nums[i]){
                continue;

            }
            else{
                if(st!=nums[i-1]){
                    s.add(String.valueOf(st)+"->"+String.valueOf(nums[i-1]));
                }
                else{
                    s.add(String.valueOf(st));
                }
                
                    st=nums[i];
                    l=i;
                
            }

        }
        
            if(l<nums.length-1 && st!=nums[l+1]){
                    s.add(String.valueOf(st)+"->"+String.valueOf(nums[i-1]));
                }
            else{
                    s.add(String.valueOf(st));
                }    

        
        return s;
        
    }

}