class Solution {
    public int search(int[] nums, int target) {
        List<Integer> li=new ArrayList<>();
        for(int i:nums){
            li.add(i);
        }
        return li.indexOf(target);
        
    }
}