class Solution {
    public int firstMissingPositive(int[] nums) {
        int m=Integer.MIN_VALUE;
        
        for(int i:nums){
            m=Math.max(m,i);

        }
        if(m<0){
            return 1;
        }
         Set<Integer> set = new HashSet<>();
    for (int i : nums) {
        set.add(i);
    }

    for (int i = 1; i <= m; i++) {
        if (!set.contains(i)) {
            return i;
        }
    }

    return m + 1;
}
        
    }
