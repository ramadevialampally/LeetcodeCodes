class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> h=new HashSet<>();
        for(int i:nums2){
            h.add(i);
        }
        Set<Integer> a=new HashSet<>();
        for(int j:nums1){
            if(h.contains(j)){
                a.add(j);

            }
        }
        int[] arr=new int[a.size()];
        int i=0;
        for(int k:a){
            arr[i]=k;
            i+=1;
        }
       
        return arr;

        
    }
}