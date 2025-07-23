class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Double> a=new ArrayList<>();
        for(int i=0;i<nums1.length;i++){
            a.add((double)nums1[i]);
        }
        for(int j=0;j<nums2.length;j++){
            a.add((double)nums2[j]);
        }
        Collections.sort(a);
        if(a.size()%2!=0){
            return a.get((int)a.size()/2);
        }
        else{
            return (a.get((int)a.size()/2)+a.get(((int)a.size()/2)-1))/2;
        }

        
    }
}