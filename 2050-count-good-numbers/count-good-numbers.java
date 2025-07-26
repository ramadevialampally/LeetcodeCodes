class Solution {
    static long mod(long base,long ex,long mod){
        long res=1;
        base=base%mod;
        while(ex>0){
            if(ex%2!=0){
                res=(base*res)%mod;
            }
            base=(base*base)%mod;
            ex=ex/2;
        }
        return res;
    }
    public int countGoodNumbers(long n) {
        long mod=1_000_000_007;
        long evenv=(n+1)/2;
        long oddv=(n)/2;
        long res1=mod(5,evenv,mod);
        long res2=mod(4,oddv,mod);
        long res3=(res1*res2)%mod;
        return (int) res3;


    }
}