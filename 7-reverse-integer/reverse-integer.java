class Solution {
    public int reverse(int x) {
        
        long res=0;
        int m=x;
        if(x<0){
            m*=-1;
        }
        while(m>0){
            int r=m%10;
            res=res*10+r;
            m=(int) m/10;
        }
        if(x<0){
            res*=-1;
        }
        if(res <Integer.MIN_VALUE || res>Integer.MAX_VALUE){
            return 0;
        }
        return (int) res;
    }
}