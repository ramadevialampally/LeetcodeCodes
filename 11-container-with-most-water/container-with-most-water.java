class Solution {
    public int maxArea(int[] height) {
        int res=0;
        int s=0;
        int end=height.length-1;
        while(s<end){
            int v=(end-s)*Math.min(height[end],height[s]);
            if(height[s]>height[end]){
                end-=1;
            }
            else{
                s+=1;
            }
            res=Math.max(res,v);
        }
        return res;
        
    }
}