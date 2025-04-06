import java.util.Arrays;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=0;
        while(i<n){
            nums1[m]=nums2[i];
            i+=1;
            m+=1;
        }
        
        Arrays.sort(nums1);
    }
}