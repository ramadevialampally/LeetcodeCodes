class Solution {
    public boolean isPalindrome(int x) {
        int n=x;
        int res=0;
        while(x>0){
            int r=x%10;
            res=res*10+r;
            x=(int) x/10;
        }
        return res==n;
        
        
    }
}