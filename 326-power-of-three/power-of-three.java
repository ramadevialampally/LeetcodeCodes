class Solution {
    boolean power(int n){
        if(n==1){
            return true;
        }
        if(n%3!=0 || n==0){
            return false;
        }
        return power(n/3);
    }
    public boolean isPowerOfThree(int n) {
    
        boolean ans= power(n);     
        return ans;   
    }
}