class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> h =new HashMap<>();
        List<Integer> list=new ArrayList<>();
        for(int i:nums){
            list.add(i);
        }
        for(int i=0;i<nums.length;i++){
            h.put(nums[i],i);
        }
        int[] res=new int[2];
        for(int i=0;i<nums.length;i++){
            int x=target-nums[i];
            if(list.contains(x) && list.indexOf(x)!=i){
                res[0]=i;
                res[1]=list.indexOf(x);
                return res;
            }
        }
        return new int[0];
        
        
    }
}