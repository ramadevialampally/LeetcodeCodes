class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer>s=new HashSet<>();
        for(int i: nums1){
            s.add(i);
        }
        Set<Integer> s2=new HashSet<>();
        for(int i:nums2){
            s2.add(i);
        }
        Set<Integer> diff1=new HashSet<>(s);
        diff1.removeAll(s2);
        Set<Integer> diff2=new HashSet<>(s2);
        diff2.removeAll(s);
        List<List<Integer>> res=new ArrayList<>();
        res.add(new ArrayList<>(diff1));
        res.add(new ArrayList<>(diff2));
        return res;

        
    }
}